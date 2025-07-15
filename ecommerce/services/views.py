from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def services(request):
#     return HttpResponse("You're at sevices page.")

def services(request):
    return render(request, 'services.html',{})