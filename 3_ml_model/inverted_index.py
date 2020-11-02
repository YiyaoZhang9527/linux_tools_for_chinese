# -*- encoding: utf-8 -*-
'''
@File    :   inverted_index.py
@Time    :   2020/10/06 00:31:42
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib
from tqdm import tqdm
import sys
from os.path import expanduser
from os import sep,path
# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
sys.path.append(project)
# 加载各模块位置
from file_tools import ml_model_dir, search_moduel_dir, data_preprocessing_dir, python_functional_script_dir, bash_functional_script_dir, data_structure_dir, question_data_dir, math_module_dir,info_table,onehot_matrix_static_list,word_frequency_of_each_articles_static_table,eigenvector_static_table,feature_static_dictionary,feature_static_vector,static_cache_dir
# 加载机器学习模块
sys.path.append(data_preprocessing_dir)
import text_preprocessing
sys.path.append(question_data_dir)
from onehot_encoding import onehot_encoding


#TODO ：构造到排表函数 
def inverted_index(paper,word_vector):
    result = dict()
    n = -1
    #for i in tqdm(paper,desc='倒排表当前排序的文章'):
    for i in paper:
        n += 1
        for j in i:
            if j in word_vector:
                if j in result:
                    result[j] = result[j]+[n]
                else:
                    result.update({j:[n]})
    return {i:list(set(result[i])) for i in result}


def check_data_function(original_data=None
                        ,word_vectors_path=None
                        ,word_punct_tokenizer_datas_path=None
                        ):
    '''
    检查并且预加载到排表所需数据
    '''
    if path.isfile(word_vectors_path) and path.isfile(word_punct_tokenizer_datas_path):
        pass
    elif path.isfile(original_data):
        onehot_encoding(original_data)
        pass
    return None

def inverted_index_function(original):
    clearing_data = text_preprocessing(original)
    return clearing_data

if __name__ == "__main__":
    #inverted_index_function()