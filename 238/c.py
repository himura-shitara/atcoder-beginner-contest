def f(x):
    n = len(str(x))
    if n == 1:
        return x
    else:
        return x - int('9' * (n - 1))


N = int(input())
current = 0
for i in range(N):
    current += f(i + 1)
print(current % 998244353)
