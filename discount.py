#Apply a 20% discount to products costing more than $100 and return the updated price
def discount():
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Headphones", "price": 80},
        {"name": "Smartphone", "price": 700},
        {"name": "Monitor", "price": 150}
    ]
    more=filter(lambda x:x["price"]>100,products)
    discount=map(lambda x:x["price"]*0.8,more)  
    print(list(discount))
discount()