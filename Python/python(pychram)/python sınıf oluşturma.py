class bilgisayar():
    marka="HP"
    ekran_kartı="RTXX 3060"
    ram="32 GB"
    islemci="i7"

bilgisayar1=bilgisayar()
bilgisayar2=bilgisayar()
print(bilgisayar.marka)
print(bilgisayar.ram)


#***********__init__*****************
#__init__ sayesinde veri girşleri yaparak birden fala o sınıfa ait farklı değerler kullana biliyoruz
class bilgisayarlar():
    def __init__(self,marka="marka yok",ekran_kartı="Ekran kartı yok",ram="ram yok",islemci="islemci yok"):
        self.marka = marka
        self.ekran_kartı = ekran_kartı
        self.ram = ram
        self.islemci=islemci

bilgisayarlar1=bilgisayarlar("dell","3070","16","i9")

print(bilgisayarlar1.marka)