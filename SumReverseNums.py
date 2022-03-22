def sum_dif_rev(n):
    # [1 = 45] 
    # [2 = 54]
    # [3 = 495]
    # [4 = 594]
    # [5 = 4995]
    # [6 = 5994]
    buffer = n // 2
    if n % 2:
        print(int(f'4{"9" * buffer}5'))
    else:
        print(int(f'5{"9" * (buffer - 1)}4'))

sum_dif_rev(1)
sum_dif_rev(3)
sum_dif_rev(4)
sum_dif_rev(6)