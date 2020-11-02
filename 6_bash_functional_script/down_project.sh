#!/bin/bash
# bash /Users/zhangjing/网络工具/MY_NLP_SCRIPT/down_project.sh
# 从阿里云下载下载项目文件到本地
rsync -av -e 'ssh -p 1121' root@47.114.143.177:/root/linux_tools_for_chinese/ /Users/zhangjing/linux_for_chinese_history/linux_tools_for_chinese
#date +%p_%Y_%m_%d_%H_%I_%S%_ > V_history.log