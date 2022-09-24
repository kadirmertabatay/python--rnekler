class yazılımcı:
    def __init__(self,isim,soy_isim,numara,maas,diller):
        self.isim=isim
        self.soy_isim=soy_isim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileri_göster(self):
        print("""
        Yazılımcı Özellikleri
        
        isim : {}
        
        Soyisim : {}
        
        Numara : {}
        
        Maaş : {}
        
        Bilinen Diller : {}
        
        """.format(self.isim,self.soy_isim,self.soy_isim,self.numara,self.maas,self.diller))

    def zam_yap(self,zam_miktarı):
          self.maas+=zam_miktarı
          print("zam yapıldı")

    def dil_ekle(self,yeni_dil):
          self.diller.append(yeni_dil)
          print("Dil eklendi")
