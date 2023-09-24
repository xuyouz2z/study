def gcd(x, y):
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            max = i
    return max


print(gcd(200, 6))
