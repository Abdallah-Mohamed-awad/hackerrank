if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for i in range(N):
        method = input().split()

        if method[0] == "append":
            list_1.append(int(method[1]))

        elif method[0] == "insert":
            list_1.insert(int(method[1]), int(method[2]))

        elif method[0] == "remove":
            list_1.remove(int(method[1]))

        elif method[0] == "sort":
            list_1.sort()

        elif method[0] == "reverse":
            list_1.reverse()

        elif method[0] == "pop":
            list_1.pop()

        elif method[0] == "print":
            print(list_1)
