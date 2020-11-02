#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wangyi.py
@Time    :   2020/08/19 15:49:15
@Author  :   ManmanZhang
@Version :   1.0
@Contact :   408903228@qq.com
@Desc    :   None
'''

# here put the import lib
#coding=utf-8
import json
import requests

def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error ,can\'t use it now'

def reuslt(repsonse):
    result = json.loads(repsonse)
    print("input：%s" % result['translateResult'][0][0]['src'])
    print("translation：%s" % result['translateResult'][0][0]['tgt'])
    return result['translateResult'][0][0]['tgt']

def main():
    word = input('please enter a word or sentence：')
    list_trans = translate(word)
    reuslt(list_trans)

def translateapi(word):
    return {i:reuslt(translate(i)) for i in word}


if __name__ == '__main__':
    main()