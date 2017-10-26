#encoding=utf-8
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
text_from_file=open('data.txt','r').read()
Word_spilt_jieba = jieba.cut(text_from_file,cut_all = False)
word_space = ' '.join(Word_spilt_jieba)
img=imread('bipt.jpg')
img = np.array(Image.open('bipt.jpg'))
my_wordcloud = WordCloud(
    background_color='white', #设置背景颜色
    mask=img,  #背景图片
    max_words = 200, #设置最大显示的词数
    stopwords = STOPWORDS, #设置停用词
    #设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载会出现问题。
    font_path = 'simkai.ttf', 
    max_font_size = 100, #设置字体最大值
    random_state=50, #设置随机生成状态，即多少种配色方案
    ).generate(word_space)
iamge_colors = ImageColorGenerator(img)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
my_wordcloud.to_file('res.jpg')
