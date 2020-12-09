def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    instructions = parseData()
    swaps = []
    i = 0
    while i < len(instructions):
        swapped = False
        seen = []
        i = 0
        value = 0
        while i < len(instructions) and i not in seen:
            operation = instructions[i].split(" ")[0]
            amount = int(instructions[i].split(" ")[1])
            seen.append(i)

            if operation == 'acc':
                value += amount
                i += 1
            elif operation == 'jmp':
                if not swapped and i not in swaps:
                    swapped = True
                    swaps.append(i)
                    i += 1
                    continue
                i += amount
                if i < 0:
                    i = 0
            else:
                i += 1
        
    print(value)


if __name__ == "__main__":
    main()
