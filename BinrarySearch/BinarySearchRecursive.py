# Recursive Binary Search 
# Given a list and a target, determine if the target is present in the list 

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 28 

def binary_search_recursive(data, target, low, high):
    if low > high: 
        return False 
    else: 
        mid = (low + high) // 2 
        if target == data[mid]:
            return True 
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1) 
        elif target > data[mid]:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_recursive(data, target, 0, len(data)-1))

    
