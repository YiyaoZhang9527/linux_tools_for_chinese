# -*- encoding: utf-8 -*-
'''
@File    :   feature_dictionary_editor.py
@Time    :   2020/10/28 14:25:03
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib
import sys
from os.path import expanduser
from os import sep
# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
sys.path.append(project)
# 加载各模块位置
from file_tools import ml_model_dir, search_moduel_dir, data_preprocessing_dir, python_functional_script_dir, bash_functional_script_dir, data_structure_dir, question_data_dir, math_module_dir,info_table
# 加载数据预处理模块
sys.path.append(data_preprocessing_dir)
from text_preprocessing import split_words_from_chinese_func,word_punct_tokenizer_for_chinese,filter_stop_words
# 加载数学模块
sys.path.append(math_module_dir)
from statistics_module import probaitily,frequency
from numpy import dot,ones_like,ones,zeros_like,array,zeros
from pandas import DataFrame

def feature_dictionary_editor(article_list,optimization_=False):
    '''
    特征字典编辑器
    '''
    all_words = filter_stop_words(split_words_from_chinese_func(article_list))
    return probaitily(all_words,return_type='dict',optimization=optimization_)

'''
def creater_of_feature_vector(article_list):
    #对文章列队创建全局特征字典
    # 构建特征字典
    split_words_for_acticles = filter_stop_words(split_words_from_chinese_func(article_list)) #分词并过滤停用词 
    distances , counter = frequency(split_words_for_acticles,return_type="tuple")
    the_total_number_of_words = counter.dot(ones_like(counter)) #总单词数量

    feature_dictionary = dict(zip(distances,counter/the_total_number_of_words)) #特征字典

    split_words_for_acticle = word_punct_tokenizer_for_chinese(article_list)#对所有文章分词，并保持篇幅

    lenght_of_feature_dictionary = len(feature_dictionary) #计算全部单词数量

    # 构造单文特征向量
    m , n = len(article_list),counter.size
    init_feature_mat = zeros((m,n))
    print(init_feature_mat.shape)
    time = -1
    for NO,row in split_words_for_acticle.items():
        time += 1
        distances_of_row , counter_for_row = frequency(row,return_type='tuple')
        init_feature_vector_of_one_row = dict(zip(distances,zeros(n))) #单文特征字典初始化
        #print(len(init_feature_vector_of_one_row))
        for word , prob in zip(distances_of_row,counter_for_row/lenght_of_feature_dictionary):
            init_feature_vector_of_one_row[word]=prob
        feature_vector = array([prob for word,prob in init_feature_vector_of_one_row.items()]) #字典转向量
        print(feature_vector.shape)
        init_feature_mat[time] = feature_vector
    table = DataFrame(init_feature_mat,columns=distances)
    return {"特征字典":feature_dictionary,"文章分词列表":split_words_for_acticle ,"特征矩阵":init_feature_mat,"文章词特征向量表":table}
'''

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
    print(feature_dictionary_editor(instructions_text))