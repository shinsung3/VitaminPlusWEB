import numpy as np
import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import warnings

fileSet = [['TommyJeans_2021_Test_data_2.xlsx',1117],['TommyJeans_2021_Test_data_3.xlsx',536],['RA_2021_Test_data_4.xlsx',1217]]

for i in range(3):
#엑셀 불러오기
    # base_dir = 'VitaminPlusChat/static/excel'
    excel_file = fileSet[i][0]
    print(excel_file)
    # excel_dir = os.path.join(base_dir, excel_file)

    with warnings.catch_warnings(record=True): 
        warnings.simplefilter("always")
        df_from_excel = pd.read_excel(excel_file,
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
                                nrows = fileSet[i][1],
                                comment = '#',
                                engine="openpyxl")


    m_list = list(df_from_excel['chat'])
    text = " ".join(m_list)
    print(text)

    #명사 추출
    okt = Okt()
    noun = okt.nouns(text)

    for i,v in enumerate(noun):
        if len(v) < 2:
              noun.pop(i)

    count = Counter(noun)
    noun_list = count.most_common(100)

    f = open('Okt'+str(i)+'.txt', 'w',encoding='UTF-8')
    f.write(noun_list)
    f.close()