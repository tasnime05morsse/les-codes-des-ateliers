def factoriel(n):
    if n==0:
        return 1
    else:
        return n*factoriel(n-1)
s=0
x=5
for i in range (1,x+1):
    s=s+factoriel(i)/i
print(s)
