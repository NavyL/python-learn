# -*- coding: utf-8 -*-
h = float(input('你的身高是多少？（单位：米）'))
w = float(input('你的体重是多少？（单位：千克）'))
b = w/(h*h)
print('你的BMI指数是：%.1f' %b)
if b > 32:
    print('你的体型：严重肥胖')
elif b >= 28:
    print('你的体型：肥胖')
elif b >= 25:
    print('你的体型：过重')  
elif b >= 18.5:
    print('你的体型：正常')  
else:
    print('你的体型：过轻')  