def tri_bulle(tab):
    permuta = True
    a = 0
    while permuta == True:
        permuta = False
        a = a + 1
        for i in range(0, len(tab) - a):
            if tab[i] > tab[i + 1]:
                permuta = True
                tab[i], tab[i + 1] = tab[i + 1],tab[i]
    return tab
from array import *
tableau = array('i', [4,2,8,99,3,7,1])
print(tri_bulle(tableau))

