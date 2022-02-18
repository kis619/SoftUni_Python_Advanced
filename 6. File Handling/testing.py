import re


def get_each_line(file_path: str) -> list:
    with open(file_path) as file:
        text = [line[:-1] for index, line in enumerate(file.readlines()) if index % 2 == 0]

    return text


def replace_characters(text: list, to_be_replaced, replacer: str) -> list:
    reformatted_text = []
    for line in text:
        line = re.sub("[-,.!?]", "@", line)
        reformatted_text.append(line)
    return reformatted_text


def print_result(result: list):
    for line in result:
        words = line.split()
        print(*list(reversed(words)))


SPECIAL_CHARACTERS = "[-,.!?]"
TO_BE_REPLACED_WITH = "Q"

lines = get_each_line("Files/even_lines.txt")

even_lines_without_special_characters = replace_characters(lines, SPECIAL_CHARACTERS, TO_BE_REPLACED_WITH)
print_result(even_lines_without_special_characters)
