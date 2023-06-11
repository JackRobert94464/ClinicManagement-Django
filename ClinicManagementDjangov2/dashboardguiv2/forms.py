from django import forms
from .models import Patient

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth']  # Add other fields here

from django import forms

class EstimatePriceForm(forms.Form):
    drug_id = forms.IntegerField(label='Drug ID')

from .models import Regulation

class ChangeRegulationForm(forms.ModelForm):
    class Meta:
        model = Regulation
        fields = ['title', 'content']

from django import forms
from .models import MonthlyReport

class MonthlyReportForm(forms.ModelForm):
    class Meta:
        model = MonthlyReport
        fields = ['month', 'year', 'num_patients', 'drug_usage', 'revenue']

from django import forms

class RegistrationForm(forms.Form):
    ROLES = [
        ('receptionist', 'Receptionist'),
        ('manager', 'Manager'),
        ('nurse', 'Nurse'),
        ('doctor', 'Doctor'),
        ('cashier', 'Cashier'),
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLES)

