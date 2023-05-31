from django.test import TestCase

# Create your tests here.
from .models import Patient, Billing

patient = Patient.objects.get(pk=1)  # Assuming patient ID is 1
billing = Billing(patient=patient, exam_fee=100, drug_fee=50, total_fee=150)
billing.save()

drug = Drug(name='Paracetamol', price=10)
drug.save()

drug = Drug(name='Amphetamine', price=100)
drug.save()