def position(T, a):
    for i in range(len(MAT)):
        for j in range(len(MAT[0])):
            if a == MAT[i][j]:
                ni = i
                nj = j
                return ni, nj


MAT = [[2, 9, 1], [0, 5, 4], [-17, 3, -2]]
a = int(input("chercher un élément : "))
p = position(MAT, a)
print("la position  de  ", a, "dans la matrice : ", p)



