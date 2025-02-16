#You have a list of cities with their population data. Sort the cities in descending order of their population.
def city():
    cities = [
        {"name": "New York", "population": 8419600},
        {"name": "Los Angeles", "population": 3980400},
        {"name": "Chicago", "population": 2716000},
        {"name": "Houston", "population": 2328000}
    ]
    res=sorted(cities,key=lambda x:(-x["population"]))
    print(res)
city()
