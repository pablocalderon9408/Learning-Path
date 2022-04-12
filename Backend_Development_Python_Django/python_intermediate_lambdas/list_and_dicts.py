def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "John", "last_name": "Doe"}

    super_list = [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "John", "last_name": "Doe"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "integer_nums": [-1, -22, -53, 4, 5, 6, 7, 8, 9, 10],
        "float_nums": [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10],
    }

    for key,value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()