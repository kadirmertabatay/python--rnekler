a=5
def yaz():
    global a
    a=3
    print(a)

yaz()
print(a)
#normalde a değknenin değişmemsi gerekir ama global
# komutuyla globaldaki değeri çağararak değişiklik yapabiliyoruz