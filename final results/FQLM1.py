
import random
import numpy as np
import math


def insertinfile(maplist):
    with open('map.txt', 'w') as f:
        bstring = binarystring(maplist)
        f.write(bstring)
        print('Attached in file')


def binarystring(maplist):
    binarylist = ['{:032b}'.format(int(round(num * 2 ** 32))) for num in maplist]
    binarystring = ''
    for i in binarylist:
        binarystring += i
    return (binarystring)


def xorinfile(x, y):
    with open('map.txt', 'w') as f:
        bstring1 = binarystring(x)
        bstring2 = binarystring(y)
        bstring = ''
        for i in range(len(bstring1)):
            if (bstring1[i] == bstring2[i]):
                bstring += '0'
            else:
                bstring += '1'
        f.write(bstring)
        print('Attached in file')


def testlist(maplist):
    count = 0
    for i in maplist:
        count += 1
        if i > 1:
            print(i, 'Element is greater than 1')
            return False
    else:
        print('All elements <= 1 and number of elements =', count)
        return True


def spmod(a, b=1):
    return a - math.floor(a / b) * b
#all 14
def MS_map1(r1,r2,x):
    return spmod(r1*r2*x/(1+r2*(1-x)**2))

def circle_map1(w,k,x):
    return spmod(x + w + (k/(2*(math.pi)))*math.sin(2*math.pi*x))

def MScircle_map2(r1,r2,w,k,x0,n):
    '''f: x[i+1] = mod(r1*r2*x[i]/(1+r2*(1-x[i])**2),1)
    g: x[i+1] = mod(x[i] + w + (k/2π)*sin(2πx[i]))
    map = gof
    '''
    print(x0)
    y = np.zeros(n+1)
    y[0] = x0
    for i in range(1,n+1):
        y[i] = circle_map1(w,k,MS_map1(r1,r2,y[i-1]))
    return y[1:]

x = MScircle_map2(r1 = 3.8, r2 = 3, w = 0.5, k = 1000, x0 = 0.9, n = 50115)

if testlist(maplist = x):
    insertinfile(maplist = x)