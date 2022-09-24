bas=input('başlangıç değerini giriniz : ')
bitis=input('bitiş değerini giriniz : ')
toplam=0;

for i in range(int(bas),int(bitis)+1):
    toplam+=i

print(bas+"ile"+bitis+"arasındaki sayıların tooplamı"+format(toplam))

