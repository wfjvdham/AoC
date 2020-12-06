

if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    n_valid = 0

    line = lines[0]
    line = "1-3 b: cdefg"
    for line in lines:
        parts = line.split()
        indexes = list(map(int, parts[0].split("-")))
        search = parts[1][0:-1]
        password = parts[2]

        if (int(password[indexes[0] - 1] == search) +
                int(password[indexes[1] - 1] == search) == 1):
            n_valid += 1

    print(n_valid)