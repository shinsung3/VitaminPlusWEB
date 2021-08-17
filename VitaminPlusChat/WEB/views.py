# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .templates.keyword.wordranking import make_top_word_graph
from .models import ChatData, KeywordData

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
    wordList = make_top_word_graph('Okt0.txt', 5)

    return render(request, 'keyword/keyword.html', {'word': wordList})

def emotion(request):
    emotion = ["슬리피", "자켓", "미진", "블루", "방송", "모델", "대박", "핏", "착용", "모자"]
    value = [79, 45, 37,37,31,31,30,30,29,27]
    bad = ["박재범", "끝", "개"]
    good = ["라이브", "진짜", "쿠폰", "오", "로열"]
    print(emotion)
    print(value)
    return render(request, 'frontend/emotion.html', {"emotion":emotion, "value":value, "bad":bad, "good":good})

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