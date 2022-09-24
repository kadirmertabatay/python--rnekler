print(""""
*******HESAP İŞLEMLERİ********
 
     1.BAKİYE SORGOLAMA

     2.PARA YATIRMA

     3.PARA ÇEKME 
     
     Çımak için q ya basın
""")

bakiye=5000

while True :
   numara = input("işlem numaranızı giriniz : ")
   if (numara=="1"):
       print("Hesap bakiyeniz : ",bakiye)
   elif(numara=="2"):
       a=int(input("yatırıcağanız para miktarını giriniz : "))
       bakiye=bakiye+a
       print("güncel bakiye ",bakiye)
   elif(numara=="3"):
       c=int(input("Ytırıcağanız para miktarını giriniz : "))
       bakiye=bakiye-c
       print("Güncel bakiye ",bakiye)
   elif(numara=="q"):
       print("çıkış yapılmısştır")
       break