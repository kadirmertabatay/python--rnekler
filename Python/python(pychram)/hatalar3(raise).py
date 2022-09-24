def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]

