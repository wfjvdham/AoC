import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def move_tail(current_head, current_tail):
    if current_head[0] > current_tail[0] + 1:
        y_tail = current_tail[1]
        x_tail = current_tail[0] + 1
        if current_head[1] > current_tail[1]:
            y_tail = current_tail[1] + 1
        elif current_head[1] < current_tail[1]:
            y_tail = current_tail[1] - 1
        current_tail = (x_tail, y_tail)
    elif current_head[1] > current_tail[1] + 1:
        y_tail = current_tail[1] + 1
        x_tail = current_tail[0]
        if current_head[0] > current_tail[0]:
            x_tail = current_tail[0] + 1
        elif current_head[0] < current_tail[0]:
            x_tail = current_tail[0] - 1
        current_tail = (x_tail, y_tail)
    elif current_head[0] < current_tail[0] - 1:
        y_tail = current_tail[1]
        x_tail = current_tail[0] - 1
        if current_head[1] > current_tail[1]:
            y_tail = current_tail[1] + 1
        elif current_head[1] < current_tail[1]:
            y_tail = current_tail[1] - 1
        current_tail = (x_tail, y_tail)
    elif current_head[1] < current_tail[1] - 1:
        y_tail = current_tail[1] - 1
        x_tail = current_tail[0]
        if current_head[0] > current_tail[0]:
            x_tail = current_tail[0] + 1
        elif current_head[0] < current_tail[0]:
            x_tail = current_tail[0] - 1
        current_tail = (x_tail, y_tail) 

    return current_tail


def move_head(direction, current_head):
    if direction == 'R':
        current_head = (current_head[0] + 1, current_head[1])
    elif direction == 'U':
        current_head = (current_head[0], current_head[1] + 1)   
    elif direction == 'L':
        current_head = (current_head[0] - 1, current_head[1])
    elif direction == 'D':
        current_head = (current_head[0], current_head[1] - 1)

    return current_head 

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        tail_locations = set()
        locations = list(((100, 100), ) * 10)

        for line in lines:
            commands = line.split()
            print(commands)
            direction = commands[0]
            steps = int(commands[1])
            
            for i in range(steps):
                locations[0] = move_head(direction, locations[0])
                for j in range(1, len(locations)):
                    locations[j] = move_tail(locations[j - 1], locations[j])
                    
                    # if j == 1:
                    #     print(j, "===", locations[j])
                    # if j == 2:
                    #     print(j, "===", locations[j])
                    
                    if j == 9:
                        print(locations[j])
                        tail_locations.add(locations[j])
        
        print(len(tail_locations))
        #6266 too high