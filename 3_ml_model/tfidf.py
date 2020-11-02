# -*- encoding: utf-8 -*-
'''
@File    :   tfidf.py
@Time    :   2020/10/05 22:09:15
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib

import numpy as np
#from tqdm import tqdm



#TODO : TF算法
def TF(paper_words,word_vector):
    m = word_vector.size
    init_TF = np.zeros(m)
    for word in paper_words:
        if word in word_vector:
            index_ = np.argwhere(word_vector==word)[0][0]
            init_TF[index_] += 1
    return init_TF

#TODO ：IDF算法
def IDF(paper_words_list,word_vector):
    m = word_vector.size
    init_IDF = np.zeros(m)
    N = paper_words_list.shape
    n = -1
    for word in word_vector:
    #for word in tqdm(word_vector,desc = 'IDF词汇'):
        n += 1
        for paper_arr in paper_words_list:
            if word in paper_arr:
                init_IDF[n] += 1
    return np.log(N/(init_IDF+1))

#TODO : 整个训练TFIDF词向量
def TFIDF(paper_words_list,word_vector):
    IDF_arr = IDF(init_paper,word_vector)
    #TF_arr = np.array([TF(paper,word_vector) for paper in tqdm(paper_words_list,desc = 'TF矩阵')])
    TF_arr = np.array([TF(paper,word_vector) for paper in paper_words_list])
    return TF_arr*IDF_arr,IDF_arr

