from collections import defaultdict

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def containsShinyGold(bag, bagReferences):
    if bag == 'shinygold':
        return True
    children = bagReferences[bag]
    for child in children:
        if containsShinyGold(child, bagReferences):
            return True
        
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
            bagReferences[parentBag].append(childBag)

    referencesToShinyGold = 0

    for bag, value in bagReferences.items():
        if containsShinyGold(bag, bagReferences):
            referencesToShinyGold += 1
    
    # accounting for the shinygold bag itself
    print(referencesToShinyGold - 1)

if __name__ == "__main__":
    main()
