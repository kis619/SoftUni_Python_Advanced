def args_length(*args):
    return len(args)
#     count_arguments = 0
#     for arg in args:
#         count_arguments += 1
#
#     return count_arguments


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
