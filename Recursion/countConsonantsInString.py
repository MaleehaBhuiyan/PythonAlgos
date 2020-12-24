# given a string, count the number of consonants 
# A letter that is not a, e, i, or u 


str_one = "Maleeha"
str_two = "loves"
str_three = "GumDrops"

#iterative 

def find_consonant_iterative(str):
    i = 0 
    count = 0 
    while i < len(str):
        if str[i] not in ["a","e","i","o","u"]:
            count += 1
            i+=1
        else:
            i+=1
    return count  


print(find_consonant_iterative(str_one))



# recursive 

def find_consonant_recursive(str, count = 0):
    newCount = count 
    if len(str) == 0:
        return count 
    else:
        if str[0] not in ["a","e","i","o","u"]:
            newCount+=1
        return find_consonant_recursive(str[1:], newCount)  

print(find_consonant_recursive(str_one))