from konlpy.tag import Okt
okt = Okt()
print(okt.pos(u'이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요'))

# import platform
# print(platform.architecture())

# import sys
# print(sys.version)

# from konlpy import init_jvm
# print(init_jvm("<JAVA_HOME>"))

# from konlpy.tag import Kkma
# from konlpy.utils import pprint

# kkma = Kkma()

# pprint(kkma.nouns(u'드디어 오류 없이 잘 실행됩니다. 오늘은 여기까지 안녕'))
# >>> ['오류', '실행', '오늘', '여기', '안녕']

# from konlpy.tag import Kkma
# print(Kkma().pos('설치여부확인법'))