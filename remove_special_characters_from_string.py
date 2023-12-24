import re
def remove_special_characters(input_string):
 
 result_string = ''.join(filter(str.isalnum, input_string))
 return result_string

print(remove_special_characters('abcd&*gshshs'))
print(remove_special_characters('atif'))
print(remove_special_characters('mohd atif'))

def remove_special_characters_regex(input_string):
 result_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
 return result_string

print(remove_special_characters_regex('abcd&*gshshs'))
print(remove_special_characters_regex('atif'))
print(remove_special_characters_regex('mohd atif3'))