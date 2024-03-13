from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

def calculate(request):
    return HttpResponse("ben çalıştım")
