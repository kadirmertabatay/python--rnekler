print("Çıkmak için q ya basın")

sayac=0
while True:
    sayı=input("Sayı giriniz : ")
    if(sayı=="q"):
        print(sayac)
        break
    sayac += int(sayı)