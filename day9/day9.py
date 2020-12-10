from collections import deque

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data


def twoSum(nums, target):
    differences = {}
    for num in nums:
        diff = target - num
        if num in differences:
            return True
        else:
            differences[diff] = num
    return False

def main():
    nums = parseData()
    preamble = 25
    stack = deque([])
    
    # Initialize preamble
    for i in range(preamble):
        stack.append(int(nums[i]))

    i = preamble
    while i < len(nums) and twoSum(stack, int(nums[i])):
        stack.popleft()
        stack.append(int(nums[i]))
        i += 1

    print(nums[i])

if __name__ == "__main__":
    main()
