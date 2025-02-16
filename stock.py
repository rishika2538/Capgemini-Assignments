# initial_stock = {"apple": 50,"banana": 100,"orange": 75}
# sold_item = {"apple": 10, "banana": 20, "orange": 15}
# calculate the current stock and display current stock

initial_stock = {"apple": 50, "banana": 100, "orange": 75}
sold_item = {"apple": 10, "banana": 20, "orange": 15}
current_stock = {}
for item in initial_stock:
    if item in sold_item:
        current_stock[item] = initial_stock[item] - sold_item[item]
    else:
        current_stock[item] = initial_stock[item]

for item, quantity in current_stock.items():
    print(f"current stock is: {item}: {quantity}")
