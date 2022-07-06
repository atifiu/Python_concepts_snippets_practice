from pipe import where, select
list1 = [2, 4, 9, 10, 20]
new_list = list(
                list1 | # source list on which operation to be performed
                where (lambda x: x >= 10) | # filtering the list i.e only values euqal or greater than 10
                select(lambda x : x * 2) # performing the operation on each element of filtered list
                )
print(new_list)