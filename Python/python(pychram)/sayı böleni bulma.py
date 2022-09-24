def bölen(sayı):
    a=[]
    for i in range(1,sayı+1):
        if(sayı%i==0):
            a.append(i)
    print(a)



while True:
   sayı = input("Lütfen Sayı giriniz :")
   if(sayı=="q"):
       print("program sonlandırılıyor")
       break
   bölen(int(sayı))


