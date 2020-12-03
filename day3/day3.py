travel = []
with open('input.txt') as f:
    travel = [line.rstrip() for line in f]

treesHit = 0
for i, line in enumerate(travel):
    # every 31 characters, the map pattern repeats
    if line[i*3%31] == '#':
        treesHit += 1

print(treesHit)
