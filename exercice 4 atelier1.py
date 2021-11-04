def fibonacci(s):
    if s==0:
        return 0
    elif s==1:
        return 1
    else:
        return (fibonacci(s-1) + fibonacci(s-2))
s=int(input("entrez le nombre"))
for i in range (0,s):
    print( fibonacci(i) ,end=' ')
