#try / except / finally / raise

try:

    a = int("324234dsadsad")  # Burası ValueError hatası veriyor.
    print("Program burada")
except:  # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.

print("Bloklar sona erdi")



