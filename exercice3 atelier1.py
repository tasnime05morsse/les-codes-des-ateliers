def somme(a):
    if a==0:
        return 0
    else:
        return a + somme(a-1)
a=int(input("entrer le nombre"))
print('votre somme est ',somme(a))