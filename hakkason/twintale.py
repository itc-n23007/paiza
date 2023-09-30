def twintale(s, t):
    pro = "-" * s
    pro = pro[: t - 1] + "+" + pro[t:]
    print(pro)


s, t = map(int, input().split())
result = twintale(s, t)
print(result)
