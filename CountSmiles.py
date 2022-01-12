def count_smileys(arr):
    eyes = [':', ';']
    noses = ['-', '~']
    mouths = [')', 'D']
    smile_count = 0
    for s in arr:
        if len(s) == 2:
            if s[0] in eyes:
                if s[1] in mouths:
                    smile_count += 1
        if len(s) == 3:
            if s[0] in eyes:
                if s[1] in noses:
                    if s[2] in mouths:
                        smile_count += 1

    return smile_count


print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))