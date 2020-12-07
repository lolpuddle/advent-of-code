def parseData():
    data = []
    group = []
    with open('input.txt') as f:
        for line in f:
            lineData = line.rstrip()
            if len(lineData) > 0:
                group.append(lineData)
            else:
                if len(group) == 0:
                    pass
                data.append(group)
                group = []
    
    if len(group) > 0:
        data.append(group)
    return data

def main():
    data = parseData()
    sumOfCounts = 0

    for group in data:
        dictOfCharacters = defaultdict(int)
        overlap = group[0]
        for i in range(1, len(group)):
            overlap = ''.join(set(overlap).intersection(group[i]))
        sumOfCounts += len(overlap)
    print(sumOfCounts)


if __name__ == "__main__":
    main()
