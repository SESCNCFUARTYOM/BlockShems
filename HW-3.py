if __name__ == "__main__":
    c = 3
    a = 2
    b = 10
    while True:
        if b > a:
            a += c
            b -= 1
            c += 1
        else:
            c *= b
            print(c)
            break