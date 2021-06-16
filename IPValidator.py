def is_valid_IP(strng):
    parts = strng.split('.')
    if len(parts) != 4:
        return False
    for x in parts:
        if str.isnumeric(x) and (0 <= int(x) <= 255):
            if x[0] == '0' and len(x) > 1:
                return False
            continue
        else:
            return False
    return True