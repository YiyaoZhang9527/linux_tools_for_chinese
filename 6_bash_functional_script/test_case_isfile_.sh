#!/bin/sh 
#TODO shell判断文件,目录是否存在或者具有权限 
myPath="/var/log/httpd/" 
myFile="/var /log/httpd/access.log" 
# 这里的-x 参数判断$myPath是否存在并且是否具有可执行权限 
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi

#!/bin/bash
function demoFun1(){
    echo "这是我的第一个 shell 函数!"
    return `expr 1 + 1`
}

demoFun1
echo $?

function demoFun2(){
 echo "这是我的第二个 shell 函数!"
 expr 1 + 1
}

demoFun2
echo $?
demoFun1
echo 在这里插入命令！
echo $?

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";