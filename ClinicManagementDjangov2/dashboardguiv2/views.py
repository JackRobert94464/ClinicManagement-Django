from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse  # Import the HttpResponse class

# Create your views here.
# views.py

from .models import Service

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

def appointment(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        appointment_date = request.POST.get('appointment_date')
        message = request.POST.get('message')

        # Perform any necessary processing with the form data
        # For example, you could save the appointment details to the database
        
        # Display a success message
        messages.success(request, 'Appointment submitted successfully!')

        # Redirect to a thank you page or any other relevant page
        # return redirect('thank_you')

    # If the request method is not POST, render the form template
    return render(request, 'appointment.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the appropriate view based on the user's role
            return redirect('dashboardguiv2:index')
        else:
            # Display login unsuccessful message
            return render(request, 'login.html', {'message': 'Login unsuccessful'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Redirect to the main screen or login page after logout
    return redirect('dashboardguiv2:login')

@login_required
def receptionist_view(request):
    # Logic for receptionist view
    return render(request, 'receptionist.html')

@login_required
def manager_view(request):
    # Logic for manager view
    return render(request, 'manager.html')

@login_required
def nurse_view(request):
    # Logic for nurse view
    return render(request, 'nurse.html')

@login_required
def doctor_view(request):
    # Logic for doctor view
    return render(request, 'doctor.html')

@login_required
def cashier_view(request):
    # Logic for cashier view
    return render(request, 'cashier.html')

def unauthorized_view(request):
    return HttpResponse("Unauthorized access")  # Customize the response content as needed

# Routing and access control
@login_required
def index(request):
    if request.user.is_superuser:
        return redirect('dashboardguiv2:manager_view')
    if request.user.groups.filter(name='Receptionist').exists():
        return redirect('dashboardguiv2:receptionist_view')
    if request.user.groups.filter(name='Nurse').exists():
        return redirect('dashboardguiv2:nurse_view')
    if request.user.groups.filter(name='Doctor').exists():
        return redirect('dashboardguiv2:doctor_view')
    if request.user.groups.filter(name='Cashier').exists():
        return redirect('dashboardguiv2:cashier_view')

    # Display an error message or redirect to a default page for other roles or unauthorized users
    return HttpResponse("Unauthorized access")  # Customize the response content as needed





from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User.objects.create_user(username=username, email=email, password=password)
            if role in ['manager', 'admin']:
                group = Group.objects.get(name='Manager')  # Replace 'Manager' with the appropriate group name
                user.is_staff = True
                user.is_superuser = True
            else:
                group = Group.objects.get(name=role.capitalize())  # Assuming group names are capitalized role names
            user.groups.add(group)
            user.save()

            return redirect('dashboardguiv2:registration_success')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')


from .forms import PatientRegistrationForm

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register_patient.html', {'form': form})

from .models import Patient

def view_patient_information(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        name = request.POST.get('name')
        # Perform validation and retrieve patient information
        try:
            if patient_id:
                patient = Patient.objects.get(id=patient_id)
            elif name:
                patient = Patient.objects.get(name=name)
            else:
                return render(request, 'view_patient.html', {'error': 'Please provide a valid patient ID or name.'})

            return render(request, 'view_patient.html', {'patient': patient})
        except Patient.DoesNotExist:
            return render(request, 'view_patient.html', {'error': 'Patient not found.'})
    else:
        return render(request, 'view_patient.html')


from .models import Patient, Appointment

def setup_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        # Validate patient ID
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return render(request, 'setup_appointment.html', {'error': 'Invalid patient ID. Please try again.'})

        # Fetch available appointment itineraries
        itineraries = get_available_itineraries()  # Replace with your logic to retrieve available itineraries

        return render(request, 'setup_appointment.html', {'patient': patient, 'itineraries': itineraries})
    else:
        return render(request, 'setup_appointment.html')

def get_available_itineraries():
    # Replace with your logic to retrieve and return available appointment itineraries
    # This could involve querying the database or calling an external API
    return ['Itinerary 1', 'Itinerary 2', 'Itinerary 3']

from datetime import date


def complete_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        itinerary = request.POST.get('itinerary')
        # Validate patient ID and itinerary
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return render(request, 'complete_appointment.html', {'error': 'Invalid patient ID. Please try again.'})

        # Create appointment
        appointment = Appointment(patient=patient, appointment_date=date.today())  # Set appointment_date to today's date
        appointment.save()

        return redirect('dashboardguiv2:appointment_complete')
    else:
        return redirect('dashboardguiv2:setup_appointment')

def appointment_complete(request):
    return render(request, 'appointment_complete.html')


from django.shortcuts import render, redirect
from .models import Patient, MedicalRecord

def edit_record(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        illness = request.POST.get('illness')
        date = request.POST.get('date')
        symptom = request.POST.get('symptom')
        # Validate patient ID
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return render(request, 'edit_record.html', {'error': 'Invalid patient ID. Please try again.'})
        # Create or modify medical record
        record, created = MedicalRecord.objects.update_or_create(patient=patient,
                                                                 defaults={'illness': illness, 'date': date, 'symptom': symptom})
        return redirect('dashboardguiv2:edit_record')
    else:
        return render(request, 'edit_record.html')

def view_record(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        # Validate patient ID
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return render(request, 'view_record.html', {'error': 'Invalid patient ID. Please try again.'})
        # Retrieve medical record
        try:
            record = MedicalRecord.objects.get(patient=patient)
        except MedicalRecord.DoesNotExist:
            record = None
        return render(request, 'view_record.html', {'record': record})
    else:
        return render(request, 'view_record.html')


from .models import Prescription

def prescribe(request):
    error_message = ''
    
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        drug = request.POST.get('drug')

        # Perform validation and save the prescription to the database
        try:
            patient = Patient.objects.get(id=patient_id)
            prescription = Prescription(patient=patient, drug=drug)
            prescription.save()
            return redirect('dashboardguiv2:prescription_success')
        except Patient.DoesNotExist:
            error_message = 'Patient ID is not correct. Please enter a valid ID.'

    return render(request, 'prescribe.html', {'error_message': error_message})

def prescription_success(request):
    return render(request, 'prescription_success.html')


from django.shortcuts import render
from .models import Drug, Bill
from .forms import EstimatePriceForm

#drug = Drug(name='Paracetamol', price=10)
#drug.save()

#drug = Drug(name='Amphetamine', price=100)
#drug.save()


def estimate_prices(request):
    error_message = ''
    drug = None
    total_price = None

    if request.method == 'POST':
        form = EstimatePriceForm(request.POST)
        if form.is_valid():
            drug_id = form.cleaned_data['drug_id']
            try:
                drug = Drug.objects.get(id=drug_id)
                total_price = drug.price
            except Drug.DoesNotExist:
                error_message = 'Drug ID is not correct. Please enter a valid ID.'
    else:
        form = EstimatePriceForm()

    return render(request, 'estimate_prices.html', {
        'form': form,
        'drug': drug,
        'total_price': total_price,
        'error_message': error_message
    })


from django.shortcuts import render, get_object_or_404
from .models import Patient, Bill, Payment

def collect_fees(request, patient_id=None):
    if patient_id is None:
        patients = Patient.objects.all()
        return render(request, 'select_patient.html', {'patients': patients})

    patient = get_object_or_404(Patient, pk=patient_id)
    bill = Bill.objects.get(patient=patient)

    if request.method == 'POST':
        amount_paid = request.POST.get('amount_paid')
        payment = Payment(bill=bill, amount_paid=amount_paid)
        payment.save()

        bill.paid = True
        bill.save()

        return render(request, 'payment_success.html', {'patient': patient})

    return render(request, 'collect_fees.html', {'patient': patient, 'bill': bill})



from django.shortcuts import render
from .forms import ChangeRegulationForm
from .models import Regulation

def change_regulation(request):
    if request.method == 'POST':
        form = ChangeRegulationForm(request.POST)
        if form.is_valid():
            regulation = form.save()  # Save the form data and get the Regulation object
            return render(request, 'change_regulation_success.html')
    else:
        form = ChangeRegulationForm()

    return render(request, 'change_regulation.html', {'form': form})


def change_regulation_success(request):
    return render(request, 'change_regulation_success.html')

from django.shortcuts import render, redirect
from .forms import MonthlyReportForm
from .models import MonthlyReport

def create_monthly_report(request):
    if request.method == 'POST':
        form = MonthlyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardguiv2:report_success')
    else:
        form = MonthlyReportForm()
    return render(request, 'create_monthly_report.html', {'form': form})

def view_monthly_report(request):
    reports = MonthlyReport.objects.all()
    return render(request, 'view_monthly_report.html', {'reports': reports})

def report_success(request):
    return render(request, 'report_success.html')

from django.shortcuts import render, redirect
from .forms import MonthlyReportForm
from .models import MonthlyReport

def create_monthly_report(request):
    if request.method == 'POST':
        form = MonthlyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardguiv2:report_success')
    else:
        form = MonthlyReportForm()
    return render(request, 'create_monthly_report.html', {'form': form})

def view_monthly_report(request):
    reports = MonthlyReport.objects.all()
    return render(request, 'view_monthly_report.html', {'reports': reports})

def report_success(request):
    return render(request, 'report_success.html')
from django.shortcuts import render, redirect
from .forms import MonthlyReportForm
from .models import MonthlyReport

def create_monthly_report(request):
    if request.method == 'POST':
        form = MonthlyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardguiv2:report_success')
    else:
        form = MonthlyReportForm()
    return render(request, 'create_monthly_report.html', {'form': form})

def view_monthly_report(request):
    reports = MonthlyReport.objects.all()
    return render(request, 'view_monthly_report.html', {'reports': reports})

def report_success(request):
    return render(request, 'report_success.html')
from django.shortcuts import render, redirect
from .forms import MonthlyReportForm
from .models import MonthlyReport

def create_monthly_report(request):
    if request.method == 'POST':
        form = MonthlyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboardguiv2:report_success')
    else:
        form = MonthlyReportForm()
    return render(request, 'create_monthly_report.html', {'form': form})

def view_monthly_report(request):
    reports = MonthlyReport.objects.all()
    return render(request, 'view_monthly_report.html', {'reports': reports})

def report_success(request):
    return render(request, 'report_success.html')
