def find_squares(num):
    num2 = num // 2
    num1 = num2 + 1
    return f"{num1 ** 2}-{num2 **2}"

print(find_squares(5))