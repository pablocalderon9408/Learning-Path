def run():
    my_dict = {}

    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1,101) if i%3 != 0}
    print(my_dict)

    # key: value for value in iterable if condition

    squares_dict = {i:i**0.5 for i in range(1,101)}
    print(squares_dict)

if __name__ == '__main__':
    run()
    