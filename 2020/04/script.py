import re

if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()
    lines = ''.join(lines)

    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_list = []
    invalid = []
    reason = ''

    passports = lines.split('\n\n')
    n_valid = 0
    passport = passports[len(passports)-1]
    for passport in passports:
        passport_field_tags = []
        passport_field_values = []
        passport_lines = passport.split('\n')
        passport_line = passport_lines[0]
        for passport_line in passport_lines:
            passport_fields = passport_line.split(' ')
            for passport_field in passport_fields:
                keyvalue = passport_field.split(':')
                if len(keyvalue) == 2:
                    passport_field_tags.append(keyvalue[0])
                    passport_field_values.append(keyvalue[1])

        valid = True
        for req_field in req_fields:
            if not (req_field in passport_field_tags):
                reason = 'not all required tags'
                valid = False
                break

        for i in range(len(passport_field_tags)):
            key = passport_field_tags[i].strip()
            value = passport_field_values[i].strip()
            if key == 'byr':
                if not ((len(value) == 4) & (int(value) >= 1920) & (int(value) <= 2002)):
                    reason = 'wrong byr'
                    valid = False
                    break
            if key == 'iyr':
                if not ((len(value) == 4) & (int(value) >= 2010) & (int(value) <= 2020)):
                    reason = 'wrong iyr'
                    valid = False
                    break
            if key == 'eyr':
                if not ((len(value) == 4) & (int(value) >= 2020) & (int(value) <= 2030)):
                    reason = 'wrong eyr'
                    valid = False
                    break
            if key == 'hgt':
                if len(value) > 2:
                    unit = value[-2:]
                    number = int(value[:-2])
                    if not (unit in ['cm', 'in']):
                        reason = 'wrong unit'
                        valid = False
                        break
                    if unit == 'cm':
                        if not ((number >= 150) & (number <= 193)):
                            reason = 'wrong cm length'
                            valid = False
                            break
                    if unit == 'in':
                        if not ((number >= 59) & (number <= 76)):
                            reason = 'wrong in length'
                            valid = False
                            break
                else:
                    reason = 'hgt to short'
                    valid = False
            if key == 'hcl':
                if value[0] != '#' or any([c not in '0123456789abcdef' for c in value[1:]]):
                    reason = 'invalid hex'
                    valid = False
            if key == 'ecl':
                if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    reason = 'invalid ecl'
                    valid = False
            if key == 'pid':
                if not ((len(value) == 9) & (value.isdigit())):
                    reason = 'invalid pid'
                    valid = False

        if valid:
            valid_list.append((passport, reason))
            n_valid += 1
        else:
            invalid.append((passport, reason))

    print(n_valid)
