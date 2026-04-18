from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from google import genai
from django.conf import settings
from appointments.models import Appointment
from doctors.models import doctor
from patients.models import Patient
import markdown_it
# Create your views here.
@login_required
def dashboard_home(request):
    return render(request, 'dashboard_home.html')


@login_required
def dashboard_hms_ai(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        doctors = doctor.objects.all()
        patients = Patient.objects.all()
        appointments = Appointment.objects.all()
        doctors = list(doctors.values())
        patients = list(patients.values())
        appointments = list(appointments.values())

        final_query = f'''
            You are the AI chatbot inside a website called CurelinkHMS
            You responsibility is to answer questions about
            CurelinkHMS data. Anything part from this, you are not allowed to
            answer. Below is the doctor data you need to know. 
            {doctors} ,
            below are patients {patients}
            and below are appointments {appointments}

           Answer below:
            {user_query}
            ''' 
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=final_query,
        )
        md = markdown_it.MarkdownIt()
        answer = md.render(response.text)

        return render(request, "dashboard_hms_ai.html", {
            'answer': answer
        })
    return render(request, "dashboard_hms_ai.html")




# projects/969694106790
# 969694106790
