"""
binary search works on sorted arrays.
its time complexity is O(log n).
binary_recursion and binary_loop functions are two alternative ways to find element index, 
binary_recursion uses recursion and binary_loop uses while loop
both takes arguments target (element to find in the given array), arr (array itself), 
low, high(low and high are start and end index of array respectively - get adjusted in the function logic for the array parts)
returns -1 if target element not found in the array else the index of the target element in the array
"""

def binary_recursion(target, arr, low, high):
    if low > high:
        return -1
    # mid = (low + high)//2
    mid = low + (high-low)//2
    # print(mid, low, high)
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_recursion(target, arr, low, mid-1)
    else:
        return binary_recursion(target, arr, mid+1, high)


def binary_loop(target, arr, low, high):
    target_index = -1
    while low <= high:
        mid = low + (high-low)//2
        if target == arr[mid]:
            target_index = mid
            break
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return target_index
        

arr = [1,2,3,4,5,6]
# target = 1
# print(binary_recursion(target, arr, 0, len(arr)-1))

for target in range(-10, 10):
    # target_index = binary_recursion(target, arr, 0, len(arr)-1)
    target_index = binary_loop(target, arr, 0, len(arr)-1)
    print(target, target_index)
