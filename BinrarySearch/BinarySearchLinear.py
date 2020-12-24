# Given a list and a target, determine if the target is present in the list 

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 28 


# Linear search 
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False 
