#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   init_algorithm.py
@Time    :   2020/10/27 14:45:54
@Author  :   Rao Guangxiang 
@Version :   1.0
@Contact :   408903228@qq.com
@License :   my-self
@Desc    :   None
'''

# here put the import lib

import sys
from os.path import expanduser
from os import sep
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
sys.path.append(project)
from file_tools import algorithm_dir,question_data_dir
sys.path.append(algorithm_dir)
from algorithm.tfidf import TFIDF
sys.path.append(question_data_dir)
#from question_data.question_data import init_paper,word_vector

code_of_TFIDF,IDF_var = TFIDF(init_paper,word_vector)