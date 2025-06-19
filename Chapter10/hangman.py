def hangman(word):
    wrong = 0
    stage = ["",
             "ーーーーーー       ",
             "|                  ",
             "|          |       ",
             "|          O       ",
             "|         /|\\     ",
             "|         / \\     "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    while wrong < len(stage) - 1:
        print("\n")
        msg = "１文字を予想してね: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stage[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            win = True
            break
    if not win:
        print("\n".join(stage[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

hangman("cat")
