def toplama (*a):
    print(a)

toplama(1,23,4)

#yukarıda gördüğümğüz paretmere sayısını esnek bir şekilde kullananbiliriz ve bir demet(dizi) şeklinde tutulur

def topla(*b):
    t=0
    for i in b:
        t+=i
    print(t)

topla(23,45,56)

#görüldüğü gibi kaç tane parametre alsığını söylemeden esnek bir şekilde kullanım sağlamış olabiliriz

def selamla(İsim="İsimsiz"):
    print("Selam",İsim)

selamla()
selamla("kadir")

#normal şartlarda kullanılan parametreye istenilen değer
#verilmesse hata verirdi ancak parametreye başlangıç değeri vererek bu hatayı ortadan kaldıra biliyoruz