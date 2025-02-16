# calculate count the item frequency from the below products and store it in dictionary

products = "yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
product_list = products.split()
frequency = {}
for product in product_list:
    if product in frequency:
        frequency[product] += 1
    else:
        frequency[product] = 1
print(frequency)