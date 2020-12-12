from copy import deepcopy

def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def checkSitDown(i, j, seats):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for x, y in directions:
        if (len(seats) > i + x >= 0) and (len(seats[0]) > j + y >= 0):
            if seats[i + x][j + y] == '#':
                return False
    return True

def checkGetUp(i, j, seats):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    numberOfSeated = 0
    for x, y in directions:
        if (len(seats) > i + x >= 0) and (len(seats[0]) > j + y >= 0):
            if seats[i + x][j + y] == '#':
                numberOfSeated += 1
    return numberOfSeated >= 4

def seatTransform(seats):
    tempSeats = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == 'L':
                if checkSitDown(i, j, seats):
                    tempSeats[i] = tempSeats[i][:j] + '#' + tempSeats[i][j + 1:]
            elif seats[i][j] == '#':
                if checkGetUp(i, j, seats):
                    tempSeats[i] = tempSeats[i][:j] + 'L' + tempSeats[i][j + 1:]
    return tempSeats

def main():
    seats = parseData()
    newSeats = seatTransform(seats)
    while newSeats != seats:
        seats = newSeats
        newSeats = seatTransform(newSeats)

    seatsTaken = 0
    for i in range(len(newSeats)):
        for j in range(len(newSeats[0])):
            if seats[i][j] == '#':
                seatsTaken += 1
    print(seatsTaken)


if __name__ == "__main__":
    main()
