def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    directions = parseData()
    allDirections = ['E','N','W','S']
    facing = 'E'
    position = (0, 0)
    for direction in directions:
        step = direction[:1]
        value = int(direction[1:])    
        if step == 'F':
            step = facing

        if step == 'L' or step == 'R':
            index = allDirections.index(facing)
            rotation = value/90
            if step == 'L':
                newIndex = (rotation + index) % len(allDirections)
                facing = allDirections[newIndex]
            if step == 'R':
                newIndex = (index - rotation + len(allDirections)) % len(allDirections)
                facing = allDirections[newIndex]
        elif step == 'E':
            position = (position[0] + value, position[1])
        elif step == 'W':
            position = (position[0] - value, position[1])
        elif step == 'N':
            position = (position[0], position[1] + value)
        elif step == 'S':
            position = (position[0], position[1] - value)
        
    print(abs(position[0]) + abs(position[1]))

if __name__ == "__main__":
    main()
