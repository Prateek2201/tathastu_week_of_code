for i in range(1,6):
    for j in range(1,11):
        if(j<=6-i or j>=5+i):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
for i in range(1,6):
    for j in range(1,11):
        if(j<=i or j>=11-i):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
