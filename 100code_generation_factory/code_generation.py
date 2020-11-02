# -*- encoding: utf-8 -*-
'''
@File    :   code_generation.py
@Time    :   2020/10/29 23:14:19
@Author  :   DataMagician 
@Version :   1.0
@Contact :   408903228@qq.com
'''

# here put the import lib

from os import getcwd,walk
from os.path import sep,isdir
from os import path
import re 
from ast import literal_eval
import numpy as np
from numpy.linalg import solve

variable_base = ['！', '？', '｡', '。', '＂', '＃'
, '＄', '％', '＆', '＇', '（', '）', '＊'
, '＋', '，', '－', '／', '：', '；', '＜'
, '＝', '＞', '＠', '［', '＼', '］', '＾'
, '＿', '｀', '｛', '｜', '｝', '～', '｟'
, '｠', '｢', '｣', '､', '\u3000', '、', '〃'
, '〈', '〉', '《', '》', '「', '」', '『'
, '』', '【', '】', '〔', '〕', '〖', '〗'
, '〘', '〙', '〚', '〛', '〜', '〝', '〞'
, '〟', '〰', '〾', '〿', '–', '—', '‘'
, '’', '‛', '“', '”', '„', '‟', '…', '‧'
, '﹏', '﹑', '﹔', '·', '.', '!', '?', '"'
, '#', '$', '%', '&', "'", '(', ')', '*'
, '+', ',', '-', '/', ':', ';', '<', '='
, '>', '@', '[', '\\', ']', '^', '_', '`'
, '{', '|', '}', '~']

variable_function_stop = "func function functions".split()+variable_base

def extract_english_function(original):
    '''
    只要英文
    '''
    return re.findall(r'[a-zA-Z]+', original)

def extract_numbers(original):
    '''
    只要数字
    '''
    return re.findall(r'\d+',original)

def extract_numbers_and_english_function(original):
    '''
    只要数字和英文
    '''
    return re.findall(r'[a-zA-Z0-9]',original)

def extract_segment_functions(strings,symbol_to_delete=variable_base):
    """
    '提取其他'
    """
    srcrep = {i:'' for i in symbol_to_delete}
    rep = dict((re.escape(k), v) for k, v in srcrep.items())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], strings)

def generation_function(function_names=False
                        ,dir_path=getcwd()
                        ,default_del=variable_function_stop
                        ,mode="a+"):
    '''
    批量生成函数
    '''
    if isinstance(function_names,dict) and isdir(dir_path):
        
        filename = list(function_names)[0]
        filepath = dir_path+sep+filename+'.py'
        f = open(filepath,mode)
        print(filepath)
        if dir_path and function_names:
            for function_items in function_names[filename]:
                init_function_name,function_API = tuple(*(function_items.items()))
                function_name = "".join(list(map(lambda x : extract_segment_functions(x,symbol_to_delete=default_del)+"_" ,extract_english_function(init_function_name))))[:-1].lower().replace("_tion_","")
                print(function_name)
                function_line = ("def "+ function_name+"_function"+"():\n"+'    """\n    '+repr(function_API)+'\n    """\n'+"    "+"pass\n\n").replace("__","_")
                print(function_line)
                f.writelines(function_line)
        f.close()

def generate_variable_names_function(variable_names=False
                            ,dir_path=getcwd()
                            ,default_del=variable_function_stop
                            ,mode="a+"):
    '''
    批量生成变量名
    '''
    if isinstance(variable_names,dict) and isdir(dir_path):
        
        filename = list(variable_names)[0]
        filepath = dir_path+sep+filename+'.py'
        f = open(filepath,mode)
        #print(filepath)
        if dir_path and variable_names:
            for variable_items in variable_names[filename]:
                init_variable_name,annotation = tuple(*(variable_items.items()))
                variable_name = ("".join(list(map(lambda x : extract_segment_functions(x,symbol_to_delete=default_del)+"_" ,extract_english_function(init_variable_name))))[:-1]).lower()
                variable_line = "variable_"+variable_name + ' = "" #'+annotation + "\n\n"
                f.writelines(variable_line)
        f.close() 

def search_files_function(target,dirpath=getcwd(),default_del=variable_function_stop):
    '''
    列出文件夹下所有路径
    '''
    configfile = path.expanduser("~/linux_tools_for_chinese/8_static_cache/file_path_config.py")
    configdir = path.expanduser("~/linux_tools_for_chinese/8_static_cache/dir_path_config.py")
    f = open(configfile,'w+')
    d = open(configdir,"w+")
    file_type_dict = {'csv':[],'other':[],'log':[],'sh':[],
                      'txt':[],'pyc':[],'ini':[],'josn':[],
                      'DS_Store':[],'py':[],'json':[],'ipynb':[],
                      }
    check_path_config = path.expanduser("~/linux_tools_for_chinese/8_static_cache/pathconfig.")
    for dir_,folder,files in walk(dirpath):
        for file in files:
            temp = path.join(dir_,file)
            split_file_name = temp.split(".")
            file_type = split_file_name[-1]
            clearning_file_name = split_file_name[0]
            if file_type in file_type_dict:
                file_type_dict[file_type].append(temp)
            else:
                file_type_dict["other"].append(temp)
            init_var_name = path.split(temp)[-1].split(".")[0]
            var_name = ("".join(list(map(lambda x : extract_segment_functions(x,symbol_to_delete=default_del)+"_" ,extract_english_function(init_var_name))))[:-1]).lower()+"".join(extract_numbers(init_var_name))
            if len(var_name):
                code_characters_of_file = "var_"+(var_name) + ' = "'+ clearning_file_name+'"\n'
                code_characters_of_dir = "dir_"+"".join(list(map(lambda x:x+'_',extract_english_function(path.split(temp)[0].split(sep)[-1])))) + ' = "'+path.split(temp)[0]+'"\n'

                print(code_characters_of_file)
                print(code_characters_of_dir)
            d.writelines(code_characters_of_dir)
            f.writelines(code_characters_of_file)
    f.close()
    d.close()
                
                
    return file_type_dict



'''
def generates_the_path_function(paths,dir_path=getcwd(),new_path=False,default_del=variable_function_stop,mode="a+"):
    

    filename = list(paths)[0]
    filepath = dir_path+sep+filename+'.py'
    f = open(filepath,mode)
    #print(filepath)
    if dir_path and paths:
        for variable_items in paths[filename]:
            init_variable_name,annotation = tuple(*(variable_items.items()))
            variable_name = "".join(list(map(lambda x : extract_segment_functions(x,symbol_to_delete=default_del)+"_" ,extract_english_function(init_variable_name))))[:-1]
            variable_line = "variable_"+variable_name + ' = "" #'+annotation + "\n\n"
            f.writelines(variable_line)
    f.close() 
'''

if __name__ == "__main__":
    function_names = {"test":[
                {'Save as csv format':"保存为csv格式"},
                {'Save as josn':"保存为josn格式"},
                {'Save as text format':"保存为text格式"},
                {'Synchronize files to remote servers':"同步文件到远程服务器"},
                {'Synchronize files to local servers':'同步文件到本地服务器'},
                {"Convert the dictionary to JOSn":"将字典转换为josn"},
                {"Convert dictionary to DataFrame":"将字典转换为数据帧"},
                {"create folder function":"创建文件夹函数"}
                ]}
    generate_variable_names_function(function_names,mode="w+")
    generation_function(function_names)
    search_files_function("8_static_cache",path.expanduser("~/linux_tools_for_chinese/"))
    #print(generates_the_path_function(function_names,new_path="/7_python_functional_script"))
    