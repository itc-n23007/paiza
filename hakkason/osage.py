def osage(n, m):
    total_time = 0
    for i in range(m):
        total_time += int(input())
        if total_time > n * 60:
            return i
    return "OK"


n = int(input())
m = int(input())
result = osage(n, m)
print(result)
