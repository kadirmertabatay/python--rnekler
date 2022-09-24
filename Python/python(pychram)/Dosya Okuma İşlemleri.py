"""
try:
    file = open("bilgiler2.txt","r",encoding= "utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı....")

    olmayan dosyayı okuyamayacağımızdan dolayı böyle hata yakalayabiliriz

"""

file=open("C:/yazılım/python/python(pychram)/bilgiler2.txt","r",encoding= "utf-8")
#r komutu okuma işlemi yapmamızı sağlar

for i in file:
    print(i,end="")#end=""  yazma sebebimiz fazladan oluşan bboşluklaraı yok etmek
file.close()

#********************************************************


file = open("bilgiler2.txt","r",encoding="utf-8")

icerik = file.read()#read ile

print("Dosya İçeriği:\n",icerik,sep ="")

file.close()

"""
1. Okuma : Dosya İçeriği:
Mustafa Murat Coşkun
Mehmet Gençol
Oğuz Artıran
Serhat Say
Mert Erarslan

2. Okuma : Dosya İçeriği:

örnekte görüldüğü gibi  2. okumada boş geliyor çünkü 1.okuma sayfa sonunda bitiyor 

"""

#**************************************************************


""""
file = open("bilgiler.txt","r",encoding="utf-8")
print(file.readline())

tek satır okuma gerçekleştirir

"""

file = open("bilgiler2.txt","r",encoding="utf-8")
print(file.readlines())
file.close()
#['Kadir Mert Abatay\n', 'Hurşit Efe Abatay\n', 'Semiha Abatay\n', 'Murat abatay'] bu şekilde dizi olarak yazar
