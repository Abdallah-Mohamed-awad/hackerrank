def minion_game(string):
    string = string.upper()
    kevin = 0
    stuart = 0
    for index in range(len(string)):
        if string[index] in "AEIOU":
            kevin += len(string) - index
        else:
            stuart += len(string) - index

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
