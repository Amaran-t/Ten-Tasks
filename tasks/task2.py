def f(n):
    return n - 10 if n > 100 else f(f(n + 11))

print(f(50))  