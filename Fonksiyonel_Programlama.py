#FONKSIYONEL PROGRAMLAMA

#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1:Bagimsizlik

A=9

def impure_sum(b) :
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(5)
pure_sum(3,4)

#İsimsiz Fonksiyonlar

def old_sum(a,b) :
    return a + b

old_sum(4,5)

new_sum = lambda a,b : a + b
new_sum(4,5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste
sorted(sirasiz_liste, key = lambda x : x[1])

#Vektörel Operasyonlar

#OOP

a=[1,2,3,4]
b=[2,3,4,5]

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

ab

#FP

import numpy as np

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

a*b


#map,filter and reduce

#map

liste=[1,2,3,4,5]
list(map(lambda x : x + 10 , liste))

#filter

liste=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x : x % 2 == 0 , liste))

#reduce

from functools import reduce

liste=[1,2,3,4]
reduce(lambda a,b : a + b , liste)

















