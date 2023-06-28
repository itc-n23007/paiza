def osage(n,m,times):
        total_time = 0
    for i in range(m):
        total_time += times[i]
        if total_time > n * 60:
            return i
    return "OK"

n,m,times=map(int,input().split())
result=osage(n,m,times)
print(result)
