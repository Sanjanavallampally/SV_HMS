from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.contrib.auth.decorators import login_required

# Create your views here
@login_required
def patient_list(request):
      patients = Patient.objects.all()
      return render(request, 'lists.html',  {'patients': patients})


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.save()
        return redirect('/patients')
    return render(request, 'patient_edit.html', {'patient': patient})

@login_required
def patient_delete(request,pk):
     patient = get_object_or_404(Patient,pk=pk)
     patient.delete()
     return redirect('/patients')
@login_required
def patient_create(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        Patient.objects.create(
            name=name,
            phone=phone,
            email=email
        )
        return redirect('/patients')
     return render(request,'patient_create.html')