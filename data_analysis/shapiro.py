#-*- coding:utf-8 _*- 
""" 
@file: shapiro.py 
@time: 2021/01/28
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

from scipy import stats
import numpy as np


'''
小样本数据的正态性校验
'''

np.random.seed(12345678)
x = stats.norm.rvs(loc=5, scale=10, size=80) # loc为均值，scale为方差

#夏皮罗维尔克检验法 (Shapiro-Wilk) 用于检验参数提供的一组小样本数据线是否符合正态分布，统计量越大则表示数据越符合正态分布，但是在非正态分布的小样本数据中也经常会出现较大的W值。
# 需要查表来估计其概率。由于原假设是其符合正态分布，所以当P值小于指定显著水平时表示其不符合正态分布。


print(stats.shapiro(x))


#返回结果 p-value=0.029035290703177452，比指定的显著水平（一般为5%）小，则拒绝假设：x不服从正态分布。
