from collections import defaultdict

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def countTotalBags(bagName, references):
    sum = 0
    children = references[bagName]
    for child, amount in children:
        sum += (countTotalBags(child, references) * amount) + amount
    return sum
        
# input structure comes as adjective + color _contains_ number + no bags or more bags
def main():
    rules = parseData()
    bagReferences = defaultdict(list)
    for rule in rules:
        words = rule.split(' ')
        parentBag = words[0] + words[1]
        if words[4] == 'no':
            continue
        for i in range(4, len(words), 4):
            childBag = words[i + 1] + words[i + 2]
            count = int(words[i])
            bagReferences[parentBag].append((childBag, count))

    sumOfBags = countTotalBags('shinygold', bagReferences)
    print(sumOfBags)

if __name__ == "__main__":
    main()
