def unused_digits(numbers: list[int]):
    digits = {0,1,2,3,4,5,6,7,8,9}
    ans = ''
    for x in numbers:
        for y in str(x):
            ans += f'{y}'
            digits.discard(int(y))
    print(''.join([str(x) for x in digits]))

unused_digits([12, 34, 56, 78])