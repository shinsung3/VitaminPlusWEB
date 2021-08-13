# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import ChatData

def index_home(request):
    chatData = ChatData.objects.filter()
    keys = []
    for i in range(121):
        keys.append(str(i))
    # print(keys)

    timeLine = dict.fromkeys(keys, 0)
    for i in chatData:
        liveTime = i.liveTime.split(":")
        if len(liveTime) >2:
            key = str(int(liveTime[0])*60 + int(liveTime[1]))
            value = timeLine.get(key)+1
            timeLine.update({key : value})
        else:
            value = timeLine.get(liveTime[0])+1
            key = liveTime[0]
            timeLine.update({key : value})
    # print(timeLine)
    timeLine = sorted(timeLine.items())

    return render(request, 'frontend/home.html', {'chat': chatData, 'timeLine':timeLine})

def keyword(request):
    return render(request, 'keyword/keyword.html')

def emotion(request):
    return render(request, 'frontend/emotion.html')

def timeline(request):
    chatData = ChatData.objects.filter()
    chat = []
    keys = []
    for i in range(121):
        keys.append(str(i))
    # print(keys)

    timeLine = dict.fromkeys(keys, 0)
    for i in chatData:
        liveTime = i.liveTime.split(":")
        if len(liveTime) >2:
            key = str(int(liveTime[0])*60 + int(liveTime[1]))
            value = timeLine.get(key)+1
            timeLine.update({key : value})
            # chat.append(key)
            chat.append(i.liveTime)
            chat.append(i.chat)
        else:
            value = timeLine.get(liveTime[0])+1
            key = liveTime[0]
            timeLine.update({key : value})
            # chat.append(key)
            chat.append(i.liveTime)
            chat.append(i.chat)
    # print(timeLine)
    timeLine = sorted(timeLine.items())

    return render(request, 'frontend/timeline.html', {'chat': chat, 'timeLine':timeLine})