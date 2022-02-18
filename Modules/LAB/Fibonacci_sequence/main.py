from Fibonacci_sequence.fibonacci_task_functions import *

command = input()

while not command == "Stop":
    if "Create" in command:
        number = int(command.split()[2])
        fib_sequence = create_fibonacci_sequence(number)
        print(*fib_sequence)

    if "Locate" in command:
        number = int(command.split()[1])
        print(locate_num_in_fibonacci(number, fib_sequence))

    command = input()


# с for-loop и iter

# from Modules.LAB.Fibonacci_sequence.fibonacci_task_functions import *
#
# for command in iter(input, "Stop"):
#     if "Create" in command:
#         number = int(command.split()[2])
#         fib_sequence = create_fibonacci_sequence(number)
#         print(*fib_sequence)
#
#     if "Locate" in command:
#         number = int(command.split()[1])
#         print(locate_num_in_fibonacci(number, fib_sequence))

