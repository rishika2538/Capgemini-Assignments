def product():
    products = [
        {"name": "Laptop", "price": 92000},
        {"name": "Smartphone", "price": 48000},
        {"name": "Tablet", "price": 20000},
        {"name": "Monitor", "price": 8000}
    ]
    pro=sorted(products,key=lambda x:(x["price"],x["name"]))
    print(pro)
product()