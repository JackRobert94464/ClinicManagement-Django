# dashboardguiv2/urls.py

from django.urls import path
from . import views

app_name = 'dashboardguiv2'

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),

    path('doctor/', views.doctor_view, name='doctor_view'),
    path('nurse/', views.nurse_view, name='nurse_view'),
    path('cashier/', views.cashier_view, name='cashier_view'),
    path('manager/', views.manager_view, name='manager_view'),
    path('receptionist/', views.receptionist_view, name='receptionist_view'),
    
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('register_patient/', views.register_patient, name='register_patient'),
    path('view_patient/', views.view_patient_information, name='view_patient'),
    path('setup_appointment/', views.setup_appointment, name='setup_appointment'),
    path('complete_appointment/', views.complete_appointment, name='complete_appointment'),
    path('appointment_complete/', views.appointment_complete, name='appointment_complete'),
    path('edit_record/', views.edit_record, name='edit_record'),
    path('view_record/', views.view_record, name='view_record'),
    path('prescribe/', views.prescribe, name='prescribe'),
    path('prescription_success/', views.prescription_success, name='prescription_success'),
    path('estimate_prices/', views.estimate_prices, name='estimate_prices'),
    path('collect_fees/', views.collect_fees, name='collect_fees'),
    path('collect_fees/<int:patient_id>/', views.collect_fees, name='collect_fees'),
    path('change_regulation/', views.change_regulation, name='change_regulation'),
    path('change_regulation_success/', views.change_regulation_success, name='change_regulation_success'),
    path('create_monthly_report/', views.create_monthly_report, name='create_monthly_report'),
    path('view_monthly_report/', views.view_monthly_report, name='view_monthly_report'),
] 