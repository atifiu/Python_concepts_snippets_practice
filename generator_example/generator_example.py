def my_generator():
    for row in open(r"C:\Users\Atif\Desktop\sql_notes.txt"):
        row = row.strip()
        print(row)
        data = {c: row.count(c) for c in set(row)}
        yield data
freq = {}
for item in my_generator():
    for k,v in item.items():
        freq[k] = freq.get(k, 0) + v
print(freq)
        #print(k, sep = ":", end = " ")
        #print(v)
