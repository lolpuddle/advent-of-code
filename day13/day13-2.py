def parseData():
    data = []
    with open('input.txt') as f:
        data = [line.rstrip() for line in f]
    return data

def main():
    data = parseData()
    busFrequency = data[1].split(',')
    lcm = 1
    startTime = 0
    relevantBuses = []
    for i, bus in enumerate(busFrequency):
        if bus == 'x':
            continue        
        relevantBuses.append((i, int(bus)))
    
    for offset, bus in relevantBuses:
        while (startTime+offset) % bus != 0:
            startTime += lcm
        lcm *= bus
    
    print(startTime)

if __name__ == "__main__":
    main()