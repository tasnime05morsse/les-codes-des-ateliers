liste_1=[3, 6, 9, 12, 15, 18, 21]
liste_2=[4, 8, 12, 16, 20, 24, 28]
liste=[]
elm=0
for i  in liste_1:
    if elm % 2 == 1:
        liste.append(i)
    elm+=1
elm=0
for i  in liste_2:
    if elm % 2 == 0:
        liste.append(i)
    elm+= 1
print(liste)



