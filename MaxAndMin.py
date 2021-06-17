def high_and_low(numbers):
    nums = numbers.split()
    maxInt = int(nums[0])
    minInt = int(nums[0])
    for num in nums[1:]:
        maxInt = max(maxInt, int(num))
        minInt = min(minInt, int(num))
    return f"{maxInt} {minInt}"