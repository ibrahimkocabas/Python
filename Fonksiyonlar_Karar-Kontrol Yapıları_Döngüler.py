# FONKSÄ°YONLAR

#Fonksiyon Nasıl YazÄ±lÄ±r ?

def kare_al(x) :
    print(x**2)
   
kare_al(5)

#Bilgi Notuyla Cikti Uretmek
    
def kare_al(x) :
    print("Girilen Sayinin Karesi :" + str(x**2))
   
kare_al(5)

#Iki Argumanlı Fonksiyon Tanimlamak

def carpma_yap(x,y):
    print(x*y)

carpma_yap(5,4)  

#Ne Zaman Fonksiyon Yazılır ?

def direk_hesap(isi,nem,sarj):
    print ((isi + nem)/ sarj)

direk_hesap(30,60,33)   

#Fonksiyonlar sık tekrar eden ya da uzun islemlerden kurtulmak icin yazılan ifadelerdir.    
    

#Fonksiyonların Cıktılarını Girdi Olarak Kullanma : return

def direk_hesap(isi,nem,sarj):
    return (isi + nem) / sarj

direk_hesap(30,60,33)*9
cikti = direk_hesap(45,30,85)
cikti
print(cikti)

#Local Etki Alanından Global Etki Alanıni Degistirmek

x=[]

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi.")
    
eleman_ekle("Ali")    
eleman_ekle("Veli")
x
    
# KARAR & KONTROL YAPILARI   

#True-False Sorgulamaları

sinir =5000
sinir == 4000
sinir == 5000

#if

sinir = 50000
gelir = 40000

if gelir < sinir :
    print ("Gelir sinirdan kucuk")

#else

sinir = 50000
gelir = 40000

if gelir > sinir :
    print("Gelir sinirdan buyuk")
else :
     print("Gelir sinirdan kucuk")   
    

sinir = 50000
gelir = 51000

if gelir == sinir :
    print("Gelir sinira esittir")
else :
     print("Gelir sinira esit degildir")     

#elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir :
    print("Tebrikler,hediye kazandınız.")
elif gelir1 < sinir :
    print("Uyarı !")
else:
    print("Takibe devam")

     
if gelir3 > sinir :
    print("Tebrikler,hediye kazandınız.")
elif gelir3 < sinir :
    print("Uyarı !")
else:
    print("Takibe devam")
    

if gelir2 > sinir :
    print("Tebrikler,hediye kazandınız.")
elif gelir1 < sinir :
    print("Uyarı !")
else:
    print("Takibe devam")


    
#Mini Ornek Uygulama

sinir = 50000

magaza_adi = input("Magaza Adinizi Giriniz:")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler " + magaza_adi + " promosyon kazandiniz .")
elif gelir < sinir:
    print("Uyarı ! Geliriniz cok dusuk :" + str(gelir))
else:
    print("Takibe devam")
    
     

#DÖNGÜLER

#for

ogrenci = ["ali","veli","isik","berk"]    

for i in ogrenci :
    print(i)
    
#Döngü ve Fonksiyonların Birlikte Kullanılması

maaslar = [1000,2000,3000,4000,5000]

def yeni_maas(x):
    print(x*20/100 + x)
    
 yeni_maas(2000)   

for i in maaslar:
    yeni_maas(i)


#if , for ve fonksiyonları birlikte kullanma
#mini uygulama

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x) :
    print(x*10/100 + x)
        

def maas_alt(x) :
    print(x*20/100 + x)
    
for i in maaslar :
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break ve continue

maaslar = [8000,5000,2000,1000,3000,7000,4000]        

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar :
    if i == 3000 :
        print("İşlem kesildi")
        break
    print(i)


#continue

for i in maaslar :
    if i == 3000 :
        continue
    print(i)
    




    








    
    