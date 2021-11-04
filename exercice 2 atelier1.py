def convertir(n):
    if n == 0:
        return 0
    else :
        return ((n%2)+ (10*convertir(n//2)))
n= int(input('entrer votre nombre svp' ))
print(convertir(n))
