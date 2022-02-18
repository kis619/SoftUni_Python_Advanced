def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]

    # filetered_nums = numbers
    if command == "even":
        filetered_nums = filter(lambda x: x % 2 == 0, numbers)
    elif command == "odd":
        filetered_nums = filter(lambda x: x % 2 == 1, numbers)

    return list(filetered_nums)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
