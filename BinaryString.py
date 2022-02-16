def binary_array_to_number(arr):
    binary = ''
    for x in arr:
        binary += str(x)
    return int(binary, 2)

binary_array_to_number([0,0,0,1])