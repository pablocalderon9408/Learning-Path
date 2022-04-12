def run():
    # squares = []
    # for i in range(1,101):
    #     squares.append(i**2)

    # print(squares)

    # [element for element in iterable if condition]
    squares = [i**2 for i in range(1,101)]

    challenge = [i for i in range(1,999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(challenge)

if __name__ == '__main__':
    run()