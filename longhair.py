def longhair(N):
    return "lucky" if N % 7 == 0 else "unlucky"


N = int(input())

result = longhair(N)
print(result)
