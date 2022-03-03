def divisors(n):
    ans = 0
    for x in range(1, n + 1):
        if n % x == 0:
            ans += 1
    # return ans
    # return len([x for x in range(1, n + 1) if n % x == 0])
    return sum([n % x == 0 for x in range(1, n + 1)])

print(divisors(1))
print(divisors(4))
print(divisors(5))