#Define it using a hash table.
def TwoNumberSum(targetSum =10):
    array = [3,5,-4,8,11,1,-1,6]
    nums = {}
    for i in array:
        if targetSum - i in nums:
            return [targetSum - i, i]
        else:
            nums[i] = True
    return[]

#Define it using length
def TwoNumberSum2(targetSum = 10):
    array = [3,5,-4,8,11,1,-1,6]
    for i in range(len(array) - 1):
        num1 = array[i]
        for j in range(i + 1, len(array) - 1):
            num2 = array[j]
            if num1 + num2 == targetSum:
                return[num1,num2]
    return[]

#Define it using math left and right equation
def TwoNumberSum3(targetSum = 10):
    array = [3,5,-4,8,11,1,-1,6]
    array.sort()
    left = 0
    right = len(array) - 1
    while left - right:
        total = array[left] + array[right]
        if targetSum == total:
            return[array[left], array[right]]
        elif total < targetSum:
            left += 1
        elif total > targetSum:
            right -= 1
    return[]

print(TwoNumberSum3())