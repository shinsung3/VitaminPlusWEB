import numpy as np
import pandas as pd
import os
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import sys
# from konlpy import Okt
# from collections import Counter
import warnings

#엑셀 불러오기
base_dir = 'VitaminPlusChat/static/excel'
excel_file = 'RA_2021_Test_data_4.xlsx'
excel_dir = os.path.join(base_dir, excel_file)

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df_from_excel = pd.read_excel(excel_dir,
                                sheet_name = 'chatting list',
                                header = 0,
                                dtype = {'index':str,
                                       'liveTime':str,
                                       'time':str,
                                       'memberDiff':str,
                                       'chat':str,
                                       'userCode':str,
                                       'userGroup':str,
                                       'userId':str,
                                       'userName':str,
                                       'userNick':str,
                                       'phone':str},
                                index_col = 'index',
                                na_values = 'NaN',
                                thousands='',
                                nrows = 1217,
                                comment = '#',
                                engine="openpyxl")


m_list = list(df_from_excel['chat'])
# print(m_list)
text = " ".join(m_list)

# #명사 추출
# okt = Okt()
# noun = okt.nouns(text)

# for i,v in enumerate(noun):
#        if len(v) < 2:
#               noun.pop(i)

# count = Counter(noun)
# noun_list = count.most_common(100)

stopwords = {'ㅋ','은','는','입니다','너무','오','와우','ㅠㅠ','헐','슬리피님','슬리피',
'대박','라이브','방송','엠디님','박재범','가능합니다','착용하신','와',
'ㅋㅋㅋㅋㅋ','ㅋㅋㅋㅋㅋㅋㅋㅋㅋ','ㅋㅋㅋㅋ','ㅋㅋㅋㅋㅋㅋ','모델분','진짜','우왕','넘','더','ㅋㅋㅋ',
'현정님','것 같아요','잘','완전','와ㅏㅏㅏㅏ','ㅎㅎㅎ','또','아','ㅜㅜ','어머'}

# stopwords = {}

#wordcloud 그리기
clothes_coloring = np.array(Image.open('VitaminPlusChat/static/img/clothes3.png'))
image_colors = ImageColorGenerator(clothes_coloring)

font_path = 'C:/Windows/Fonts/H2GTRM.ttf'
#wordcloud = WordCloud(font_path=font_path, background_color='white').generate(text)
wordcloud = WordCloud(font_path=font_path, background_color='white',max_font_size=300, mask=clothes_coloring,stopwords=stopwords).generate(text)
# wordcloud.generate_from_frequencies(dict(noun_list))
wordcloud.recolor(color_func=image_colors)
wordcloud.to_file('VitaminPlusChat/static/img/wordcloud_3.png')



wordcloud = WordCloud(font_path=font_path, background_color='#FFD85B',max_font_size=300, mask=clothes_coloring,stopwords=stopwords).generate(text)
wordcloud.recolor(color_func=image_colors)
wordcloud.to_file('VitaminPlusChat/static/img/keyword_3.png')

fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()