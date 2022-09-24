class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maaş, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman



class Yönetici(Çalışan):#kalıtımı bu şekilde sınıftan sınıfa şekilde yapıyoruz

    def __init__(self, isim, maaş, departman, kişi_sayısı):
        super().__init__(isim, maaş,departman)
#burada kullanış olduğumuz super kalıtım aldığımız initi bir daha yazmak yerine direkt olarak bize ulaştırıyor
        print("Yönetici sınıfının init fonksiyonu")
        self.kişi_sayısı = kişi_sayısı  #burada ise yönetici sınıfına özel bir özellik tanımlıyoruz


    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maaş, self.departman,self.kişi_sayısı))


    def zam_yap(self, zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
