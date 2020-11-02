# -*- encoding: utf-8 -*-
'''
@File    :   question_data.py
@Time    :   2020/10/06 00:28:19
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib

import numpy as np
import data_preprocessing
from jieba import cut
from ast import literal_eval
from os import path,symlink,listdir
from path_file import home , program_dir

loadtext = open("{}{}".format(home,"/网络工具/MY_NLP_SCRIPT/question_file.txt","r")).read()

change_data_type = literal_eval(loadtext)

return_cmd = change_data_type

questions = [list(cut(ask)) for ask in return_cmd]
all_word = np.array([j for i in questions for j in i])

word_dict,word_vector,read_original,init_paper = data_preprocessing.data_preprocessing(questions)


