from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("You're at sevices page.")

def home(request):
    return render(request, 'home.html',{})