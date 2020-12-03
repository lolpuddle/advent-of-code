nums = []
with open('input.txt') as f:
    nums = [int(line.rstrip()) for line in f]

for i, num in enumerate(nums):
    target = 2020 - num
    differences = {}
    for val in range(len(nums)):
        local_num = nums[val]
        diff = target - local_num
        if local_num in differences:
            print(local_num * differences[local_num] * num)
        else:
            differences[diff] = local_num
    