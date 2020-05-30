n = int(input('Enter number of terms: '))
a,b = -1,1
for i in range(n):
    c = a+b
    print(c,end=' ')
    a,b = b,c
