def tribonacci(signature, n):
    while (len(signature) < n):
        signature.append(sum(signature[-3:]))
    return (signature[0:n])

tribonacci([1, 1, 1], 10)