### Interview question asked in Phrama company online interview using code signal app in Jan 2024
# Give a number find the different between multiple and sum of digits of that number

def get_difference(number):
    # split the number into list of digits using list comprehension
    list_number = [int(digit) for digit in str(number)]
    sum_number = sum(list_number) # we can easily get the sum of list using sum function
    multiple_number = 1
    # for multiplcation we will loop through the elements of list
    for digit in list_number:
        multiple_number = multiple_number * digit
    return multiple_number - sum_number

print(get_difference(12345))
    