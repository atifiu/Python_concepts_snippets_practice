### Interview asked in Apple 2024 Jan
# Replace spaces in string with hyphen"-" and if multiple spaces between words then only one 
# hyphen should be present and trailing and leading hyphens should not be present"

def replace_spaces(string):
    # split has default of space otherwise we can pass character based on which split should be done. Split returns
    # list of values
    # join will take iterable and join it based on seperator provided
    return "-".join(string.split())

print(replace_spaces(" My name is  John Doe "))
print(replace_spaces("My      name is  John Doe"))
