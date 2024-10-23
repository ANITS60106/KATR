from django.shortcuts import render

def index(request):
<<<<<<< HEAD
    return render(request, 'web/index.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def home(request):
    return render(request, 'users/home.html')
=======
    return render(request, 'web/index.html')
>>>>>>> 1b6ad91097e8102e128dce4a5b3b8c78c03332c0
