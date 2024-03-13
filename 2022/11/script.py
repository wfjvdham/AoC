import os
import timeit
from collections import deque

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        monkeys = []

        for i in range(0, len(lines), 7):
            new_monkey = {}
            new_monkey["items"] = deque(map(int, lines[i + 1].split(":")[1].split(",")))
            new_monkey["operation"] = lines[i + 2].split()[4]
            new_monkey["op2"] = lines[i + 2].split()[5]
            new_monkey["test"] = int(lines[i + 3].split()[3])
            new_monkey["true"] = int(lines[i + 4].split()[5])
            new_monkey["false"] = int(lines[i + 5].split()[5])
            new_monkey["inspections"] = 0
            monkeys.append(new_monkey)
        
        mod_all = 1
        for monkey in monkeys:
            mod_all *= monkey["test"]

        for r in range(10000):
            print(r)
            for monkey in monkeys:
                while monkey["items"]:
                    monkey["inspections"] += 1
                    new = monkey["items"].popleft()
                    if monkey["operation"] == "+":
                        if monkey["op2"] == "old":
                            new = new + new
                        else:
                            new = new + int(monkey["op2"])
                    else:
                        if monkey["op2"] == "old":
                            new = new * new
                        else:
                            new = new * int(monkey["op2"])
                    
                    #new = new // 3
                    new = new % mod_all
                    if new % monkey["test"] == 0:
                        monkeys[monkey["true"]]["items"].append(new)
                    else:
                        monkeys[monkey["false"]]["items"].append(new)

        inspections = []
        for monkey in monkeys:
            print(monkey)
            inspections.append(monkey["inspections"])

        highest_values = sorted(inspections)[-2:]
        print(highest_values[0] * highest_values[1])