from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Resgistration succesdull, Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})
            
    return render(request, 'register.html')

def login_view(request):
    if request.method =='POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {"eror": "Invalid credentials. Please try again"})
        
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})
    
    
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def joinroom(request):
    if request.method =='POST':
        roomID = request.POST['roomID']
        return redirect('/meeting?roomID=' +roomID)
    return render(request, 'joinroom.html', {'name': request.user.first_name + " " + request.user.last_name})