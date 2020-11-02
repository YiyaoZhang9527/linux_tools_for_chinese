#!bash/bin
#系统运行查看
cat /proc/uptime| awk -F. '{run_days=$1 / 86400;run_hour=($1 % 86400)/3600;run_minute=($1 % 3600)/60;run_second=$1 % 60;printf("系统已运行：%d天%d时%d分%d秒",run_days,run_hour,run_minute,run_second)}'

#刷新DNS缓存
sudo /etc/init.d/nscd restart
#抓包
sudo tcpdump -i any

# #命令行代理翻墙
alias http_proxy="export http_proxy=\"http://127.0.0.1:12333\""
alias https_proxy="export https_proxy=\"http://127.0.0.1:12333\""
#刷新DNS缓存
alias reDNS="sudo /etc/init.d/nscd restart"
#抓包
alias checkPakg="sudo tcpdump -i any"
# GPU状态
alias GPUstate="watch -n 1 nvidia-smi"
#每隔一秒高亮显示网络连接数变化
alias NetWorkState="watch -n 1 -d netstat -ant"
#输出系统运行时间信息
alias runing_time_info="bash /home/manman/my_tools/system_info.sh"
#反向服务器快捷方式
#系统运行查看