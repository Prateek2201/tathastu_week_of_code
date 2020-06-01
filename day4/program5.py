n = int(input('Enter the number of votes: '))
dct={}
for i in range(n):
    name = input('Enter name of candidate: ')
    if name not in dct.keys():
        dct[name] = 1
    else:
        dct[name] += 1
    max_votes = max(dct.values())
    max_votes_candidates = []
    for i in dct.keys():
        if dct[i]==max_votes:
            max_votes_candidates.append(i)
print(min(max_votes_candidates))
