# Ряд Лейбница.

def leibnitz(n):
    pi = 0.0
    for i in range(1, n+1):
        if i % 2 == 1:
            pi += 4 / (2 * i - 1)
        else:
            pi -= 4 / (2 * i - 1)
    return pi

print(leibnitz(10))
