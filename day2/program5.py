k=4
for i in range(1,4):
    k -= 1
    for j in range(1,6):
        if(j<=7-2*i):
            if(j%2!=0):
                print(k,end='')
            else:
                print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(1,4):
    for j in range(1,6):
        if(j<=-1+2*i):
            if(j%2!=0):
                print(k,end='')
            else:
                print('*',end='')
        else:
            print(' ',end='')
    k += 1
    print()
