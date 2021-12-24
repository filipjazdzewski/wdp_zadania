import countrydb_utils as cdb

countries = []

countries.append(cdb.add_country('Poland', 38))
countries.append(cdb.add_country('Germany', 84))
countries.append(cdb.add_country('France', 67))

cities = []
cities.append(cdb.add_city('Warsaw', 2))
cities.append(cdb.add_city('Berlin', 3))
cities.append(cdb.add_city('Paris', 3.5))

print(countries)
print(cities)