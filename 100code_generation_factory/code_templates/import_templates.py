import sys
from os.path import expanduser
from os import sep
# 加载自定义模块
project = "{}{}{}".format(expanduser("~"),sep,"linux_tools_for_chinese")
sys.path.append(project)
# 加载各模块位置
from file_tools import ml_model_dir, search_moduel_dir, data_preprocessing_dir, python_functional_script_dir, bash_functional_script_dir, data_structure_dir, question_data_dir, math_module_dir,info_table,onehot_matrix_static_list,word_frequency_of_each_articles_static_table,eigenvector_static_table,feature_static_dictionary,feature_static_vector,static_cache_dir

# 加载机器学习模块
sys.path.append(ml_model_dir)
from tfidf import TF,IDF,TFIDF
import simulate_anneal
from feature_dictionary_editor import feature_dictionary_editor
from onehot_encoding import character_encoding

# 加载数据预处理模块
sys.path.append(data_preprocessing_dir)
import extract,determine_character_type,text_preprocessing

# 加载数据结构模块
sys.path.append(data_structure_dir)
from data_structure import check_ndarray,deeping_flatten,data_structure_normalization

# 加载数学模块
sys.path.append(math_module_dir)
from statistics_module import frequency,sort_by_dictionary_value,probability_optimization,probaitily
sys.path.append(static_cache_dir)