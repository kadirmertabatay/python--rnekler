toplam = 0
durum = False
while not durum: #durumu kontrol eder ve dur true olana kadar döngü çalışır.
    deger = int(input("Lütfen pozitif tam sayı giriniz (Çıkış için 999):"))
    if deger < 0:
       print("Negatif değer girildi, ", deger, "degeri işleme alınmadı")
       continue
    if deger != 999:
        print("Eklenen değer", deger)
        toplam += deger
    else:
       durum = True
print("Toplam =", toplam)