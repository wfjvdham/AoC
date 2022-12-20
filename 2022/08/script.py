import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines() 

        n_visible_trees = \
            ((len(lines) - 1) * 2) + \
            ((len(lines[0]) - 1) * 2)

        max_scenic_score = 0

        for i in range(1, len(lines) - 1):
            for j in range(1, len(lines[i]) - 1):
                try_tree = int(lines[i][j])
                scenic_score_top = 0
                scenic_score_left = 0
                scenic_score_right = 0
                scenic_score_bottom = 0 
                is_visible = False

                # from top
                for k in range(i - 1, -1, -1):
                    if try_tree > int(lines[k][j]):
                        scenic_score_top += 1
                    else:
                        scenic_score_top += 1
                        break

                # from left
                for k in range(j - 1, -1, -1):
                    if try_tree > int(lines[i][k]):
                        scenic_score_left += 1
                    else:
                        scenic_score_left += 1
                        break

                # from bottom
                for k in range(i + 1, len(lines)):
                    if try_tree > int(lines[k][j]):
                        scenic_score_bottom += 1
                    else:
                        scenic_score_bottom += 1
                        break

                # from right
                for k in range(j + 1, len(lines[0])):
                    if try_tree > int(lines[i][k]):
                        scenic_score_right += 1
                    else:
                        scenic_score_right += 1
                        break

                scenic_score = scenic_score_top * scenic_score_left * \
                    scenic_score_right * scenic_score_bottom

                max_scenic_score = max(max_scenic_score, scenic_score)

        print("finished")
        print(max_scenic_score)
