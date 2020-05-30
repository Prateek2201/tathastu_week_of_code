n = int(input('Enter size of list: '))
lst = list(map(int,input().split()[:n]))
def least(lst):
    add = 1
    for i in lst:
        if add>=i:
            add += i
    return add
print(least(lst))
