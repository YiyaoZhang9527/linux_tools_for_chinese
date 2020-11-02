# -*- encoding: utf-8 -*-
'''
@File    :   extract.py
@Time    :   2020/10/27 22:34:37
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib

import re
from zhon import hanzi
from zhon import pinyin

'''加载标准停用词（标点符号）'''
base_stopwords = list(hanzi.stops)+list(hanzi.non_stops)+list(pinyin.stops)+list(pinyin.non_stops)

#TODO 正则提取1.0 即将清理

def extract_english(original):
    '''
    只要英文
    '''
    return re.findall(r'[a-zA-Z]+', original)

def extract_chinese(original):
    '''
    只要中文
    '''
    return re.findall(u'[\u4e00-\u9fa5]',original)

def extract_numbers(original):
    '''
    只要数字
    '''
    return re.findall(r'\d+',original)

def temp_extract(strings,symbles=base_stopwords):
    '''
    临时删除
    '''
    srcrep = {i:'' for i in symbles }
    rep = dict((re.escape(k), v) for k, v in srcrep.items())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], strings)

#TODO 未来的版本中将使用以下正则函数

def extract_english_function(original):
    """
    '提取中文'
    """
    return re.findall(r'[a-zA-Z]+', original)

def extract_number_function(original):
    """
    '提取数字'
    """
    return re.findall(r'\d+',original)

def extract_chinese_function(original):
    """
    '提取英文'
    """
    return re.findall(u'[\u4e00-\u9fa5]',original)

def extract_segment_functions(strings,symbol_to_delete=base_stopwords):
    """
    '提取其他'
    """
    srcrep = {i:'' for i in symbol_to_delete}
    rep = dict((re.escape(k), v) for k, v in srcrep.items())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], strings)

if __name__ == "__main__":
    s = "Hello world , world you takes same words for me "
    sym = "word","world","wor"
    #print(extract_segment_functions(s,sym))
    print(base_stopwords)
    print(extract_segment_functions(s,sym))


