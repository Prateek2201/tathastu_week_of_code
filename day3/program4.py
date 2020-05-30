n = int(input('Enter number of elements to enter in list: '))
print('Enter elements separated by space: ',end='')
lst = map(int,input().split()[:n])
l1=list()
for i in lst:
    if i not in l1:
        l1.append(i)
print(l1)
