baslangıc=input('başlangıç değerini giriniz  : ')

bitis=input('bitiş değerini giriniz : ')

print("çift sayılar")
for i in range(int(baslangıc),int(bitis)):
    if i%2==0:
        print(i)
print("tek sayılar")
for i in range(int(baslangıc),int(bitis)):
    if i%2!=0:
        print(i)

