def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n & 1:
            return False
        n >>= 1
    return True

# Проверка
test_cases = [1, 2, 3, 8, 10, 0, -4, 16, 255, 256]
for num in test_cases:
    print(f"is_power_of_two({num}) - {is_power_of_two(num)}")