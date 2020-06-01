n=int(input('Enter size of list: '))
print('Enter elements of list seprated by space')
l=list(map(int,input().split()))
for i in range(len(l)-1):
    l[i]=max(l[i+1:])
print(l)
