from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password or not email or not phone:
            return render(request, 'user_signup.html', {'error': 'All fields are required.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'user_signup.html', {'error': 'Username already exists.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'user_signup.html', {'error': 'Email is already registered.'})

        if not phone.isdigit() or len(phone) < 7:
            return render(request, 'user_signup.html', {'error': 'Enter a valid mobile number.'})
        send_mail(
             subject="Hello ,Thank you for signing up to our website",
             message="your account have been created..",
             from_email="Curelink<onboarding@resend.dev>",
             recipient_list= [email],
             html_message="<strong>Your account has been successfully created!</strong>",
        )

        login(request, user)
        return redirect('/dashboard/')

    return render(request, 'user_signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        return render(request, 'user_login.html', {'error': 'Invalid credentials'})

    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')