import copy

def findSolution(solution, field_ranges):
    for i in range(20):
        field_options = list(field_ranges.keys())
        for key in field_ranges.keys():
            for ticket in valid_tickets:
                ticket_values = ticket.split(',')
                if int(ticket_values[i]) not in field_ranges[key]:
                    field_options.remove(key)
                    break
        if len(field_options) == 1:
            solution[field_options[0]] = i
            field_ranges.pop(field_options[0])
    return solution, field_ranges

if __name__ == '__main__':
    input_file = open("2020/16/input")
    raw_lines = input_file.readlines()

    valid_numbers = set()
    field_ranges = dict()

    for i in range(20):
        line = raw_lines[i]
        key = line.split(':')[0]
        value = set()
        ranges = line.split(':')[1].split()
        for valid_range in ranges:
            if valid_range != 'or':
                borders = valid_range.split('-')
                for j in range(int(borders[0]), int(borders[1]) + 1):
                    valid_numbers.add(j)
                    value.add(j)
        field_ranges[key] = value

    invalid_values = list()
    valid_tickets = list()

    for i in range(25, len(raw_lines)):
        ticket = raw_lines[i]
        ticket_values = ticket.split(',')
        is_valid = True
        for j in range(len(ticket_values)):
            if int(ticket_values[j]) not in valid_numbers:
                invalid_values.append(int(ticket_values[j]))
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)
    print(sum(invalid_values))

    solution = dict()

    while True:
        solution, field_ranges = findSolution(solution, field_ranges)
        if len(solution) == 20:
            break

    my_ticket = raw_lines[22]
    my_ticket = my_ticket.split(',')

    result = 1

    for key in solution.keys():
        if key.startswith('departure'):
            result *= int(my_ticket[solution[key]])
            values.append(int(my_ticket[solution[key]]))

