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
        setOfCharacters = []
        for answer in group:
            for character in answer:
                if character not in setOfCharacters:
                    setOfCharacters.append(character)
                    sumOfCounts += 1
    print(sumOfCounts)


if __name__ == "__main__":
    main()
