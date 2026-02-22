from django.shortcuts import render, redirect
from .models import Candidate, Company
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def register_view(request):
    if request.method == 'POST':
        if request.POST.get('role') == 'candidate':
            name = request.POST.get('fullName')
            university = request.POST.get('university')
            major = request.POST.get('major')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            password = make_password(request.POST.get('password'))
            if Candidate.objects.filter(email=email).exists():
                print("Email already exists:", email)
                return render(request, 'core/register.html', {'error': 'Email already exists'})

            candidate = Candidate(name=name, university=university, major=major, email=email, phone_number=phone_number, password=password)
            candidate.save()
            print("Candidate registered successfully with email:", email)
            return redirect('login')
        elif request.POST.get('role') == 'company':
            name = request.POST.get('companyName')
            taxid = request.POST.get('taxCode')
            major = request.POST.get('industry')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            password = make_password(request.POST.get('password'))
            if Company.objects.filter(email=email).exists():
                print("Email already exists:", email)
                return render(request, 'core/register.html', {'error': 'Email already exists'})

            company = Company(name=name, taxid=taxid, major=major, email=email, phone_number=phone_number, password=password)
            company.save()
            print("Company registered successfully with email:", email)
            return redirect('login')
    print("Nothing posted, rendering register page")
    return render(request, 'core/register.html')

def login_view(request):
    print("Login view accessed")
    if request.method == 'POST':
        if request.POST.get('user_type') == 'candidate':
            email = request.POST.get('email')
            password = request.POST.get('password')

            print("Received login data - Email:", email, "Password:", password)
            try:
                candidate = Candidate.objects.get(email=email)
                if check_password(password, candidate.password):
                    print("Login successful for email:", email)
                else:
                    print("Invalid password for email:", email)
                    messages.error(request, 'Invalid password')
                    return render(request, 'core/login.html', {'error': 'Invalid password'})
                return redirect('home')
            except Candidate.DoesNotExist:
                print("No candidate found with email:", email)
                messages.error(request, 'Cannot find an candidate with that email')
                return render(request, 'core/login.html', {'error': 'Cannot find an candidate with that email'})
        elif request.POST.get('user_type') == 'company':
            email = request.POST.get('email')
            password = request.POST.get('password')

            print("Received login data - Email:", email, "Password:", password)
            try:
                company = Company.objects.get(email=email)
                if check_password(password, company.password):
                    print("Login successful for email:", email)
                else:
                    print("Invalid password for email:", email)
                    messages.error(request, 'Invalid password')
                    return render(request, 'core/login.html', {'error': 'Invalid password'})
                return redirect('home')
            except Company.DoesNotExist:
                print("No company found with email:", email)
                messages.error(request, 'Cannot find an company with that email')
                return render(request, 'core/login.html', {'error': 'Cannot find an company with that email'})
    print("Nothing posted, rendering login page")
    return render(request, 'core/login.html')

def check_email(request):
    email = request.GET.get('email')
    exists = Candidate.objects.filter(email=email).exists() or Company.objects.filter(email=email).exists()
    print("Checking email:", email, "Exists:", exists)
    return JsonResponse({'exists': exists})

