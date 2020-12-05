import re


def parsePassportData():
    passports = []
    user = []
    with open('input.txt') as f:
        for line in f:
            data = line.rstrip()
            if len(data) > 0:
                user += data.split(' ')
            else:
                if len(user) == 0:
                    pass
                passportAsDict = {}
                for item in user:
                    key, value = item.split(':')
                    passportAsDict[key] = value
                passports.append(passportAsDict) 
                user = []

    # Hacky last line add
    passportAsDict = {}
    for item in user:
        key, value = item.split(':')
        passportAsDict[key] = value
    passports.append(passportAsDict)
    return passports

mandatoryKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
rules = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'hgt': [(150, 193), (59, 76)], #cm, in
    'hcl': '^#(?:[0-9a-fA-F]{3}){1,2}$',
    'pid':  '^([0-9]{9})$'
    'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
}
def validatePassport(passport):
    for ruleKey, ruleValue in rules.items():
        if ruleKey not in passport.keys():
            return False
            
        if ruleKey in ['byr', 'iyr', 'eyr']:
            if not (ruleValue[0] <= int(passport[ruleKey]) <= ruleValue[1]):
                return False

        elif ruleKey in ['hcl', 'pid']:
            if not (re.search(ruleValue, passport[ruleKey])):
                return False

        elif ruleKey == 'ecl':
            if passport[ruleKey] not in ruleValue:
                return False

        elif ruleKey == 'hgt':
            value = passport[ruleKey]
            if not ('in' in value or 'cm' in value):
                return False
            if value[-2:] == 'cm':
                if not (ruleValue[0][0] <= int(value[:-2]) <= ruleValue[0][1]):
                    return False
            else:
                if not (ruleValue[1][0] <= int(value[:-2]) <= ruleValue[1][1]):
                    return False
    return True

def main():
    validPassports = 0
    passports = parsePassportData()
    for passport in passports:
        if validatePassport(passport):
            validPassports += 1
    print(validPassports)

if __name__ == "__main__":
    main()
