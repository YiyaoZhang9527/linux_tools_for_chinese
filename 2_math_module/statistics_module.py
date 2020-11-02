# -*- encoding: utf-8 -*-
'''
@File    :   statistical.py
@Time    :   2020/10/28 00:24:33
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib
import numpy as np
from sys import path as syspath
from os.path import expanduser
from os import sep
# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
syspath.append(project)
from file_tools import ml_model_dir, search_moduel_dir, data_preprocessing_dir, python_functional_script_dir, bash_functional_script_dir, data_structure_dir, question_data_dir, math_module_dir,info_table
syspath.append(data_structure_dir)
from data_structure import check_ndarray

def sort_by_dictionary_value(dictionary):
    '''
    按字典值排序
    '''
    return sorted(dictionary.items(), key=lambda d:d[1], reverse = True)

def probability_optimization(prob,optimization=False):
    '''
    概率表达方式优化模块
    '''
    if optimization==False:
        prob = prob
    elif optimization == 'log':
        prob = np.log(prob)
    elif optimization == '-log':
        prob = -np.log(prob)    
    return prob

def return_type_func(sorted_data,return_type):
    '''
    选择返回的数据结构
    '''
    if return_type == "dict":
        return dict(zip(sorted_data[:,0],sorted_data[:,-1].astype(float)))
    if return_type == 'tuple':
        return sorted_data[:,0],sorted_data[:,-1].astype(float)
    return sorted_data

    
def frequency(data,return_type="dict"):
    '''
    频率计算并排序
    '''
    init_data = check_ndarray(data)
    unique,counter = np.unique(init_data,return_counts=True)
    sorted_ = np.array(sort_by_dictionary_value(dict(zip(unique,counter))))
    return return_type_func(sorted_,return_type)

def probaitily(x,return_type="dict",optimization=False):
    '''
    概率计算
    '''
    init_x = check_ndarray(x)
    lenght = init_x.size
    elements,counter= np.unique(init_x,return_counts=True)
    prob = counter/lenght
    sorted_ = sorted_ = np.array(sort_by_dictionary_value(dict(zip(elements,probability_optimization(prob,optimization)))))
    return return_type_func(sorted_,return_type)

def sigmoid(x):
    '''sigmoid函数'''
    return 1/(1+np.exp(x*-1))


if __name__ == "__main__":
    case = np.array(['查询', 'GPU', '或者', '检查', '时间', '存储', '文件', '开房',  '检查', '时间', '存储', '文件', '开房','扫描', '目标',
       '网络工具', '是', '内', '上', '输入', '，', '了', '信息', '数据', '哪些', '运行',
       'UDP', '设备', '识别', '端口', '留下', ' ', '集', '本', '日志', '哪个', '到',
       '酒店', '在线', '项目', '系统', '查看', '/', '历史', '机', '的', '网段', '》',
       '端口扫描', '在', '服务器', '很少', '隐藏', '激活', '启动', '某台', '存活', '有',
       '大型项目', '：', '本地', '公网', '开放', '《', '开机', 'ip', '只', '位置', '同步',
       '操作系统', '华为', '所在', '上传', '盘', '主机'])
    print(frequency(case,return_type="tuple"))
    #print(probaitily(case,return_type='dict',optimization='-log'))#,optimization='-log'))
