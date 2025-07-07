def two_sum_recursive(nums, target, start=0):
    if start >= len(nums):
        return None
    for i in range(start + 1, len(nums)):
        if nums[start] + nums[i] == target:
            return (nums[start], nums[i])
    return two_sum_recursive(nums, target, start + 1)

# Example
nums = [2, 7, 11, 15]
target = 9
result = two_sum_recursive(nums, target)
print("Two Sum Pair:", result)
