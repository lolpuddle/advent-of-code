policies = []
with open('input.txt') as f:
    policies = [line.rstrip() for line in f]

validPasswords = 0

for line in policies:
    parts = line.split(" ")
    lowerBound = int(parts[0].split("-")[0])
    upperBound = int(parts[0].split("-")[1])
    character = parts[1][0]
    password = parts[2]

    if lowerBound <= password.count(character) <= upperBound:
        validPasswords += 1

print(validPasswords)