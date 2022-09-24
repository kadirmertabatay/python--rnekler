not1=input('1. notunuzu giriniz : ')
not2=input('2.notunuzu giriniz : ')
not3=input('3.notunuzu giriniz : ')

ortalama=(float(not1)+float(not2)+float(not3))/3

if(float(ortalama)>=50):

    print("geçtiniz")

elif(float(ortalama)<50):
    print("kaldınız")

print("Yazılı Ortalamanız"+format(ortalama))

