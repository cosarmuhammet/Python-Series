# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:40:36 2022

@author: Mc
"""
# %%       #"kodu bölümlere ayırarak çalıştırmak için"
#variable (degisken)

var1 = 10 #integer
var2 = 15

gun = "pazartesi" #string

var3 = 10.0 #double

# %%
# String

s = "bugun gunlerden pazartesi"

variable_type = type(s)

print(s)

var1 = "ankara";
var2 = "ist"

var3 = var1+var2

uzunluk = len(var3)

# %%
# numbers

# int double
integer_deneme = -50

# double = float = ondalikli sayi

float_deneme = -30.7

# %%
# built in functions

str1 = "deneme"

float1 = 10.6
# float(10)
# int(float1)
# round(float1)

str2 = "1005"

# %% user defined functions

var1 = 10
var2 = 20


#fonksiyon parametresi = input
def benim_ilk_func (a,b):
    """
    
    ilk deneme
    
    parametre:
        
    return:
        
    """
    output = (a+b)*5
    
    return output
    
   
    
sonuc = benim_ilk_func(var1, var2)   

# %% default ve flexible functions

# default  f: cemberin cevre uzunlugu = 2*pi*r

def cember_cevresi_hesapla(r,pi = 3.14):
    
    """
    cember cevresi hesapla 
    input(parametre)= r
    output = cemberin cevresi
    """
    
    output = 2*pi*r
    
    return output

# flexible 

def hesapla(boy,kilo,*args):
    print(args)
    output = boy+kilo
    return output


# def hesapla(boy,kilo,yas):
#     output = boy+kilo*yas
#     return output

# %% QUIZ

# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len(),float())
# *args soyisim
# default parametre ayakkabi numarasi

yas = 5
name = "ali"
soyisim= "veli"

def function_quiz(yas,name, *args, ayakkabi_numarasi = 35):
    
    print("Cocugun ismi :",name, "yasi : ", yas, "ayak numarasi : ", ayakkabi_numarasi )
    print(type(name))
    print(float(yas))
    
    output = args[0] * yas
    
    return output

sonuc = function_quiz(yas, name, soyisim)
    
print("args[0]*yas =" , sonuc)

# %% Lambda function

def hesapla(x):
    
    
    return x*x

sonuc = hesapla(3)


sonuc2 = lambda x : x*x 
print(sonuc2(3))

# %%
# List

liste = [1,2,3,4,5,6]

liste_str = ["pazartesi","sali","carsamba"]

value = liste[1]
print(value)
   
last_value = liste[-1] # listenin son elemanını verir

liste_divide = liste[0:3] # listenin 0. elemanından 3. elemana kadar 3 dahil değil

liste_reverse = liste[::-1] # listeyi tersten yazdirma

liste.append(7) # liste sonuna eleman ekleme
liste.remove(7) # listeden belirtilen elemani cikarma
liste.reverse()# listeyi tersten yazdirma
liste.sort() # liste ici kücükten büyüge siralama

string_int_liste = [1,2,3,"aa","bb"]   

# %%
# Tuple (Degistirilemez liste)

t = (1,2,3,3,4,5,6)
    
t.count(3) # verilen degerin kac kere tekrar ettigini dondurur
t.index(5) # verilen degerin bulundugu indexi dondurur
   
    
# %% 
# Dictionary (Sözlük)   key-value

dictionary = {"Ali" : 32 , "Veli" : 45 , "Ayse" : 15}

# ali,veli,ayse = keys
# 32,45,15 = values

def deneme():
    dictionary = {"Ali" : 32 , "Veli" : 45 , "Ayse" : 15}
    return dictionary

dic = deneme()

dic2 = {"Ali": 13}

# %% Conditionals
# if else statement

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var1 esittir var2")
else:
    print("var1 kucuktur var2")
    
liste = [1,2,3,4,5]

value = 10
if value in liste:
    print("{} degeri listede bulunuyor".format(value))
else:
    print("{} degeri listede bulunmuyor".format(value))

# %%
# QUIZ

# 1640. yıl = 17.yuzyıl
# metod yazin 
     #input integer yillar
     #output yuzyil
# input = year >> 1<= year <=2005

def year2Century(year):
    
    """
    Year to century
    """
    
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):                               #100,200,300......
        if(str_year[1:3] == "00"): 
            return int(str_year[0])
        else:                                               # 190,250,440...
            return int(str_year[0]) + 1 
    else:                                                   #1700,1900....
        if(str_year[2:4] == "00"):  
            return int(str_year[:2])
        else:                                               #1705, 1645,1250
            return int(str_year[:2]) + 1 
    

year2Century(2005)


#2.Bir çözüm
def yuzyil(yil):
    if yil%100==0:
        return yil//100
    return yil//100+1

yuzyil(2002)

# %%
#For Loop

for each in range(1,11):
    print(each)
 #  
    
for each in "ankara ist":
    print(each)
 #  

for each in "ankara ist".split():
    print(each)
   
 #
liste = [1,2,3,56,7,82]

summation = sum(liste)
 #
count = 0
for each in liste:
    count = count + each
    print(count)

    
#While Loop

i=0
while(i<4):
    print(i)
    i = i+1

#

sinir = len(liste)
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1

# %% 
# QUIZ

# liste verecek
# listedeki en kucuk sayiyi bulan program

liste = [222,98,101,76,99]

enkucuk = liste[0]
enbuyuk = liste[0]

for i in liste:

    if(i < enkucuk):
        enkucuk = i
        
    if(i > enbuyuk):
        enbuyuk = i
    
print("{} sayisi listedeki en kucuk sayidir.".format(enkucuk))

print("{} sayisi listedeki en buyuk sayidir.".format(enbuyuk))

 # PYTHON BASİCS END
   
 