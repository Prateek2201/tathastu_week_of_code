n = int(input('Enter size od dict: '))
dct={}
dct1={}
for i in range(n):
    key = int(input(f'Enter key-{i} of dict: '))
    val = int(input(f'Enter val-{i} of dict: '))
    dct[key] = val
    if dct[key] not in dct1.values():
        dct1[key] = val
print(dct1)
