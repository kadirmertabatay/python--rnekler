from random import randint
rand = randint(1, 100)

while True:

    sayi=int(input('1 ile 100 arasında sayı tahmin ediniz(çıkış için 0) : '))
    if (sayi==0):
        print("oyunu iptal edniz")
        break
    elif(sayi>rand):
        print("Daha düşük söyle ")
    elif(rand>sayi):
        print("Daha yüksek söyle")
    elif(rand==sayi):
        print("doğru bildiniz")
        break




