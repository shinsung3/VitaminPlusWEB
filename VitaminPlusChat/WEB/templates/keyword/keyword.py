import numpy as np
import pandas as pd
import os
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import sys
from konlpy import Okt
from collections import Counter
import warnings

#엑셀 불러오기
base_dir = 'VitaminPlusChat/static/excel'
excel_file = 'excel.xlsx'
excel_dir = os.path.join(base_dir, excel_file)

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df_from_excel = pd.read_excel(excel_dir,
                                sheet_name = 'chatting list',
                                header = 0,
                                dtype = {'second':str,
                                       'reg_dt':str,
                                       'message_type':str,
                                       'message':str,
                                       'user_cd':str,
                                       'user_group':str,
                                       'user_id':str,
                                       'user_nm':str,
                                       'user_nicknm':str,
                                       'user_phonenumber':str},
                                index_col = 'index',
                                na_values = 'NaN',
                                thousands='',
                                nrows = 668,
                                comment = '#',
                                engine="openpyxl")


m_list = list(df_from_excel['이벤트 타입'])
text = " ".join(m_list)

#명사 추출
okt = Okt()
noun = okt.nouns(text)

for i,v in enumerate(noun):
       if len(v) < 2:
              noun.pop(i)

count = Counter(noun)
noun_list = count.most_common(100)

#wordcloud 그리기
clothes_coloring = np.array(Image.open('VitaminPlusChat/static/img/clothes.png'))
image_colors = ImageColorGenerator(clothes_coloring)

font_path = 'C:/Windows/Fonts/H2GTRM.ttf'
#wordcloud = WordCloud(font_path=font_path, background_color='white').generate(text)
wordcloud = WordCloud(font_path=font_path, background_color='white',max_font_size=100, mask=clothes_coloring)
wordcloud.generate_from_frequencies(dict(noun_list))
wordcloud.recolor(color_func=image_colors)
wordcloud.to_file('VitaminPlusChat/static/img/wordcloud.png')

fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()