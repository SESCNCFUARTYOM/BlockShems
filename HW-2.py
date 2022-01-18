if __name__ == "__main__":
    a = -3
    b = 8
    while True:
        if a > b:
            a = b
            print(a, b)
            break
        else:
            a += 3
            b -= 1