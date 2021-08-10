# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import ChatData

def index_home(request):
    chatData = ChatData.objects.filter()
    print(chatData)
    return render(request, 'frontend/home.html', {'chat': chatData})

def keyword(request):
    return render(request, 'keyword/keyword.html')