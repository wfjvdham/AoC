import os
import string

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        current = ()
        finish = ()
        min_steps = 9999999999
        finished_paths = 0

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == 'S':
                    current = (i, j)
                elif lines[i][j] == 'E':
                    finish = (i, j)

        path = [current]
        alternatives = []
        searching = True
        while searching: 
            to_search = lines[current[0]][current[1]]
            if to_search == "S":
                to_search = "a"
            index = string.ascii_lowercase.find(to_search)
            letters = string.ascii_lowercase[index:index + 2]
            if "z" in letters:
                letters += "E"
            print(letters)
            options = []
            for letter in letters:
                directions = []
                if current[0] > finish[0]:
                    directions.append(0)
                    if current[1] < finish[1]:
                        directions.append(3)
                    if current[1] > finish[1]:
                        directions.append(2)
                    directions.append(1)
                if current[0] < finish[0]:
                    directions.append(1)
                    if current[1] < finish[1]:
                        directions.append(3)
                    if current[1] > finish[1]:
                        directions.append(2)
                    directions.append(0)                
                
                for x in [0, 1, 2, 3]:
                    if x not in directions:
                        directions.append(x)
                for d in directions[::-1]:
                    if d == 0:
                        #up
                        if (current[0] - 1 >= 0) and (lines[current[0] - 1][current[1]] == letter):
                            options.append((current[0] - 1, current[1]))
                    elif d == 1:
                        #down
                        if (current[0] + 1 < len(lines)) and (lines[current[0] + 1][current[1]] == letter):
                            options.append((current[0] + 1, current[1]))
                    elif d == 2:
                        #left
                        if (current[1] - 1 >= 0) and (lines[current[0]][current[1] - 1] == letter):
                            options.append((current[0], current[1] - 1))
                    else:
                        #right
                        if (current[1] + 1 < len(lines[0])) and (lines[current[0]][current[1] + 1] == letter):
                            options.append((current[0], current[1] + 1))

            options = [option for option in options if option not in path]
            while len(options) == 0:
                if len(alternatives) == 0:
                    searching = False
                    break
                options = alternatives.pop()
                path.pop()
            if not searching:
                break
            current = options.pop()
            path.append(current)
            alternatives.append(options)

            if (current[0] == finish[0]) and (current[1] == finish[1]):
                finished_paths += 1
                min_steps = min(min_steps, len(path))
                while len(options) == 0:
                    if len(alternatives) == 0:
                        searching = False
                        break
                    options = alternatives.pop()
                    path.pop()
                if not searching:
                    break
                current = options.pop()
                path.append(current)
                alternatives.append(options)                
        
        print(finished_paths)
        print(min_steps - 1)

                 



                