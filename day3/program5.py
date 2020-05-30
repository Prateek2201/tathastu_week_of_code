n1 = int(input('Enter size of list_1: '))
print('Enter elements separated by space: ',end='')
lst1 = list(map(int,input().split()))
n2 = int(input('Enter size of list_2: '))
print('Enter elements separated by space: ',end='')
lst2 = list(map(int,input().split()))
lst=list()
for i in lst1:
    if i in lst2:
        lst.append(i)
print(lst)
