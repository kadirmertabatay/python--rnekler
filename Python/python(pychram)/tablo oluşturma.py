sayi=int(input('lütfen tablo ölçütünü giriniz : '))

for satir in range (1,sayi+1):
    print("")
    for sütün in range(1,sayi+1):
        h=satir*sütün
        print("{0:4}".format(h),end="")
