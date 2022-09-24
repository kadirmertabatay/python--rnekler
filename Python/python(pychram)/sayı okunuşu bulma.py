birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10 #onluğa tam böler mesela 37//10=3

    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))

print(okunus(sayı))