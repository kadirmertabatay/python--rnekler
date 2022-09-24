try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError: #özel olarak hataları böyle belirtiriz
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally: #finally hata olsada olmasada çalışır
    print("Her durumda çalışıyorum.")