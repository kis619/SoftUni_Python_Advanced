# start_int = int(input())
# end_int = int(input())
#
#
# def num_can_be_divided(num):
#     for divisor in range(2, 11):
#         if num % divisor == 0: return True
#
#     return False
#
#
# print([num for num in range(start_int, end_int + 1) if num_can_be_divided(num)])

start_int = int(input())
end_int = int(input())

print([num for num in range(start_int, end_int + 1) if [1 for divisor in range(2, 11) if num % divisor == 0]])