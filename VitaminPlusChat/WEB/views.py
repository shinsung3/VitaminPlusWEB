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
    chat1 = ["3:20 노랑자켓 이뻐요",
             "8:21 노랑 자켓 내가 찍얶던건데",
             "15:13 저자켓이뿌네요ㅠㅠ",
             "16:22 자켓이뻐요 인스타에서밧는데!!!!!",
              "18:45 얼마에요 자켓???",
              "20:41 오빠자켓편해요???남자칭구사주구싶넹",
              "23:09 노란자켓 사이즈 슬리피가 입은게 xl인가요",
              "23:37 슬리피 자켓사이즈 무엇?",
              "31:17 노란자켓 다른색상도 입어봐주믄 좋겠어요",
              "32:54 슬리피님 얼굴 자켓 바지 볼매",
              "33:06 카키색 자켓 보고프다",
              "37:31 헐 자켓체크무엇",
              "37:55 아 코치자켓",
              "37:57 자켓너무이쀼댜이이이",
              "38:39 코치자켓 색상 어떻게있을까요?????",
              "39:08 리버서블자켓 색상궁금해요!!",
              "41:56 여자도자켓어울리나요",
              "44:57 저자켓도 여자가입을수잇나요?입어봐주세요",
              "46:22 여자모델이입어주세요 자켓",
              "49:30 엠디님 키몇이세요????이뿌다 자켓",
              "56:41 셔켓 셔츠와 자켓 합성어",
              "1:10:33 슬리피형님 첫 자켓"]
    chat2 = ["35:33 블루 예뻐요 진이랑 어울",
              "36:20 로열블루",
              "36:26 로열블루",
              "36:26 로열블루",
              "36:26 레드 화이트 블루",
              "36:28 레드 화이트 블루",
              "36:28 로열블루",
              "36:29 로열블루",
              "36:30 로열블루",
              "36:32 로열블루",
              "36:32 레드 화이트 블루",
              "36:32 레드 화이트 블루",
              "36:33 로열블루",
              "36:33 로열블루",
              "36:35 로열블루",
              "36:36 로열블루",
              "36:44 로열블루",
              "36:47 로열블루",
              "38:53 로열블루♡♡"]
    chat3 = ["8:25 완죤 기다리던 방송이에여! 슬리피님 진행이라니 완전 찰떡이네용",
              "14:53 이런 방송참여 처음 입니다. ㅋ",
              "29:50 지금 엠디님 입고계시는 바지는 방송판매상품아닌가용?",
              "35:21 재밌어 이방송ㅋㅋㅋㅋ 두분 센스가 좋으시네 몰랐는데 슬리피님 옷빨 잘받는듯",
              "37:51 방송 부탁합니다",
              "40:02 이 방송 재밌엉ㅋㅋㅋㅋㅋ",
              "43:36 방송 재있어요",
              "43:51 방송 또 해주세요",
              "44:03 다음 방송에 슬리피 또 나오나요",
              "1:12:44 사적방송 보고싶을정도로 잘하심",
              "1:14:08 칭구들한테 오늘 방송 혜택 알릴게용"]
    chat4 = ["15:48 모델??",
              "16:11 아역시 슬모델 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ",
              "16:36 모델ㅋ",
              "16:39 명품비율 슬모델!",
              "30:07 와 모델인줄",
              "33:07 MD분 모델 같아요",
              "34:31 모델님도 모자한벋써주세여 ",
              "37:16 모델분ㅋㅋㅋ",
              "42:21 여자모델은없나요오늘?",
              "45:31 여자모델이입은거보고싶어요",
              "45:54 모델분 셔츠 사이즈 알려주세요 !!",
              "46:22 여자모델이입어주세요 자켓",
              "47:44 엠디님 모델핏",
              "56:42 이모델 대박인듯",
              "1:09:31 피쉬테일에 후드가 없는 모델"]
    chat5 = ["11:49 모자 넘 예뻐요 ",
              "11:54 모자 이쁘네요!!",
              "11:58 모자갖고싶다 ㅠㅠ",
              "15:12 저멀리 모자사은품 내가 보고있다",
              "16:06 모자  모자 ㅋㅋㅋ 커커커 컴온!!  ",
              "23:15 모자갖고싶다아 ㅠㅠ",
              "29:03 모자 예뿌당",
              "29:05 모자이쁘다 헐",
              "34:31 모델님도 모자한벋써주세여 ",
              "36:47 모자이쁘다",
              "39:11 모자도 한 번 써봐주세요 ",
              "58:10 도라에몽 슈타일 모자당",
              "1:00:28 대나무헬리콥터 달고픈 모자에옄ㅋㅋ",
              "1:04:20 사은품모자는 핏 못보나여 ㅠㅠ",
              "1:05:28 사은품모자핏보고시퍼여 ㅠㅠ",
              "1:06:04 모자쓰니 잘생겨보여요"]

    return render(request, 'keyword/keyword.html', {'word': wordList, 'chat1':chat1, 'chat2':chat1, 'chat3':chat1, 'chat4':chat1, 'chat5':chat1})

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