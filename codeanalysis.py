import os
import re
from subprocess import getoutput
import numpy as np
import pandas as pd
from tqdm import tqdm


def filesize_float(filepath):
    '''
    获得文件大小
    '''
    return os.path.getsize(filepath)/float(1024 **2 )

def filesize_to_MB(filepath):
    '''
    获得文件大小的MB单位
    '''
    return "%.10f MB"%(os.path.getsize(filepath)/float(1024 ** 2))

def filesize_to_GB(filepath):
    '''
    获得文件大小的GB单位
    '''
    return "%.10f GB"%(os.path.getsize(filepath)/float(1024 ** 3))

def filesize_to_TB(filepath):
    '''
    获得文件大小的TB单位
    '''
    return "%.10f TB"%(os.path.getsize(filepath)/float(1024 ** 4))

def getfilename(filepath):
    '''
    从路径中获得文件名
    '''
    return re.split("[/|,]",filepath)[-2]

def get_file_type_key(filename,types=['.py','txt','log','DS_Store','dp']):
    '''
    从文件名中获得疑似的文件类型
    Args:
        filename: 文件的绝对路径地址
        types: 选择的文件类型

    Returns:

    '''
    init_name_key_list = getfilename(filename).split('.')
    if len(init_name_key_list) > 1:
        return init_name_key_list[-1]
    else:
        return "empty"
    
def listfile_in_log_function(dirpath=os.getcwd(),save_path="filepaths.log"):
    '''

    Args:
        dirpath:
        save_path:

    Returns:

    '''
    print(getoutput("figlet Start searching for the path within the folder:"))
    counter = 0
    detGB = 0
    L = [0]
    time = 0
    f = open(save_path,"w+")
    for dir_,folder,files in tqdm(os.walk(dirpath)):
        for file in files:
            time+=1
            temp = os.path.join(dir_,file)
            check_file = os.path.isfile(temp)
            if check_file :
                filesize_float = os.path.getsize(temp)/float(1024 * 1024)
                filesize="%.10f MB"%(filesize_float)
                counter += filesize_float
                L.append(counter/1024)  
                detGB += L[-1]-L[-2]
                if detGB >=1:
                    print("计算得出增加1GB","%.10f GB"%(detGB),"当前累计文件共计:","%.10f GB"%(counter/1024),"累计文件数量:","%.0f 个"%(time))
                    detGB = 0 
            f.writelines(repr({temp+","+filesize})+"\n")
    f.close()
    end = "{}{}{}".format("end ","%.10f GB"%(counter/1024),"%.10f MB"%(counter))
    print(getoutput("figlet Path storage end !"))
    print(end)
    return end

    
def loadfile_to_infotable(logpath="filepaths.log"
                          ,columnsnumber=40
                          ,save_path="filepath_table.csv"):
    print(getoutput("figlet preprocess all file path data"))
    counter = 0
    detGB = 0
    L = [0]
    time = 0
    result = []
    files = open(logpath,'r').readlines()
    for file in files:
        time += 1
        init_vector = np.zeros(columnsnumber).astype(str)
        temp = re.split(r"[}|,|{]|\n| |'",file)[2]
        check_file = os.path.isfile(temp)
        if check_file :
            '''计算显示信息'''
            filesize_float = os.path.getsize(temp)/float(1024 **2 )
            counter += filesize_float
            L.append(counter/(1024))  
            detGB += L[-1]-L[-2]
            if detGB >=1:
                print("计算得出增加1GB","%.10f GB"%(detGB),"当前累计文件共计:","%.10f GB"%(counter/1024),"累计文件数量:","%.0f 个"%(time))
                detGB = 0 
            '''整理成表'''
            init_clearing_path_level1= os.path.split(temp)
            dirpath,filename = init_clearing_path_level1[0],init_clearing_path_level1[-1]
            level3 = -1
            abspath_list = temp.split(os.sep)
            abspath_ = abspath_list[:-1]
            file_name = abspath_list[-1].split('.')
            file_path = abspath_list+file_name[:-1]
            for dir_s in file_path:
                level3 += 1
                init_vector[level3]= dir_s
            init_vector[columnsnumber-1]= file_name[-1]
            init_vector[columnsnumber-2]=filesize_to_MB(temp)
            init_vector[columnsnumber-3]=temp
        result.append(init_vector)
        counter+= check_file
        if counter % 1000 == 0:
            print(pd.DataFrame(init_vector).T)
    table = pd.DataFrame(np.array(result))
    table.to_csv(save_path)
    print(getoutput("figlet preprocess is completed "))
    return table

if __name__ == "__main__":
    listfile_in_log_function(dirpath=os.path.expanduser("~"))
    #print(getoutput("figlet save path is OK !"))
    print(loadfile_to_infotable(save_path="~/linux_tools_for_chinese/filepath_table.csv"))