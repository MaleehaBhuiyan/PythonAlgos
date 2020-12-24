# Iterative Binary Search 
# Given a list and a target, determine if the target is present in the list 

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 28 

def binary_search_iterative(target, data):
    low = 0 
    high = len(data) - 1 

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True 
        elif target < data[mid]:
            high = mid - 1 
        else: 
            low = mid + 1 
    return False 

