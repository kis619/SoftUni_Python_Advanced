# data = input().split("|")
# reversed_data = list(reversed(data))
# new = [element.split() for element in reversed_data]
# new = [el for el in new if el] # input = 1| removing all the spaces
# print(*[j for el in new for j in el])


nums = [[element for element in el.split() if not element == ' ']for el in input().split("|")]
nums.reverse()
print(*[each for row in nums for each in row])
