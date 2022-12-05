# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:34:13 2022

@author: Mc
"""

# 1- Pandas hizli ve etkili for dataframes
# 2- Csv ve text dosyalarını acip inceleyip sonuçları bu dosya tiplerine daha rahat kaydedebilir
# 3- Pandas bize işimizi kolaylaştırıyor for missing data
# 4- Reshape yapıp datayı daha etkili bir şekilde kullanabiliriz.
# 5- Slicing indexing kolay
# 6- Time series data analizine cok yardımcı
# 7- Pandas hız açısından optimize edilmiş hızlı bir kütüphane


import pandas as pd

dictionary = {"Name": ["Ali","Veli","Kenan","Hilal","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)
 

head = dataFrame1.head() #DataFrame içindeki ilk 5 satırı verir
tail = dataFrame1.tail() #DataFrame içindeki son 5 satırı verir


# %% Pandas basic metods



print(dataFrame1.columns) #column isimleri

print(dataFrame1.info()) #Tablo info

print(dataFrame1.dtypes) #column type

print(dataFrame1.describe()) # numeric feature = columns (age,maas)


# %%  indexing and slicing

print(dataFrame1["Age"])

print(dataFrame1.Age)

dataFrame1["Yeni feature"] = [-1,-2,-3,-4,-5,-6] #Yeni Column ekleme

print(dataFrame1.loc[ : , "Age"])  #Tüm satırlar , istenen sütun

print(dataFrame1.loc[ 0:3 , "Age"])


print(dataFrame1.loc[:3, ["Age","Name"]])  #İlk 3 satır yaştan isime kadar olanları yazdır

print(dataFrame1.loc[::-1,:]) #Tersten yazdırma

print(dataFrame1.loc[:,:"Name"]) 

print(dataFrame1.loc[:,"Name"])

print(dataFrame1.iloc[:,2])

# %% Filtering

filtre1 = dataFrame1.Maas > 200

filtrelenmis_data = dataFrame1[filtre1] # Filtrelenmiş datayı yazdırma

filtre2 = dataFrame1.Age < 20 

dataFrame1[filtre1 & filtre2] # iki ayrı filtrelemeyi birleştirme

print(dataFrame1[dataFrame1.Age > 60])


# %% List comprehension

import numpy as np 

ortalama_maas = dataFrame1.Maas.mean() #Maas ortalamasını bulma

#ortalama_maas_np = np.mean(dataFrame1.Maas) #Numpy ile bulma

dataFrame1["Maas_seviyesi"] = [ "Dusuk Maas" if ortalama_maas > each else "Yuksek Maas" for each in dataFrame1.Maas]


#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("Dusuk Maas")
#    else:
#        print("Yuksek Maas")


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns]  #dataFrame columnlarını küçük harfe çevir

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]


# %% drop and concatenating (silme ve birleştirme)

dataFrame1.drop(["yeni_feature"], axis=1, inplace = True) #Column silme , inplace : güncellenen halini verilen dataFrameye eşitle

# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1) Yukarıdaki metotla aynı

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical (dikey) axis=0

data_concat = pd.concat([data1,data2],axis = 0) 

# horizontal (yatay) axis=1

maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)


# %% transforming data

dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.age]

# apply() metodu ile uygulama

def multiply(age):
    return age*2
    
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)


# Lamda fonksiyonu kullanarak da yapabiliriz.
 
dataFrame1["lamda_fonk_ile"] = dataFrame1.age.apply(lambda x: x*2)




