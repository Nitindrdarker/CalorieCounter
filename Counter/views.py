from django.shortcuts import render,redirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile
# Create your views here.
def home(request):
    
    
    mydefaultvalue = 1.0
    mydefaultgender = 'male'
    if request.method ==  'POST':
        try:
            exercise = request.POST['exercise']
            
        except Exception:
            exercise = 1.2
            
        try:
            
            age = int(request.POST['age'])
            
        except Exception:
            
            age = 50
            
        try:
            
            height = int(request.POST['height'])
            
        except Exception:
            
            height = 175
            
        try:
            
            gender = request.POST['gender']
            
        except Exception:
            
            gender = 'male'
            
        try:
            
            weight = int(request.POST['weight'])
        except Exception:
            
            weight = 75
        bmi = (weight)/((height/100)**2)
        if (gender == 'male'):
            bmr = 66.47 + (13.75 * weight) + (5.003 * weight) - (6.755 * age)
            res = bmr * float(exercise)
        elif(gender == 'female'):
            bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
            res = bmr * float(exercise)
        if request.user.is_authenticated:
            profile = Profile.objects.create(user=request.user, bmr = bmr, res=res, bmi = bmi)
            profile.save()
        return render(request, 'home.html', {'bmr':bmr, 'res':res, 'bmi':bmi})
        
        
    else:
        return render(request, 'home.html')

  
    
def registration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        if (User.objects.filter(username=fname).exists() or User.objects.filter(email=email).exists()):
            messages.info(request, "First name or email already exists ! ")
            return redirect('register')
        elif(fname == '' or email == '' or password == ''):
            messages.info(request, "first name, email or password cant be empty !")
            return redirect('register')
        else:
            user = User.objects.create_user(username=fname, email=email, password=password)
            user.save()
            return redirect('login')
    return render(request, 'registration.html')


    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password =password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Type correct password and username!")
            return redirect('login')

    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def results(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user = request.user)

        return render(request, 'results.html', {'profile':profile})
    else:
        return render(request, 'login.html')





    
    

    