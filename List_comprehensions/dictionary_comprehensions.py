# count the number of letters in each word
countries = ['india', 'us', 'uk', 'australia']
letter_count = {country: len(country) for country in countries}
print(letter_count)

#dictionary with count of total occurences of each element of the list
number_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 4, 4, 4]

occurence_count = {number:number_list.count(number) for number in number_list}
print(occurence_count)

#Using set for better performance
occurence_count = {number:number_list.count(number) for number in set(number_list)}
print(occurence_count)

#Using Counter to get the occurence of each element in a list
from collections import Counter
occurence_count = Counter(number_list)
print(occurence_count)
occurence_count = dict(occurence_count)
print(occurence_count)
print(type(occurence_count))
