sifre="abc"
kullanıcı="23"

a=3

while(a>0):
    sifreg = input(" Şifrenizi Giriniz :")
    kullanıcıg = input("Kullanıcı Adını Girniz :")
    if(sifre==sifreg):
        if(kullanıcıg==kullanıcı):
            print("Giriş Başarılı")
            break
        else :
            print("şifre Hatalı",a,"deneme hakkı kaldı" )
    else:
        print("sifre hatalı",a,"deneme hakıkınız kaldı")
    a-=1
