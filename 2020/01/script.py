
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    for i in range(len(lines) - 2):
        var1 = int(lines[i])
        for j in range(i, len(lines) - 1):
            var2 = int(lines[j])
            for k in range(j, len(lines)):
                var3 = int(lines[k])
                if var1 + var2 + var3 == 2020:
                    print(var1 * var2 * var3)
                    quit()