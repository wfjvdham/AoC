import os
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def add_to_dir(root, current_location, object):
    current_dir = root
    if len(current_location) != 0:
        key = "name"
        for val in current_location:
            current_dir = next(filter(lambda d: d.get(key) == val, current_dir['content']), None)
    current_dir['content'].append(object)


def calc_dir_size(root, current_location, small_dirs):
    current_dir = root
    if len(current_location) != 0:
        key = "name"
        for val in current_location:
            current_dir = next(filter(lambda d: d.get(key) == val, current_dir['content']), None)
    current_dir['size'] = sum(d['size'] for d in current_dir['content'])
    #if current_dir['size'] <= 100000:
    small_dirs.append(current_dir['size'])
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    root = {
        "type": "dir",
        "name": "/",
        "content": [],
    }

    current_location = []

    small_dirs = []

    for i in range(len(lines)):
        line = lines[i][:-1].split(" ")
        if line[0] == '$':
            # command
            if line[1] == "cd":
                # move
                if line[2] == "/":
                    # root
                    current_location = []
                elif line[2] == "..":
                    calc_dir_size(root, current_location, small_dirs)
                    current_location.pop()
                else:
                    current_location.append(line[2])
        else:
            # output
            if line[0] == 'dir':
                object = {
                    "type": "dir",
                    "name": line[1],
                    "content": [],
                }
            else:
                # file
                object = {
                    "type": "file",
                    "name": line[1],
                    "size": int(line[0]),
                }
            add_to_dir(root, current_location, object)

    for _ in range(len(current_location)):
        calc_dir_size(root, current_location, small_dirs)
        current_location.pop()
    calc_dir_size(root, current_location, small_dirs)

    #print(json.dumps(root, indent = 2))
    
    req_size = 30000000 - (70000000 - root['size'])
    
    print(min([x for x in small_dirs if x > req_size ]))