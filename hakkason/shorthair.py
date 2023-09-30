def shorthair(N, S):
    return "\n".join([S] * N)


N, S = int(input()), input()

result = shorthair(N, S)
print(result)
