countries = ['india', 'us','uk', 'australia']
print(countries)
new_countries=[country.upper() for country in countries]
print(new_countries)
new_countries=list(map(str.upper, countries))
print(new_countries)
new_countries=list(map(lambda x: len(x), countries))
print(new_countries)

value = (lambda a, b: a*b)(5, 4) - True
print(value)

new_countries=[(lambda x: x.upper())(country) for country in countries]
print(new_countries)
