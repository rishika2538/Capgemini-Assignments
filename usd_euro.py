def price_usd():
    PricesList_inr =[3000,56000,45000,2300]
    usd=map(lambda x:x*0.12,PricesList_inr)
    print(list(usd))
price_usd()

def price_euro():
    PricesList_inr =[3000,56000,45000,2300]
    euro=map(lambda x:x*0.011,PricesList_inr)
    print(list(euro))
price_euro()