
if __name__ == '__main__':
    n_valid_pw = 0
    i = 111122
    for i in range(171309, 643603):
        numbers = list(str(i))
        valid = True
        double_found = False
        double_group = 1
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j+1]:
                valid = False
                break
            elif numbers[j] == numbers[j+1]:
                double_group += 1
            else:
                if double_group == 2:
                    double_found = True
                double_group = 1
        if double_group == 2:
            double_found = True
        if not double_found:
            valid = False
        if valid:
            n_valid_pw += 1
    print(n_valid_pw)