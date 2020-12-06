import math


def calc_fuel(mass):
    return math.floor(mass / 3) - 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("01_input")
    lines = input_file.readlines()

    total_fuel = 0

    for line in lines:
        module_fuel = calc_fuel(int(line))
        extra_fuel = calc_fuel(module_fuel)
        while extra_fuel > 0:
            module_fuel += extra_fuel
            extra_fuel = calc_fuel(extra_fuel)
        total_fuel += module_fuel

    print(total_fuel)
