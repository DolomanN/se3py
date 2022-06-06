#Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141.

import math
accuracy = input ("введите точность вычисления Пи: ")
Pi = math.pi
def dot(number):
    if '.' in accuracy:
        return abs(accuracy.find('.') - len(accuracy)) - 1
    else:
        return 0

if "." in accuracy:
    print (round(Pi,int(dot(accuracy))))
else: 
    print (round(Pi,int(accuracy)))

