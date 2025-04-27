def is_power(n, k):
    if n == 1:  
        return True
    if k == 1: 
        return n == 1
    power = 1
    while power < n:
        power *= k
    return power == n

# Проверка
test_cases = [
    (1, 2),  
    (8, 2),  
    (9, 3),  
    (10, 3), 
    (81, 3), 
    (125, 5) 
]
for n, k in test_cases:
    print(f"is_power({n}, {k}) → {is_power(n, k)}")
