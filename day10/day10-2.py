def parseData():
    data = []
    with open('input.txt') as f:
        data = [int(line.rstrip()) for line in f]
    return data

def pathsToEnd(current, target, adapters, memorization):
    if current > target:
        return 0
    if current == target:
        return 1
    if current not in adapters and current != 0:
        return 0
    if current in memorization:
        return memorization[current]

    memorization[current] = (pathsToEnd(current+1, target, adapters, memorization) +
                            pathsToEnd(current+2, target, adapters, memorization) +
                            pathsToEnd(current+3, target, adapters, memorization))
    return memorization[current]

def main():
    adapters = parseData()
    adapters.sort()
    target = adapters[-1] + 3
    adapters = set(adapters)
    paths = pathsToEnd(0, target, adapters, {})
    print(paths)

if __name__ == "__main__":
    main()
