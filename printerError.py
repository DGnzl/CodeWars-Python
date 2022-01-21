def printer_error(s):
    count = 0
    for x in s:
        if x > 'm':
            count += 1
    return f'{count}/{len(s)}'