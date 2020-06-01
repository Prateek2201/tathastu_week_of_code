n1 = int(input('Enter size of words: '))
print('Enter words separated by space: ')
word_arr = list(map(str, input().split()[:n1]))
n2 = int(input('Enter size of char: '))
print('Enter characters separated by space: ')
char_arr = list(map(str, input().split()[:n2]))
for word in word_arr:
    flag = 0
    for char in range(len(word)):
        if word[char] not in char_arr:
            flag = 1
            break
    if flag==0:
        print(word,end=' ')
