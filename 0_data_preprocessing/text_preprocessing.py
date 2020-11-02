# -*- encoding: utf-8 -*-
'''
@File    :   text_preprocessing.py
@Time    :   2020/10/27 22:34:47
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''
# here put the import lib

import jieba
from zhon import hanzi
from zhon import pinyin
from sys import path as syspath
from os.path import expanduser
from os import sep
# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
syspath.append(project)
from determine_character_type import is_chinese,is_number,is_alphabet,is_other
from file_tools import ml_model_dir, search_moduel_dir, data_preprocessing_dir, python_functional_script_dir, bash_functional_script_dir, data_structure_dir, question_data_dir, math_module_dir,info_table
syspath.append(data_structure_dir)
from data_structure import deeping_flatten
import warnings
warnings.filterwarnings("ignore")



'''加载标准停用词（标点符号）'''
base_stopwords = list(hanzi.stops)+list(hanzi.non_stops)+list(pinyin.stops)+list(pinyin.non_stops)

def split_character_type(original):
    '''
    不同字符类型分割
    '''
    make = [0]
    diff = []
    n = 0
    temp = ""
    for char in original:
        if is_chinese(char):
            n = 0
        elif is_number(char):
            n = 1
        elif is_alphabet(char):
            n = 2
        elif is_other(char):
            n = 3
        else:
            n = 4
        make.append(n)
        if (make[-1]-make[-2]) == 0:
            diff.append(char)
        else:
            diff.append("|")
            diff.append(char)      
    return "".join(diff).split("|")

#TODO 分词过滤转换

def split_words_from_chinese_func(original):
    '''
    中文分词
    '''
    return list(jieba.cut(context_func(split_character_type(original))))

def word_punct_tokenizer_for_chinese(article_list,clear_data=False):
    '''
    对文章列表分词(中文优先)
    '''
    m =len(article_list)
    if clear_data:
        return {paper_num:filter_stop_words(split_words_from_chinese_func(paper)) for paper,paper_num in zip(article_list,range(m))}
    return {paper_num:split_words_from_chinese_func(paper) for paper,paper_num in zip(article_list,range(m))}

def split_words_from_english_func(original):
    '''
    英文空格分词
    '''
    return deeping_flatten((strings.split("|") for strings in split_character_type(original).split()))

def filter_stop_words(words_list,stop_words_dict = base_stopwords):
    '''
    过滤停用词
    '''
    return [word for word in words_list if word not in stop_words_dict ]

def case_conversion(msg,key=None):
    '''
    英文转换 
    key : 选择转换方式
    '''
    if key==None:
        return None
    return {"upper":msg.upper()  #upper()函数，将所有字母都转换成大写
        ,"lower":msg.lower()  #lower()函数，将所有字母都转换成小写
        ,"capitalize":msg.capitalize()  #capitalize()函数，将首字母都转换成大写，其余小写
        ,"title":msg.title()}[key] # 所有分隔英文单词首字母大写
    
def context_func(paper_list):
    '''
    连接上下文
    '''
    return "".join(paper_list)



if __name__ == "__main__":
    instructions_text=  ['扫描本机所在网段上有哪些主机是存活的',
    '端口扫描：输入目标主机ip，扫描某台主机开放了哪些端口',
    '隐藏扫描，输入目标主机ip，只在目标主机上留下很少的日志信息',
    'UDP端口扫描：输入目标主机ip，扫描目标主机开放了哪些UDP端口',
    '操作系统识别：输入目标主机ip，查询是哪个系统',
    '上传或者同步大型项目文件到服务器',
    '检查本机网段内ip',
    '查看本机网段内 激活/在线 的设备',
    '查询本地公网ip',
    '上传《网络工具》项目到GPU服务器',
    '上传《网络工具》项目到华为服务器',
    '查询系统运行时间',
    '查询系统开机时间',
    '查询系统历史启动时间',
    '存储盘的位置',
    '酒店开房数据集的位置']
    print(word_punct_tokenizer_for_chinese(instructions_text))