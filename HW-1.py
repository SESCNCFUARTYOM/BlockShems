if __name__ == "__main__":
    x = 3
    y = 0
    while True:
        if x < 0:
            y = x
            print(y)
            break
        else:
            if x > y:
                y = x * x
                print(y)
                break
            else:
                y = x - 1
