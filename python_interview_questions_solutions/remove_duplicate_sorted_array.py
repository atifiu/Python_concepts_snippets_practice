### Remove duplicate from sorted array/list

def remove_duplicate_sorted_list(list1:list[int]) ->list[int]:
    i = 0
    while i < len(list1):
        print(list1[i])
        if i <= len(list1) -2:
            if list1[i] == list1[i+1]:
                list1.remove(list1[i])
            else:
                i += 1
        else:
            i += 1
    return list1

print(remove_duplicate_sorted_list([1,1,1, 1,2,2,3,4,7,8, 8, 8, 9]))
print(remove_duplicate_sorted_list([1,1,1,1,2,2]))