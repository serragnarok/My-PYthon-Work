# -*- coding: UTF-8 -*-
import requests #連接網址套件
from bs4 import BeautifulSoup #爬蟲套件
import jieba #斷詞
import matplotlib.pyplot as plt #畫圖
from wordcloud import WordCloud, ImageColorGenerator #文字雲套件
import re #正規表達式套件
freq = {}
stop = ["的","了","好", "也", "再", "有", "與", "後", "記者", "報導", "是", "說", "會", "為", "以", "例", "都", "在", "就", "於", "及", "長", "對", "不", "讓", "被", "或", "第", "但", "到", "要", "表示", "以", "等", "和", "個"]

for i in range(5):
    url = requests.get("https://news.ltn.com.tw/search/?keyword=%E9%9F%93%E5%9C%8B%E7%91%9C&conditions=and&SYear=2019&SMonth=7&SDay=1&EYear=2019&EMonth=9&EDay=30&page=" + str(i+1))
    soup = BeautifulSoup(url.text, 'html.parser')
    t = soup.find_all("a" ,class_="tit") 
    print(i)
    for _ in t:
        article = requests.get("http://news.ltn.com.tw/" + _.get("href"))
        ap = BeautifulSoup(article.text, 'html.parser')
        txt = ap.select('div.text > p')
        for q in txt:
            words = jieba.cut(str(q), cut_all=False)
            words = [word for word in words if word not in stop]
            for word in words:
                word = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\"\'\／\。\〕\〔\」\一\）\（\］\「\︶\？\’\ˊ\ˋ\、\`\‵\，\；\%\％內容頁點我載點]", "", word)
                if word in freq:
                    freq[word] = freq[word] + 1
                else:
                    freq[word] = float(1)
        for fr in freq:
            if fr == 1:
                del fr

print(freq)

wc = WordCloud(background_color="white",width=1000, height=860, margin=2,font_path ="C:\Windows\Fonts\kaiu.ttf")
wc.generate_from_frequencies(freq)
plt.figure()

plt.imshow(wc)
plt.axis("off")
plt.show()


    



    

