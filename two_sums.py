"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. 
 
Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1]
 
Input: nums = [3,2,4], target = 6
"""

def find_sum(nums, target):
    ind1, ind2 = None, None
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                ind1, ind2 = i, j
                break
        if ind1 is not None and ind2 is not None:
            break
    return ind1, ind2


if __name__ == '__main__':
    # nums = [2,7,11,15]
    nums = [3,2,4]
    # target = 9
    target = 6
    res = find_sum(nums, target)
    print(list(res))
