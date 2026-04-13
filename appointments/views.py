from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import resend
from .models import Appointment
from patients.models import Patient
from doctors.models import doctor
from datetime import datetime

@login_required
def appointment_list(request):
    appoinments = Appointment.objects.all()
    return render(request, 'app_list.html', {'appointments': appoinments})
@login_required
def doctor_appointments(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor_appointments.html', {
        'appointments': appointments
    })
@login_required
def appointment_delete(request,pk):
    appointment = get_object_or_404(Appointment,pk=pk)
    appointment.delete()
    return redirect('/appointments')
@login_required
def appointment_edit(request,pk):
    appointment =get_object_or_404(Appointment,pk=pk)
    if request.method =='POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_datetime = datetime.combine(
            datetime.strptime(appointment_date, '%Y-%m-%d').date(),
            datetime.strptime(appointment_time, '%H:%M').time()
        )
        patient_name = request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        
        try:
            patient = Patient.objects.get(name=patient_name)
            doctor_obj = doctor.objects.get(name=doctor_name)
            
            appointment.patient = patient
            appointment.doctor = doctor_obj
            appointment.appointment_time = appointment_datetime
            appointment.save()
            return redirect('/appointments')
        except (Patient.DoesNotExist, doctor.DoesNotExist) as e:
            error_msg = f'Patient or Doctor not found. Please check the names: Patient={patient_name}, Doctor={doctor_name}'
            patients = Patient.objects.all()
            doctors = doctor.objects.all()
            return render(request, 'app_edit.html', {'appointment': appointment, 'error': error_msg, 'patients': patients, 'doctors': doctors})
    
    patients = Patient.objects.all()
    doctors = doctor.objects.all()
    return render(request, 'app_edit.html', {'appointment': appointment, 'patients': patients, 'doctors': doctors})
@login_required
def appointment_create(request):
    if request.method =='POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        appointment_datetime = datetime.combine(
            datetime.strptime(appointment_date, '%Y-%m-%d').date(),
            datetime.strptime(appointment_time, '%H:%M').time()
        )
        patient_name = request.POST.get('patient_name')
        doctor_name = request.POST.get('doctor_name')
        
        try:
            patient = Patient.objects.get(name=patient_name)
            doctor_obj = doctor.objects.get(name=doctor_name)
            
            Appointment.objects.create(
                patient=patient,
                doctor=doctor_obj,
                appointment_time=appointment_datetime,
                appointment_status=request.POST.get('appointment_status')
            )
            return redirect('/appointments')
        except (Patient.DoesNotExist, doctor.DoesNotExist):
            # Handle case where patient or doctor doesn't exist
            patients = Patient.objects.all()
            doctors = doctor.objects.all()
            return render(request, 'app_create.html', {'error': 'Patient or Doctor not found', 'patients': patients, 'doctors': doctors})
    
    patients = Patient.objects.all()
    doctors = doctor.objects.all()
    return render(request,'app_create.html', {'patients': patients, 'doctors': doctors})

