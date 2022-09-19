import re

import gensim
import jieba


def Symbol_filter(str):
    # 使用正则表达式过滤标点符号
    result = re.sub('\W+', '', str).replace("_", '')
    return result
def get_content (path):
    # 文本处理，将我们的文本处理为字符串，并且过滤掉标点符号
    string = ''
    file = open(path, 'r', encoding='UTF-8')
    one_line = file.readline()
    while one_line:
        string += one_line
        one_line = file.readline()
    # 调用标点符号过滤函数
    string = Symbol_filter(string)
    file.close()
    return string



