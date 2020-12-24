# Given a string, calculate the length of a string 

input_str = "LucidProgramming"


# iterative 

def str_length_iterative(str):
    for i in range(len(str)):
        count = 1 
        count += i 
    return count

print(str_length_iterative(input_str_3))


# recursive 

def str_length_recursive(str, count=0):
    newCount = count 
    if len(str) == 0:
        return count 
    else: 
        return str_length_recursive(str[1:], newCount+1)

print(str_length_recursive(input_str_3))


    