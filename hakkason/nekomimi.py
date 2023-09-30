import re


def count_cat_occurrences(S):
    count = len(re.findall(r"cat", S))
    return count


S = input()

result = count_cat_occurrences(S)
print(result)
