def compteur(n):
    if n<10:
        return 1
    else:
        return 1 + compteur(n//10)
n=int(input("entrez votre nombre"))
print('les chiffres de votre nombre est' ,compteur(n))

