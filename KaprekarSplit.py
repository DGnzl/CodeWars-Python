def kaprekar_split(n):
    sqStr = str(n ** 2)
    if n == 1:
        return 0
    for c in range(1,len(sqStr)):
        if int(sqStr[:c]) + int(sqStr[c:]) == n:
            return c
    return -1

kaprekar_split(9) # 1
# 45 -> 2
# 5050 -> 4