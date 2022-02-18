# def palindrome(word: str, index=0):
#     if len(word) % 2 == 1:  # нечетен палиндром
#         if index == len(word) // 2:
#             return f"{word} is a palindrome"
#     elif len(word) % 2 == 0: # четен палиндом
#         if index == len(word) // 2:
#             if word[index - 1] == word[index]:
#                 return f"{word} is a palindrome"
#
#     first_char = word[index]
#     last_char = word[-index - 1]
#
#     if first_char == last_char:
#         return palindrome(word, index + 1)
#
#     else:
#         return f"{word} is not a palindrome"
#
#
# print(palindrome("abcdedcba", 0))
# print(palindrome("abcdeedcba", 0))
# print(palindrome("petrp", 0))
# print(palindrome("peter", 0))
#
# ##################################### best
# def palindrome(word: str, index=0):
#
#     left_index = index
#     right_index = word[len(word) - 1 - index]
#
#     if left_index >= len(word) / 2:
#         return f"{word} is a palindrome"
#
#     if not word[index] == word[len(word) - 1 - index]:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, index + 1)
#
#


##################################### best
def palindrome(word: str, index=0):
    if index >= len(word) / 2:
        return f"{word} is a palindrome"

    if not word[index] == word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcdedcba", 0))
print(palindrome("abcdeedcba", 0))
print(palindrome("petrp", 0))
print(palindrome("peter", 0))

