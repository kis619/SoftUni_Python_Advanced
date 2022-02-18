def read_input():
    return [float(el) for el in input().split()]


def count_num_occurrences(list_numbers):
    numbers_occurrences = {}
    for num in list_numbers:
        if num not in numbers_occurrences:
            numbers_occurrences[num] = 0
        numbers_occurrences[num] += 1

    return numbers_occurrences

    # numbers_occurrences = {} - # TODO по-бавно
    # for num in list_numbers:
    #     numbers_occurrences[num] = list_numbers.count(num)
    # return numbers_occurrences


def print_result(dictionary_numbers):
    for number, instances in dictionary_numbers.items():
        print(f"{number} - {instances} times")


numbers = read_input()
numbers_occurrences = count_num_occurrences(numbers)
print_result(numbers_occurrences)


