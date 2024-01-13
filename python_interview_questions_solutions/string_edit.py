## Interview question Dec 2023 Agoda: you have two strings and have to find if they are same and you are allowed to make one edit
## i.e. delete 1 char, insert 1 char or repalce 1 char. Return True if two strings are same else return False.

def check_string(string1, string2) -> bool:
    counter = 0
    flag = True
    #for i  in range(0, max(len(string1), len(string2))): 
    i = 0
    j = 0
    if abs(len(string1) - len(string2)) > 1:
        flag = False
    else:
        #print(min(len(string1), len(string2)))
        while i <= max(len(string1), len(string2)) -1:
            
           # print(f"{i},{j}")   
            
            if (i or j) == min(len(string1), len(string2)):
                # print(f"counter = {counter}")
                if counter == 0:
                    flag = True
                    break 
                elif counter >= 1:
                    #print(f"counter = {counter}")
                    if len(string1) == len(string2):
                        flag = True
                        break
                    else:
                        flag = False
                        break
            #print(string1[i], string2[j])
            if string1[i] == string2[j]:
                j += 1
                i += 1
                continue
            
            else:
                if len(string1) == len(string2):
                    counter += 1
                    i += 1
                    j += 1
                else:
                    if len(string1) < len(string2):
                        j += 1
                    else:
                        i += 1
                        #print(f"inside else {j}")
                if counter > 1:
                    flag = False
                    break
            
    return flag
            

print(check_string("abc", "abc")) # true
print(check_string("abcd", "abc")) # true
print(check_string("abxd", "abcd")) #true
print(check_string("abcd", "abxcd")) # true
print(check_string("abcde", "abc")) #false
print(check_string("axy", "abc")) # false
print(check_string("zxy", "abc")) # false
    