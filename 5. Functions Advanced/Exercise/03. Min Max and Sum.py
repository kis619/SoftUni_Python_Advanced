def print_result(min, max, tots):
    print(f"The minimum number is {min}",
          f"The maximum number is {max}",
          f"The sum number is: {tots}", sep="\n")


numbers = [int(num) for num in input().split()]
minimal = min(numbers)
maximal = max(numbers)
total_sum = sum(numbers)


print_result(minimal, maximal, total_sum)

# def print_result_2(min, max, tots):
#     print(f"The minimum number is {min}\n"
#           f"The maximum number is {max}\n"
#           f"The sum number is: {tots}")
# print_result_2(mininmal, maximal, total_sum)