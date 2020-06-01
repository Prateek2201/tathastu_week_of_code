n = int(input('Enter size of dict: '))
dct = dict()
dct1 = dict()
for i in range(n):
    key = int(input(f'Enter key-{i} of dict: '))
    val = int(input(f'Enter val-{i} of dict: '))
    dct[key] = val
    if dct[key] not in list(dct1.values()):
        dct1[key] = val
print(dct1)
