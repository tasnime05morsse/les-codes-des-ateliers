my_liste =[11, 45, 8, 23, 14, 12, 78, 45, 89]
liste_1=[]
liste_2=[]
liste_3=[]
l=int(len(my_liste)/3)
for i in range(l):
    liste_1.append(my_liste[i])
for i in range(l,l*2):
    liste_2.append(my_liste[i])
for i in range(l*2,l*3):
    liste_3.append(my_liste[i])
liste_1.reverse()
liste_2.reverse()
liste_3.reverse()
print(liste_1, liste_2, liste_3)



