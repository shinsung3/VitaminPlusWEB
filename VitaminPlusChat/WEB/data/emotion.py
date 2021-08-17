# from konlpy.tag import Okt
# from konlpy import jvm

# jvm.init_jvm()
# okt = Okt()
# print(okt.pos(u'이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요'))

# from konlpy.tag import Hannanum
# hannanum = Hannanum()

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

# from konlpy.tag import Hannanum
# hannanum = Hannanum()
# print(hannanum.analyze('롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
# print(hannanum.morphs('롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
# print(hannanum.nouns('다람쥐 헌 쳇바퀴에 타고파'))
# print(hannanum.pos('웃으면 더 행복합니다!'))


# from typing import Counter
import pandas as pd
# import numpy as np
from konlpy.tag import Okt
from collections import Counter
import csv
# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer(min_df=1)
# import matplotlib.pyplot as plt
# import seaborn as sns

# import warnings
# warnings.filterwarnings('ignore')
okt = Okt()
chat = pd.read_excel("./TommyJeans_2021_Test_data_2.xlsx", usecols="E")
mylist = chat['chat'].to_string()
# print(mylist)
content = okt.nouns(mylist)
# print(content)
count = Counter(content)
arr = [("list", "value")]
for i in count.most_common(100):
    arr.append(i)
print(arr)

with open('List_csv4.xlsx','w', newline='', encoding='utf-8-sig') as file :
    write = csv.writer(file)

    for data in arr:
        write.writerow(data)

# df = pd.DataFrame(count)
# print(df)
# print(count)
# count = []
# for a in mylist:
    # count += Counter(content)
    # print(count)
# noun = okt.nouns(mylist)
# count = Counter(noun)

# noun_list = count.most_common(100)
# for v in noun_list:
#     print(v)
# for a in mylist:
    # count