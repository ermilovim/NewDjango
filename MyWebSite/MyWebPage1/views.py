from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# Create your views here.

def index(request):
    return render_to_response("mywebpage1/main.html")