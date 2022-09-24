kelime = input("Cümle Giriniz: ")
sesliHarfSayisi = 0
for c in kelime:
 if c == "A" or c == "a" or c == "E" or c == "e" \
 or c == "I" or c == "ı" or c == "İ" or c == "i" \
 or c == "O" or c == "o" or c == "Ö" or c == "ö" \
 or c == "U" or c == "u" or c == "Ü" or c == "ü":
#burada kullanılan or yapısı yada işlemi görmekte
#eğer or yapısı kullanırken alt satıra geçmek için \ ifadesi kullanılır
   print(c, ",", sep=" ", end=" ")
   sesliHarfSayisi += 1
print(" (", sesliHarfSayisi, "sesli harf vardır)", sep=" ")