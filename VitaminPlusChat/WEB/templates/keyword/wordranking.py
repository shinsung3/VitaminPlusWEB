import nltk

# make noun frequency graph per religion
def make_top_word_graph( filename, top ):
    # result_path = '/result/top-word/'
    filename = 'WEB/templates/keyword/Okt0.txt'
    # filename = 'Okt0.txt'
    file=open(filename,'r',encoding='UTF-8')
    result = file.read()
    tokens = result.split(" ") # 문자열을 공백 기준으로 구분
    text = nltk.Text(tokens) # nltk 
    topWord = text.vocab().most_common(top) # top n word
    topWord = [a[0] for a in topWord[:5 ]]

    return topWord


if __name__=="__main__":
    make_top_word_graph("",5)