from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import doctor as Doctor

# Create your views here.
@login_required
def doctor_list(request):
      doctors = Doctor.objects.all()
      return render(request, 'list_doc.html',  {'doctors': doctors})
@login_required
def doctor_delete(request, pk):
      doctor = get_object_or_404(Doctor, pk=pk)
      doctor.delete()
      return redirect('/doctors')
@login_required
def doctor_edit(request, pk):
      doctor = get_object_or_404(Doctor, pk=pk)
      if request.method == 'POST':
          doctor.name = request.POST.get('name', doctor.name)
          doctor.email = request.POST.get('email', doctor.email)
          doctor.specialization = request.POST.get('specialization', doctor.specialization)
          doctor.rating = request.POST.get('rating', doctor.rating)
          doctor.save()
          return redirect('/doctors')
      return render(request, 'doc_edit.html', {'doctor': doctor})

@login_required
def doctor_create(request):
      if request.method == 'POST':
            Doctor.objects.create(
                 name = request.POST.get('name'),
                 email = request.POST.get('email'),
                 specialization = request.POST.get('specialization'),
                 rating = request.POST.get('rating')
            )
            return redirect('/doctors')
      return render(request,'doc_create.html')
