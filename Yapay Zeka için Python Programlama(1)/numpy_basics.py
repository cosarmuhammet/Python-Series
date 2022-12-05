# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:26:16 2022

@author: Mc
"""

#%% NUMPY Basics

import numpy as np     #import etme

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])  # 1*15 matris

print(array.shape)

a = array.reshape(3,4)
print("Dizinin boyutu: ", a.shape)       # (satır , sütun)
print("Dizinin satır sayısı: ", a.ndim ) 
print("Dizinin sütun sayısı: ", len(a) )

print("data type: ", a.dtype.name)
print("Size: ", a.size )

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

zeros = np.zeros ((3,4)) #0 matrisi

zeros[0,0] = 5 #Matris elemanı güncelleme
print(zeros)

np.ones((3,3))  #Bir matrisi

np.empty((2,3)) #Boş bir dizi oluşturur

x = np.arange(10,50,5) # 10 dan 50 ye kadar 5 er atlayarak array oluşturma
print(x)

y = np.linspace(10,50,20) # 10dan 50 ye kadar araya 20 tane sayı yazıyor





#%% Numpy Basic Operations
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a ** 2) 

print(a<2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

# element wise prodcut
print(a*b)

#matris product

a.dot(b.T)  #Transpoz alıp çarpıldı

a = np.random.random((5,5))

print("Toplam: ",a.sum())
print("Max: ",a.max())
print("Min: ",a.min())


print(a.sum(axis=0)) #Sütunları topla
print(a.sum(axis=1)) #Satırları topla


print(np.sqrt(a)) #karekök
print(np.square(a)) # a**2


print(np.add(a,a)) # a+a

# %% İndexing and slicing

import numpy as np

array = np.array([1,2,3,4,5,6,7])

print(array[0])
print(array[0:3])

reverse_array = array[ : :-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[0,4]) # (satır,sütun)

print(array1[ : ,1 ]) #Satırların hepsinden 0,1 indexlerini yazdırır
print(array1[ 1, 1:4 ])

print(array1[ -1, : ]) # Son satırı al
print(array1[ : ,-1]) #Son sütunu al

# %% Shape Manipulation

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten 

a = array.ravel() #Cok boyutlu diziyi tek boyutluya donusturme

array2 = a.reshape(3,3)

arrayT = array2.T #Transpoz alma


array5 = ([[1,2],[3,4],[5,6]])
#array5.resize((3,2))  # (3,2)'lik matrisi (2,3)' e çevirme

#%% Stacking arrays
import numpy as np

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical (dikey) Birleştirme

#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))

# horizontal (yatay) Birleştirme

#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))


#%% Convert and copy

import numpy as np

liste = [1,2,3,4] #Liste

array = np.array(liste) #np array

liste2 = list(array)


a = np.array([1,2,3])

b = a
b[0] = 5
c = a



d =  np.array([1,2,3])

e = d.copy()

f = d.copy()




















