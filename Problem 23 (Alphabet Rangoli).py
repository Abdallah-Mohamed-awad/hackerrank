import string

def print_rangoli(size):
    letters = string.ascii_lowercase

    wd = 4 * size - 3

    for i in range(size - 1, -1, -1):
        part = letters[i:size]
        row = part[::-1] + part[1:]
        print("-".join(row).center(wd, "-"))

    for i in range(1, size):
        part = letters[i:size]
        row = part[::-1] + part[1:]
        print("-".join(row).center(wd, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
