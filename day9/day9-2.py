def parseData():
    data = []
    with open('input.txt') as f:
        data = [int(line.rstrip()) for line in f]
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
    target = 69316178
    start = 0
    end = 0
    sumValue = 0

    while end < len(nums) and sumValue != target:
        sumValue = sum(nums[start:end])
        if sumValue < target:
            end += 1
        elif sumValue > target:
            start += 1

    contiguousSet = nums[start:end]
    print(min(contiguousSet) + max(contiguousSet))


if __name__ == "__main__":
    main()
