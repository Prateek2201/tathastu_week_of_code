s = input()
lst = list(s)
lng = len(s)
def permutation(s,l,u):
    if l==u:
        str1=''
        print(str1.join(s))
    else:
        for i in range(l,lng):
            s[i],s[l] = s[l],s[i]
            permutation(s,l+1,u)
            s[i],s[l] = s[l],s[i]
permutation(lst,0,lng-1)
