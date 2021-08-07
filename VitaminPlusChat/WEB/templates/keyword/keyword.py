import numpy as np
import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import warnings

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

#print(df_from_excel.loc[:,['이벤트 타입','유저 그룹']])

#print(df_from_excel.loc['이벤트 타입'])

m_list = list(df_from_excel['이벤트 타입'])
text = " ".join(m_list)
#print(text)

font_path = 'C:/Windows/Fonts/H2GTRM.ttf'
#wordcloud = WordCloud(font_path=font_path, background_color='white').generate(text)
wordcloud = WordCloud(font_path=font_path, background_color='#4395e0').generate(text)
wordcloud.to_file('VitaminPlusChat/static/img/wordcloud.png')

#fig = plt.figure(figsize=(12,12))
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()