sayı =(input("Lütfen sayınızı giriniz : "))

sayac=0

for i in range(len(sayı)):
   a=int(sayı[i])
   b=len(sayı)
   h=a**b
   sayac+=h
if(sayac==int(sayı)):
    print("girilen sayı armstrog sayıdır")
else :
    print("girilen sayı armstrog sayı değildir")

print(sayac)