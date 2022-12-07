import os
import string

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    buffer = ""

    line = lines[0]

    i = 1

    search_size = 14

    for c in line:
        
        if len(buffer) == search_size:
            buffer = buffer[1:search_size] + c
        else:
            buffer = buffer + c

        if len(set(buffer)) == search_size:
            print(i)
            break

        i += 1

