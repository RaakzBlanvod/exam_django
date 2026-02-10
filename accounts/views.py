from django.shortcuts import render

# Create your views here.
def profile_view (request):
    return render(request, './profile.html', {})

def login_view (request):
    return render(request, './login.html', {})

def logout_view (request):
    return render(request, '', {})

def registration_view (request):
    return render(request, './registration.html', {})

def basket_view (request):
    return render(request, './basket.html', {})

def main_view (request):
    return render(request, './main.html', {})