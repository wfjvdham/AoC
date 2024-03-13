import os
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        