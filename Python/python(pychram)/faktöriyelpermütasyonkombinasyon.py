print(""""------Menü------
         Faktöriyel.... 1
         Permütasyon... 2
         Kombinasyon... 3""")

f=1;
f2=1;
f3=1;


islemsayı=int(input("işleminiz sayısını seçin : "))

if(islemsayı==1):

    sayı=int(input('işlem yapacağınız sayıyı giriniz : '))
    for i in range(1,int(sayı)+1):
        f=f*i

    print("sonuç = "+format(f))





elif(islemsayı==3):

    n=input('p(n,k) n i giriniz : ')
    k=input('p(n,k) k yı giriniz : ')
    for i in range(1, int(n)+1):
       f = f * i

    for i in range(1, int(k)+1):
       f2 = f2 * i

    h=int(n)-int(k)
    for i in range(1,int(h)+1):
        f3=f3*i

    hesap=f/(f3*f2)
    print("işlem sonucu = "+format(hesap))






elif (islemsayı == 2):

    n = input('p(n,k) n i giriniz : ')
    k = input('p(n,k) k yı giriniz : ')
    for i in range(1, int(n)+1):
        f = f * i


    for i in range(1, int(k)+1):
        f2 = f2 * i




    hesap = f / f2
    print("işlem sonucu = " + format(hesap))
else:
    print("böyle bir seçim yok lütfen tekrar deneyiniz.")