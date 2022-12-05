import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_file = open("input")
    lines = input_file.readlines()

    your_scores = []

    for line in lines:
        chars = line.split()

        game_points = 3

        opponent_selection = ['A', 'B', 'C']
        responses = ['X', 'Y', 'Z']

        i = opponent_selection.index(chars[0])

        req_outcome = chars.pop()
        # you need to lose
        if req_outcome == 'X':
            i = (i - 1) % 3
        elif req_outcome == 'Z':
            i = (i + 1) % 3

        # print('you need to: ', req_outcome)
        # print('your response', responses[i])

        chars.append(responses[i])

        shape_points = 1

        if chars[1] == 'Y':
            shape_points = 2
        elif chars[1] == 'Z':
            shape_points = 3

        # you win
        if (
            (chars[0] == 'A' and chars[1] == 'Y') or
            (chars[0] == 'B' and chars[1] == 'Z') or
            (chars[0] == 'C' and chars[1] == 'X')
        ):
            game_points = 6
        # you lose
        elif (
            (chars[0] == 'A' and chars[1] == 'Z') or
            (chars[0] == 'B' and chars[1] == 'X') or
            (chars[0] == 'C' and chars[1] == 'Y')
        ):
            game_points = 0
        
        your_scores.append(game_points + shape_points)

    print(sum(your_scores))

# higher then 10368