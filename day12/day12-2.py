import math

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    directions = parseData()
    allDirections = ['N','E','S','W']
    position = (0, 0)
    waypoint = (10, 1)
    for direction in directions:
        step = direction[:1]
        value = int(direction[1:])    
        if step == 'F':
            newX = position[0] + waypoint[0] * value
            newY = position[1] + waypoint[1] * value
            position = (newX, newY)
        elif step == 'L' or step == 'R':
            if step == 'L':
                yMultiplier = 1
                yChange = math.cos(value)
                if yChange < 0:
                    yMultiplier = -1
                xMultipler = 1
                xChange = math.sin(value)
                if xChange < 0:
                    xMultipler = -1
                if value == 180:
                    waypoint = (waypoint[0] * xMultipler, waypoint[1] * yMultiplier)
                else:
                    waypoint = (waypoint[1] * yMultiplier, waypoint[0] * xMultipler)
            if step == 'R':
                yMultiplier = 1
                yChange = math.sin(value)
                if yChange < 0:
                    yMultiplier = -1
                xMultipler = 1
                xChange = math.cos(value)
                if xChange < 0:
                    xMultipler = -1
                if value == 180:
                    waypoint = (waypoint[0] * xMultipler, waypoint[1] * yMultiplier)
                else:
                    waypoint = (waypoint[1] * yMultiplier, waypoint[0] * xMultipler)

        elif step == 'E':
            waypoint = (waypoint[0] + value, waypoint[1])
        elif step == 'W':
            waypoint = (waypoint[0] - value, waypoint[1])
        elif step == 'N':
            waypoint = (waypoint[0], waypoint[1] + value)
        elif step == 'S':
            waypoint = (waypoint[0], waypoint[1] - value)
        
    print(abs(position[0]) + abs(position[1]))

if __name__ == "__main__":
    main()
