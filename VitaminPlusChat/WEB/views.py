# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render


def index_home(request):
    return render(request, 'frontend/index.html')