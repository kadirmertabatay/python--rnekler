from random import randint;

s=0
while True:
    rand = randint(1, 7)
    rand2 = randint(1, 7)
    print("zar1 : ",rand)
    print("zar2 : ",rand2)
    s+=1
    if(rand==rand2):
     print(s,". denemede zarlar çift geldi")
     break
