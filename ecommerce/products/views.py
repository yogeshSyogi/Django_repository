from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def products(request):
#     return HttpResponse("You're at sevices page.")

def products(request):
    return render(request, 'products.html',{})