def reverse(nums):
    num2= nums.copy()
    n = len(nums)-1 #correct max index 
    for i in range(0, len(nums)): #0,1,2,3,4...n-1 range is excludes the last number 
        num2[i] = nums[n-i]
    return num2
d = [2,3,4,5,6]
print(reverse(d))