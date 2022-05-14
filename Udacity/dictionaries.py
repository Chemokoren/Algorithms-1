"""
You need to add the cities listed below by modifying the structure.
Then, you should print out the values specified by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia']={'India':['Bangalore']}
locations['North America']['USA'].append("Atlanta")
locations['Africa']={'Egypt':['Cairo']}
locations['Asia']['China']=["Shanghai"]

for countries, cities in locations['North America'].items():
    print("mine:", countries, cities)

print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

asian_cities =[]
for countries, cities in locations['Asia'].items():
    city_country = cities[0]+ " - " + countries 
    asian_cities.append(city_country)

print(2)
asia_sorted = sorted(asian_cities)
for city in asia_sorted:
    print(city)

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""