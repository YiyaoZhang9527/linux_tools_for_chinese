# -*- encoding: utf-8 -*-
'''
@File    :   onehot_encoding.py
@Time    :   2020/10/28 13:55:07
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib
import sys
from os import sep
from os.path import expanduser

# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
sys.path.append(project)
# 加载各模块位置
from file_tools import data_preprocessing_dir, data_structure_dir, math_module_dir

# 加载数据预处理模块
sys.path.append(data_preprocessing_dir)
from text_preprocessing import word_punct_tokenizer_for_chinese

# 加载数学模块
sys.path.append(math_module_dir)
from statistics_module import frequency
from numpy import ones, array,zeros
from pandas import DataFrame
sys.path.append(data_structure_dir)
from data_structure import deeping_flatten 

def character_encoding(data,clear_data=False):
    '''
    对文本列表特征编码
    '''
    split_words_from_chinese = word_punct_tokenizer_for_chinese(data,clear_data) #分词每段文章
    flatten_ = deeping_flatten((word for num,word in split_words_from_chinese.items())) # 将所有文章单词列表展开到一纬
    total_number_of_words = len(flatten_) #所有文章单词的数量的总和
    distances,counter = frequency(flatten_,return_type="tuple") #求每个单词在所有文章中出现的频率
    feature_dictionary_editor = {key:value for key,value in zip(distances,counter/total_number_of_words)}

    distance_lenght = counter.size #去重侯单词的数量
    counter_coding = []#zeros((distance_lenght,distance_lenght))
    one_vector = ones(distance_lenght) #全是1的向量
    onehot_matrix_for_each_article = dict() #初始化返回列表
    
    time_leve0 = -1
    counter_word = 0 # 初始化单词计数
    word_list = set()
    for No,words in split_words_from_chinese.items():
        time_leve0 += 1
        time_leve1 = -1
        init_onehot_mat = zeros((distance_lenght,distance_lenght)) #单文onehot矩阵 
        for word in words: #循环计算所有单词
            time_leve1 += 1
            init_onehot_dictionary = {key:value for key,value in zip(distances,zeros(distance_lenght))} #初始化onehot字典   
            init_onehot_dictionary[word]=1 #将对应单词的字典编码改为1
            init_onehot_vector = array([one_hot_code for word_leve1,one_hot_code in init_onehot_dictionary.items()]) #整理每个单词的onehot字典成为onehot向量
            init_onehot_mat[time_leve1]=init_onehot_vector #将每篇文章的onehot矩阵对应的单词行修改为当前循环单词的onehot向量
            word_list.add(word)
        counter_word += init_onehot_mat.sum() #计算每篇文章单词数 
        onehot_matrix_for_each_article.update({No:init_onehot_mat}) #将每篇文章的onehot向量于文章序号对应保存为dict结构
        counter_coding.append(init_onehot_mat.T.dot(one_vector)) # 计算每篇文章词向量
    counter_coding=array(counter_coding) # 将每一行的对应单词计数转为矩阵表达
    return {"单文章onehot矩阵":onehot_matrix_for_each_article
        ,"每篇文章出现的单词词频":DataFrame(counter_coding,columns=distances)
        ,"每篇文章出现的单词特征概率":DataFrame(counter_coding/total_number_of_words,columns=distances)
        ,"单词列表":word_list
        ,"概率特征字典":feature_dictionary_editor
        ,"概率特征向量":array([value for key,value in feature_dictionary_editor.items()])
        ,"总字数":counter_word==total_number_of_words and counter_word or "字数不符"}

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
    article_list=instructions_text
    print(character_encoding(article_list))

