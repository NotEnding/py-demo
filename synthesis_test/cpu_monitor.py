#-*- coding:utf-8 _*- 
""" 
@file: cpu_monitor.py 
@time: 2020/12/18
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import psutil
import time


print(f"{'*'*40} CPU INFO {'*'*40}")
# cpu信息
print(f"CPU的个数：{psutil.cpu_count()}")
print(f"cpu的利用率：{psutil.cpu_percent()}")
print(f"cpu的时间花费：{psutil.cpu_times()}")
print(f"cpu的耗时比例:{psutil.cpu_times_percent()}")
print(f"cpu的status:{psutil.cpu_stats()}")
print(f"cpu的频率:{psutil.cpu_freq()}")

print(f"{'*'*40} MEMORY INFO {'*'*40}")
# 内存信息
mem = psutil.virtual_memory()
print(f"总内存：{mem.total}")
print(f"可用内存:{mem.available}")
print(f"内存利用率:{mem.percent}")
print(f"已使用内存:{mem.used}")
print(f"空闲内存:{mem.free}")
# print(f"active:{mem.active}")
# print(f"inactive:{mem.inactive}")
# print(f"buffer:{mem.buffers}")
# print(f"cached:{mem.cached}")
# print(f"shared:{mem.shared}")
# print(f"slab:{mem.slab}")
print(f"swap memory:{psutil.swap_memory()}")

print(f"{'*'*40} DISK INFO {'*'*40}")
# 查看硬盘信息统计
print(f"返回磁盘io统计信息统计信息：{psutil.disk_io_counters()}")
print(f"返回所有已挂载的磁盘统计信息：{psutil.disk_partitions()}")
print(f"返回path所在磁盘的使用情况：{psutil.disk_usage('/')}")


print(f"{'*'*40} NETWORK INFO {'*'*40}")
#网络io相关信息
print(f"返回每块网卡的网络IO统计信息:{psutil.net_io_counters()}")
print(f"返回每个网络连接的详细信息:{psutil.net_connections()}")
print(f"网卡的配置信息:{psutil.net_if_addrs()}")
print(f"网卡的详细信息:{psutil.net_if_stats()}")
print(f"返回当前登录用户的信息：{psutil.users()}")
print(f"返回系统的启动时间:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(psutil.boot_time()))}")


print(f"{'*'*40} PID INFO {'*'*40}")
# 进程相关信息
print(f"返回当前正在运行的进程：{psutil.pids()}")
print(f"判断给定的pid是否存在:{psutil.pid_exists(7248)}")
print(f"返回当前正在运行的进程:{psutil.process_iter()}")
print(f"对进程进行封装，可以使用该类的方法获取进行的详细信息，或者给进程发送信号:{psutil.Process(pid=7248)}")
#进程相关信息的方法：
# name：获取进程的名称
# cmdline：获取启动进程的命令行参数
# create_time：获取进程的创建时间(时间戳格式)
# num_fds：进程打开的文件个数
# num_threads：进程的子进程个数
# is_running：判断进程是否正在运行
# send_signal：给进程发送信号，类似与os.kill等
# kill：发送SIGKILL信号结束进程
# terminate：发送SIGTEAM信号结束进程