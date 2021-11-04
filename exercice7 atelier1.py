# fonction qui donne l’inverse d’une chaine
def inverse(str1):
    rstr= ""
    t = len(str1)

    while t > 0:
      rstr += str1[t-1]
      t = t - 1
    return rstr
# demander a l utilisateur de saisir une chaine
str1=str(input("votre chaine"))
# l’appel de la fonction
print(inverse(str1))


