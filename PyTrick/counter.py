from collections import Counter

str = "hello world"
c = Counter(str)
print(c)

print(c.most_common(3))