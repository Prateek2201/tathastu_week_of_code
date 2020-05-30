cost = float(input('Enter Cost Price: '))
sell = float(input('Enter Selling Price: '))
profit = sell-cost
new_price = 0.05*profit+sell
print('Selling price afetr increasing profit by 5%:',new_price)
