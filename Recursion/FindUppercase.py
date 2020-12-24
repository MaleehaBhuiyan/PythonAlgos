# Given a string, find the first uppercase character 
# Solve using both an iterative and recursion solution 

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

# Iterative 

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

# Iterative 

def find_uppercase_iterative(str):
    for i in range(len(str)):
        if str[i].isupper():
            return str[i]
    return "No Uppercase Character found"
    

print(find_uppercase_iterative(input_str_3)) 


# Recursive 

def find_uppercase_recursive(str):
    if len(str) == 0:
        return "No Uppercase Character found"
    if str[0].isupper():
        return str[0]
    return find_uppercase_recursive(str[1:])
    

print(find_uppercase_recursive(input_str_2))