maas=input('maaşınızı giriniz : ')
zam=input('zam oranını giriniz : ')
maashesap=float(maas)*float(zam)/100
yenimaas=float(maas)+float(maashesap)

print('zamlı maaş oranınız : '+format(yenimaas))