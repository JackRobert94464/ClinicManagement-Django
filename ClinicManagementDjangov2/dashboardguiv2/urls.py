from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dashboardguiv2'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('dashboard/', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),

    path('doctor/', login_required(views.doctor_view), name='doctor_view'),
    path('nurse/', login_required(views.nurse_view), name='nurse_view'),
    path('cashier/', login_required(views.cashier_view), name='cashier_view'),
    path('manager/', login_required(views.manager_view), name='manager_view'),
    path('receptionist/', login_required(views.receptionist_view), name='receptionist_view'),

    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('register_patient/', login_required(views.register_patient), name='register_patient'),
    path('view_patient/', login_required(views.view_patient_information), name='view_patient'),
    path('setup_appointment/', login_required(views.setup_appointment), name='setup_appointment'),
    path('complete_appointment/', login_required(views.complete_appointment), name='complete_appointment'),
    path('appointment_complete/', login_required(views.appointment_complete), name='appointment_complete'),
    path('edit_record/', login_required(views.edit_record), name='edit_record'),
    path('view_record/', login_required(views.view_record), name='view_record'),
    path('prescribe/', login_required(views.prescribe), name='prescribe'),
    path('prescription_success/', login_required(views.prescription_success), name='prescription_success'),
    path('estimate_prices/', login_required(views.estimate_prices), name='estimate_prices'),
    path('collect_fees/', login_required(views.collect_fees), name='collect_fees'),
    path('collect_fees/<int:patient_id>/', login_required(views.collect_fees), name='collect_fees'),
    path('change_regulation/', login_required(views.change_regulation), name='change_regulation'),
    path('change_regulation_success/', login_required(views.change_regulation_success), name='change_regulation_success'),
    path('create_monthly_report/', login_required(views.create_monthly_report), name='create_monthly_report'),
    path('view_monthly_report/', login_required(views.view_monthly_report), name='view_monthly_report'),
]
