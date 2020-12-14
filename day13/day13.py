def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    data = parseData()
    departureTime = int(data[0])
    busFrequency = data[1].split(',')
    minutesWaited = []

    for bus in busFrequency:
        if bus == 'x':
            minutesWaited.append(departureTime)
        else:
            minutesWaited.append(int(bus) - (departureTime % int(bus)))
    
    
    minWait = min(minutesWaited)
    print(int(busFrequency[minutesWaited.index(minWait)]) * minWait)


if __name__ == "__main__":
    main()
