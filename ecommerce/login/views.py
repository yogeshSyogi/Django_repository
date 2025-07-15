from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def login(request):
#     return HttpResponse("You're at sevices page.")

def login(request):
    return render(request, 'login.html',{})