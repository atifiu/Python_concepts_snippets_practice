#Using nested list comprehension

data = [[7, 9 ,12],[1, 43], [1415, -25, 12]]
result = [num for sublist in data for num in sublist if num > 10]
print(result)

#Using nested loops

result = []
for sublist in data:
    for num in sublist:
        if num > 10 :
            result.append(num)
print(result)