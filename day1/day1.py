nums = []
with open('input.txt') as f:
    nums = [int(line.rstrip()) for line in f]

differences = {}
target = 2020

for num in nums:
    diff = target - num
    if num in differences:
        print(num * differences[num])
    else:
        differences[diff] = num