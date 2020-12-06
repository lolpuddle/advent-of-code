import re

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    tickets = parseData()
    totalValue = 0
    maxValue = 0
    minValue = 999999999999
    for ticket in tickets:
        strToConvert = ticket
        strToConvert = re.sub(r'B', '1', strToConvert)
        strToConvert = re.sub(r'F', '0', strToConvert)
        strToConvert = re.sub(r'R', '1', strToConvert)
        strToConvert = re.sub(r'L', '0', strToConvert)
        currentValue = int(strToConvert[:7], 2) * 8 + int(strToConvert[-3:], 2)
        minValue = min(currentValue, minValue)
        maxValue = max(currentValue, maxValue)
        totalValue += currentValue

    seat = sum(range(minValue, maxValue + 1)) - totalValue
    print(seat)
    
if __name__ == "__main__":
    main()
