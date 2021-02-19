import pandas as pd
import re
import jieba
import stylecloud
from IPython.display import Image

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)


def filter_str(desstr, restr=''):
    # 过滤除中文以外的其他字符
    res = re.compile("[^\u4e00-\u9fa5^,^，^.^。^【^】^（^）^(^)^“^”^-^！^!^？^?^]")
    return res.sub(restr, desstr)


def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("data/stopwords.txt", 'r', encoding='GBK') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    # 添加关键词
    my_words = []
    for i in my_words:
        jieba.add_word(i)

        # 自定义停用词
    my_stop_words = []
    stop_words.extend(my_stop_words)

    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)
    # print(word_num)
    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2]
    print(word_num_selected)
    return word_num_selected


data = pd.read_csv('data/maoyan.csv').astype(str)

data['Content'] = data['Content'].apply(filter_str)
# print(data.head())

text1 = get_cut_words(content_series=data['Content'])

stylecloud.gen_stylecloud(text=' '.join(text1), collocations=False,
                          # palette='cartocolors.qualitative.Pastel_5',
                          font_path=r'‪C:\Windows\Fonts\msyh.ttc',
                          # icon_name='fas fa-dragon',
                          # icon_name='fas fa-cat',
                          icon_name='fas fa-dove',
                          size=400,
                          output_name='电影词云.png')
Image(filename='电影词云.png')
