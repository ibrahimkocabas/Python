#NESNE YONELIMLI PROGRAMLAMA

#Sinif Ozellikleri

class VeriBilimci():
    bolum=''
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]
    
VeriBilimci.sql
VeriBilimci.deneyim_yili

#Sinif Orneklendirmesi

ali=VeriBilimci()

ali.sql
ali.bildigi_diller.append("Python")
ali.bildigi_diller

#Ornek Ozellikleri

class VeriBilimci():
    bolum=''
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=["R","PYTHON"]
    def __init__(self):
        self.bildigi_diller=[]

ali=VeriBilimci()
veli=VeriBilimci()

ali.bildigi_diller.append("Python")        
veli.bildigi_diller.append("R")  

ali.bildigi_diller
veli.bildigi_diller

VeriBilimci.bildigi_diller


#Ornek Methodları


class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum = ''
    def dil_ekle(self,yeni_dil) :
        self.bildigi_diller.append(yeni_dil)

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller


#Miras Yapiları (inheritance)

class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.Address=""
        
class DataScience(Employees):
        def __init__(self):
            self.Programming=""

veribilimci1 = DataScience()
veribilimci1.            

class Marketing(Employees):
        def __init__ (self):
            self.StoryTelling=""
            
mar1 = Marketing()
mar1.




















