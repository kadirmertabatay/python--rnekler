file = open("C:/yazılım/python/python(pychram)/bilgiler.txt","w",encoding="utf-8")
#açma ve yeniden oluşturma kipi olarak w kullanılır
#eğer dosya kayıtlıysa içindeki bligler gider ve yeni dosya oluşturur

file.write("Kadir Mert Abatay\n")

file.close()

#************************************************************

file = open("bilgiler.txt","a",encoding="utf-8")
#a kipi w farklı olarak var olanı yeniden açar

file.write("Hurşit efe Abatay\n")
file.write("Semiha Abatay\n")
