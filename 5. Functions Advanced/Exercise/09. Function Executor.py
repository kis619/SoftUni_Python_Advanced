def func_executor(*args: tuple):
    functions_results = []
    for func, nums in args:
        result = func(*nums)
        functions_results.append(result)

    return functions_results

# test code below

# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


