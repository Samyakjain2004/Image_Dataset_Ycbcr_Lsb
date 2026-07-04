import math
import numpy as np

def insertinfile(maplist):
    with open('map.txt2', 'w') as f:
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
    with open('map.txt2', 'w') as f:
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




def symmetry1_map1x(r,k5,x,y,z):
    return spmod((r*k5*y*(1-x)+z))
def symmetry1_map1y(r,k6,x,y,z,x2):
    return spmod((r*k6*y)+(z*(1+x2**2)))
def symmetry1_map1z(r,k7,x,y,z,x2,y2):
    return spmod(r*(x2+y2+k7)*math.sin(z))

def symmetry1_map2(r,k5,k6,k7,x0,y0,z0,n):
    '''map =
    x[i+1] = mod((r*k5*y[i]*(1-x[i])+z[i]),1))
    y[i+1] = mod((r*k6*y[i])+(z[i](1+x[i+1]*2))),1)
    z[i+1] = mod(r*(x[i+1]+y[i+1]+k7)*sin(z[i]),1)
    r belongs to (3.564,4)
    |k5| > 34.9
    |k6| > 38.9
    |k7| > 36.7
    x0, y0, z0 belongs to [0,1)'''
    print(x0,y0,z0)
    x,y,z = np.zeros(n//3+1),np.zeros(n//3+1),np.zeros(n//3+1)
    x[0],y[0],z[0]= x0, y0, z0
    for i in range(1,n//3 + 1):
        x[i] = symmetry1_map1x(r,k5,x[i-1],y[i-1],z[i-1])
        y[i] = symmetry1_map1y(r,k6,x[i-1],y[i-1],z[i-1],x[i])
        z[i] = symmetry1_map1z(r,k7,x[i-1],y[i-1],z[i-1],x[i],y[i])
    x = list(x[1:])
    x.extend(y[1:])
    x.extend(z[1:])
    return x

x = symmetry1_map2(r = 3.6, k5 =36, k6 =40, k7 =37, x0 = 0.842403647190268, y0 = 0.9828947516391313, z0 = 0.6427805713453543, n = 50115)

if testlist(maplist = x):
    insertinfile(maplist = x)