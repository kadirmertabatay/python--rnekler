def fakteriyel(sayı):
    f=1
    if(sayı==1 or sayı==0):
        print(sayı)
    else:
        while(sayı>0):
            f*=sayı
            sayı-=1

    print(f)


fakteriyel(4)