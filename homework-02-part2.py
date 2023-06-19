#Namu Sampath
#June 8, 2023
#homework 02, part 02

#part 02 - lists! 
countries = ["india","usa","morocco","switzerland","zambia","chile", "azerbaijan"]
for country in countries: 
    print(country)
#sort countries
sorted(countries)
#what's the first element on the list
print(countries[0])
#what's the second to last element on the list
print(countries[-2])
#delete one of the countries using its name
countries_2 = countries.remove("azerbaijan")
print(countries_2)
#convert countries to uppercase 
countries = ["india","usa","morocco","switzerland","zambia","chile", "azerbaijan"]
for country in countries: 
    print(country.upper())

#part 02 - dictionaries! 
tree = {'name': "Plumeria", 'common name': "frangipiani",
         'species':"plumeria rubra", 'age': 270, 'location name': "Central America",
         'latitude': 12.7690 , 'longtitude': -85.6024
}
print(tree['name'], "is a", tree['age'] , "years old tree that is in" , tree['location name'])
#is the tree south of NYC? 
#yes
print("The" , tree['name'], "in", tree['location name'], "is south of NYC")

#how old is the user? 
user_age = int(input("How old are you?"))
tree_age = int(tree['age'])
if user_age > tree['age']:
    print("You are", int(user_age - tree_age), "years older than tree['name']")
if user_age < tree['age']:
    print(tree['name'], "was", int(tree_age - user_age), "years old when you were born.")

#dictionaries part 02 
places = {'city1': "Moscow", 'latitude1': int(55.7558), 'longitude1': int(37.6713), 
          'city2': "Tehran", 'latitude2': int(35.7219), 'longitude2': int(51.3347), 
          'city3': "Falkland Islands", 'latitude3': int(-51.7963), 'longitude3': int(-59.5236), 
          'city4': "Seoul", 'latitude4': int(37.5519), 'longitude4': int(126.9918), 
          'city5': "Santiago", 'latitude5': int(-33.4489), 'longitude5': int(-70.6693)
}
#looping through list, which cities are above the equator, which are below?
#equator is at 0 degrees latitude
#if latitude is positive, city is north of equator
#if latitude is negative, city is south of equator


#Moscow is above the equator because the latitude is a positive number.
if (places['latitude1']) > 0: 
    print(places['city1'], "is above the equator"), 
#Tehran is above the equator because the latitude is a positive number.
if (places['latitude2']) > 0: 
    print(places['city2'], "is above the equator"),
#The Falkland Islands are below the equator. 
if (places['latitude3']) < 0: 
    print(places['city3'], "is below the equator.", "The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
#Seoul is above the equator because the latitude is a positive number.
if (places['latitude4']) > 0: 
    print(places['city4'], "is above the equator" ),
#Santiago is below the equator because its latitude is a negative number.
if (places['latitude5']) < 0: 
    print(places['city5'], "is below the equator")

if (places['latitude1']) > tree['latitude']: 
    print(places['city1'], "is north of the location of", tree['name']), 
if (places['latitude2']) > tree['latitude']:
    print(places['city2'] , "is north of the location of", tree['name']),
if (places['latitude3']) < tree['latitude']:
    print("The" , places['city3'] , "are south of the location of", tree['name']),
if (places['latitude4']) > tree['latitude']:
    print(places['city4'] , "is north of the location of", tree['name']),
if (places['latitude5']) < tree['latitude']:
    print(places['city5'] , "is south of the location of", tree['name'])


    

    




