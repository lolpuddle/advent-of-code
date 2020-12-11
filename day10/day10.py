def parseData():
    data = []
    with open('input.txt') as f:
        data = [int(line.rstrip()) for line in f]
    return data

def main():
    adapters = parseData()
    adapters.sort()
    differences = [0, 0, 0]
    current = 0
    for adapter in adapters:
        if adapter in range(current + 1, current + 4):
            difference = adapter - current
            differences[difference - 1] += 1
            current = adapter
    differences[2] += 1
    print(differences[0] * differences[2])

if __name__ == "__main__":
    main()
