travel = []
with open('input.txt') as f:
    travel = [line.rstrip() for line in f]

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
treesHit = [0, 0, 0, 0, 0]
for i in range(len(travel)):

    if travel[i][i%31] == '#':
        treesHit[0] += 1
    
    if travel[i][i*3%31] == '#':
        treesHit[1] += 1

    if travel[i][i*5%31] == '#':
        treesHit[2] += 1
    
    if travel[i][i*7%31] == '#':
        treesHit[3] += 1
    
    if (i*2 < len(travel)):
        if travel[i*2][i%31] == '#':
            treesHit[4] += 1

print(treesHit[0] * treesHit[1] * treesHit[2] * treesHit[3] * treesHit[4])