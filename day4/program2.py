size_lst = int(input('Enter size of tuple-list: '))
size_tup = int(input('Enter size of tuples: '))
lst = list()
for i in range(size_lst):
    print(f'Enter tuple-{i} elements separated by space: ',end='')
    tup = tuple(map(int, input().split()[:size_tup]))
    lst.append(tup)
ind = int(input('Enter index to sort tuple-list: '))
pos = ind-1
for i in range(size_lst-1):
    for j in range(i+1,size_lst):
        if lst[i][pos]>lst[j][pos]:
            lst[i],lst[j] = lst[j],lst[i]
print(lst)
