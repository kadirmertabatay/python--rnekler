bas=input('başlangıç değerini giriniz : ')
bitis=input('bitiş değerini giriniz : ')
sayi=input('sayı giriniz : ')


print(sayi+"sayısına bölüne bilenler")
for i in range (int(bas),int(bitis)+1):
    if(i%int(sayi)==0):
        print(i)
