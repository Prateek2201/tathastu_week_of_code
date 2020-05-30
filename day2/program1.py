n = int(input('Enter number: '))
def odd_even(n):
    print(f'{n} is even') if n%2==0 else print(f'{n} is odd')

def prime(n):
    flag = 0
    for i in range(2,n-1):
        if n%i==0:
            flag = 1
            break
    print(f'{n} is not prime') if(flag == 1) else print(f'{n} is prime')

def pallindrome(n):
    t = str(n)
    print(f'{n} is pallindrome') if(t == t[::-1]) else print(f'{n} is not pallindrome')

def armstrong(n):
    total = 0
    t = str(n)
    lng = len(t)
    for i in t:
        total += int(i)**lng
    print(f'{n} is armstrong') if(n == total) else print(f'{n} is not armstrong')
odd_even(n)
prime(n)
pallindrome(n)
armstrong(n)
