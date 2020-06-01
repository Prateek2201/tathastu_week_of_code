n=int(input('Enter number of houses'))
print('Enter values of houses seprated by space')
a=list(map(int,input('Enter values').split()))
if(a[0]>a[1]):
    high = [a[0],a[0]]
else:
    high = [a[0],a[1]]
for i in range(2,n):
    cost = 0
    for j in range(i-1):
        if(high[j]+a[i]>cost):
            cost = high[j]+a[i]
    high.append(cost)
print('Maximum stolen value:',high[-1])
