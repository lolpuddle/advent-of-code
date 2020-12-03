policies = []
with open('input.txt') as f:
    policies = [line.rstrip() for line in f]

validPasswords = 0

for line in policies:
    parts = line.split(" ")
    positionOne = int(parts[0].split("-")[0]) - 1
    positionTwo = int(parts[0].split("-")[1]) - 1
    character = parts[1][0]
    password = parts[2]

    conditionOne = password[positionOne] == character
    conditionTwo = password[positionTwo] == character

    if conditionOne ^ conditionTwo:
        validPasswords += 1

print(validPasswords)