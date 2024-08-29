# 词云图  使用Python第三方库jieba和wordcloud实现对华为笔记本评论的词云图
import jieba
from wordcloud import WordCloud

# 读取数据
with open('command.txt','r',encoding='utf-8') as file:
    s=file.read()

# 中文分词
lst=jieba.lcut(s)
# 排除词
stopword=['解决方案','服务态度','解决方案']

txt=''.join(lst)

# 绘制词云图

wc=WordCloud(background_color='white',font_path='PingFang.ttc',stopwords=stopword,width=800,height=600)

# 由txt生成词云图

wc.generate(txt)

# 保存图片

wc.to_file('command2.png')
