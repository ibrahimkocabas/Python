#VERI YAPILARI (DATA TYPES)

#Listeler

notlar =[90,80,70]
type(notlar)

liste=["a",19.3,32]
len(liste)

yeni_liste=[notlar,liste]
yeni_liste[0]
yeni_liste[1]


#Eleman İşlemleri

liste=[10,20,30,40,50]
liste[0]
liste[3]

liste[0:3]

yeni_liste=["a",10,[20,30,40]]
yeni_liste[:2]
yeni_liste[2][1]

#Eleman Değiştirme,Ekleme,Silme

liste=["ali","veli","berkcan","ayse"]
liste

liste[1]="ibrahim"
liste

liste[0:3]=["Birsen","Resul","Hanife"]
liste


liste=["ali","veli","berkcan","ayse"]

liste=liste + ["kemal"]
liste

del liste[2]
liste

#Liste Methodları

liste=["ali","veli","hasan"]
dir(liste)

liste.append("ibrahim")
liste

liste.remove("ali")
liste


liste=["ali","veli","hasan"]
liste.insert(0,"ibrahim")
liste

liste=["ali","veli","hasan"]
liste.insert(len(liste),"ayse")
liste

liste=["ali","veli","hasan"]
liste.pop(2)
liste


liste=["ali","veli","isik","ali","veli"]
liste.count("ali")
liste.count("veli")

liste_yedek = liste.copy()

liste.extend(["a","b",32])
liste


liste.index("ali")

liste.reverse()
liste

liste = [10,40,5,90]
liste.sort()
liste

liste.clear()
liste

#Veri Yapıları-Tuple

#Tuple(Demet) Olşturma

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t = "ali","veli",1,2,3.2,[1,2,3]

t = ("eleman",)
type(t)

#Tuple Eleman Islemleri

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t[1]
t[0:3]


#Veri Yapıları-Dictionary(Sözlük)

#Sozluk Oluşturma

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}
sozluk
len(sozluk)

#Sozluk Eleman İşlemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk[0] #sıralı olmayışından dolayı key error veriyor

sozluk["REG"]

#Sozluk - Eleman Ekleme ve Değiştirme

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac" #eleman ekleme-liste sonuna eklenir
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

#Veri Yapıları - Setler

#Set Olusturma

s = set()
s

l = [1,"a","ali",32]
s = set(l)
s

t = ("ali","a")
s = set(t)
s

#Set(Küme) Eleman Ekleme ve Çıkarma

l = ["gelecegi","yazanlar"]
s = set(l)
s

s.add("ile")
s

s.remove("gelecegi")
s

#Setlerde Fark İşlemleri

#difference and symmetric_difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

#intersection and union


set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set1 & set2

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.union(set2)







