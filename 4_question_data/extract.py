# TODO 正则提取集合
import re
import jieba
from zhon import hanzi
from zhon import pinyin

'''加载标准停用词（标点符号）'''
stopwords = list(hanzi.stops)+list(hanzi.non_stops)+list(pinyin.stops)+list(pinyin.non_stops)


#TODO 正则提取

def extract_english(original):
    '''
    只要英文
    '''
    return re.findall(r'[a-zA-Z]+', original)

def extract_chinese(original):
    '''
    只要中文
    '''
    return re.findall(u'[\u4e00-\u9fa5]',original)

def extract_numbers(original):
    '''
    只要数字
    '''
    return re.findall(r'\d+',original)

def extract_numbers(original):
    '''
    只要数字和英文
    '''
    return re.findall(r'[a-zA-Z0-9]',original)

def temp_extract(strings,symbles=stopwords):
    '''
    临时删除
    '''
    srcrep = {i:'' for i in symbles }
    rep = dict((re.escape(k), v) for k, v in srcrep.items())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], strings)


#TODO 中英文字符判断

def is_chinese(uchar):
        """
        判断一个unicode是否是汉字
        """
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

def is_number(uchar):
        """
        判断一个unicode是否是数字
        """
        if uchar >= u'\u0030' and uchar<=u'\u0039':
                return True
        else:
                return False

def is_alphabet(uchar):
        """
        判断一个unicode是否是英文字母
        """
        if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
        else:
                return False

def is_other(uchar):
        """
        判断是否非汉字，数字和英文字符
        """
        if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
                return True
        else:
                return False

def split_character_type(original):
    '''
    不同字符类型分割
    '''
    make = [0]
    diff = []
    n = 0
    temp = ""
    for char in original:
        if is_chinese(char):
            n = 0
        elif is_number(char):
            n = 1
        elif is_alphabet(char):
            n = 2
        elif is_other(char):
            n = 3
        else:
            n = 4
        make.append(n)
        if (make[-1]-make[-2]) == 0:
            diff.append(char)
        else:
            diff.append("|")
            diff.append(char)      
    return "".join(diff).split("|")

#TODO 分词过滤转换

def split_words_from_chinese_func(original):
    '''
    中文分词
    '''
    return list(jieba.cut(context_func(original)))


def split_words_from_english_func(original):
    '''
    英文空格分词
    '''
    return original.split()

def filter_stop_words(words_list,stop_words_dict = stopwords):
    '''
    过滤停用词
    '''
    return [word for word in words_list if word not in stop_words_dict ]

def case_conversion(msg,key=None):
    '''
    英文转换 
    key : 选择转换方式
    '''
    if key==None:
        return None
    return {"upper":msg.upper()  #upper()函数，将所有字母都转换成大写
     ,"lower":msg.lower()  #lower()函数，将所有字母都转换成小写
     ,"capitalize":msg.capitalize()  #capitalize()函数，将首字母都转换成大写，其余小写
     ,"title":msg.title()}[key] # 所有分隔英文单词首字母大写
    
def context_func(paper_list):
    '''
    连接上下文
    '''
    return "".join(paper_list)

def extract_email_flag_is_a_function_of_com(text):
    '''
    提取结尾是com的邮箱
    '''
    result = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com", text)
    print(result)

def extract_email_flag_is_a_function_of_org(text):
    '''
    提取结尾是org的邮箱
    '''
    result = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.org", text)
    print(result)

