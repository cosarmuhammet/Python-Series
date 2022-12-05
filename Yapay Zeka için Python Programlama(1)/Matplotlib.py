# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:20:07 2022

@author: Mc
"""
#Matplotlib kütüphanesi
#Gorsellestirme
# line plot, scatter plot, bar plot, subplots, histogram


import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique()) # unique türler
 
print(df.info())

print(df.describe()) #Veriler hakkında bilgi verir

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

# %% Line plot
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)

#df1.plot()
#plt.show() #Herzaman gerekli

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")


plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()


df1.plot(grid=True ,alpha= 0.9)
plt.show()



# %% Scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm ,color = "red" , label = "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")


plt.legend()

plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")

plt.show()

# %% Histogram

plt.hist(setosa.PetalLengthCm,bins= 50)

plt.xlabel("PetalLengthCm values")

plt.ylabel("frekans")

plt.title("hist")
plt.show()


#%%  

import numpy as np

#x = np.array([1,2,3,4,5,6,7])
#
#y = x*2+5
#
#plt.bar(x,y)
#plt.title("bar plot")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% Subplot

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(3,1,1)  #Kaç satır olacağı ve hangi satırda gösterileceğini ayarlıyoruz.
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(3,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.subplot(3,1,3)
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")
plt.ylabel("virginica -PetalLengthCm")

plt.show()










