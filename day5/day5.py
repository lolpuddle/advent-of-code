import re


def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    tickets = parseData()
    maxValue = 0
    for ticket in tickets:
        strToConvert = ticket
        strToConvert = re.sub(r'B', '1', strToConvert)
        strToConvert = re.sub(r'F', '0', strToConvert)
        strToConvert = re.sub(r'R', '1', strToConvert)
        strToConvert = re.sub(r'L', '0', strToConvert)
        currentValue = int(strToConvert[:7], 2) * 8 + int(strToConvert[-3:], 2)
        maxValue = max(currentValue, maxValue)
    print(maxValue)

if __name__ == "__main__":
    main()
