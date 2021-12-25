from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def customer(request):
    return render(request,'accounts/customer.html')


def profile(request):
    return render(request,'accounts/profile.html')