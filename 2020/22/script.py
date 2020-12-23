
def playGame(player1, player2, gamenr):
    print("=== Game " + str(gamenr) + " ===")
    rounds = []
    while len(player1) > 0 and len(player2) > 0:
        id = ",".join(map(str, player1)) + ":" + ",".join(map(str, player2))
        if id in rounds:
            return player1, player2, True
        else:
            rounds.append(id)
        if len(player1) > player1[0] and len(player2) > player2[0]:
            print("Playing a sub-game to determine the winner...")
            gamenr += 1
            new_player1, new_player2, player1_wins = playGame(player1[1:player1[0]+1], player2[1:player2[0]+1], gamenr)
        else:
            player1_wins = player1[0] > player2[0]
        if player1_wins:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        else:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
    return player1, player2, len(player1) > 0

if __name__ == '__main__':
    input_file = open("2020/22/input")
    raw_lines = input_file.readlines()

    raw_lines = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''.split('\n')

    player1 = []
    for i in range(1, 6):
        player1.append(int(raw_lines[i].strip()))
    player2 = []
    for i in range(8, 13):
        player2.append(int(raw_lines[i].strip()))

    player1 = []
    for i in range(1, 26):
        player1.append(int(raw_lines[i].strip()))
    player2 = []
    for i in range(28, 53):
        player2.append(int(raw_lines[i].strip()))

    player1, player2, player1_wins = playGame(player1, player2, 1)

    result = 0
    if player1_wins:
        for i in range(len(player1)):
            result += player1[i] * (len(player1) - i)
    else:
        for i in range(len(player2)):
            result += player2[i] * (len(player2) - i)
    print(result)