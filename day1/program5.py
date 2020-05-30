r1 = int(input('Runs scored by Player_1: '))
r2 = int(input('Runs scored by Player_2: '))
r3 = int(input('Runs scored by Player_3: '))
strike_1 = r1*100/60
strike_2 = r2*100/60
strike_3 = r3*100/60
print('***Player_1 Detail***')
print('Strike rate of Player_1:',strike_1)
print('Runs of Player_1 if he played 60 balls more:',r1*2)
print('max number of sixes Player_1 could hit:',r1//6)
print('***Player_2 Detail***')
print('Strike rate of Player_2:',strike_2)
print('Runs of Player_2 if he played 60 balls more:',r2*2)
print('max number of sixes Player_2 could hit:',r2//6)
print('***Player_2 Detail***')
print('Strike rate of Player_3:',strike_3)
print('Runs of Player_3 if he played 60 balls more:',r3*2)
print('max number of sixes Player_3 could hit:',r3//6)
