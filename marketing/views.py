from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'marketing_home.html')

def contact(request):
    return render(request, "marketing_contact.html")