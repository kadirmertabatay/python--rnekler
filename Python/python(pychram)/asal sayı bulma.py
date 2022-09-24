sayi=input('sayı giriniz : ')
s=0;
for i in range (2,int(sayi)):
    if(int(sayi)%i==0):
        s+=1
        break

if(s==0):
    print(sayi,"  asal sayı ")
else:
    print(sayi,"  asal sayı değil")