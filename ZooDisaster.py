def who_eats_who(zoo):
    ans = [zoo]
    meals = [
        ['antelope', 'grass'],
        ['big-fish', 'little-fish'],
        ['bug', 'leaves'],
        ['bear', 'big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
        ['chicken', 'bug'],
        ['cow', 'grass'],
        ['fox', 'chicken', 'sheep'],
        ['giraffe', 'leaves'],
        ['lion', 'antelope', 'cow'],
        ['panda', 'leaves'],
        ['sheep', 'grass']]

    animals = [x[0] for x in meals]
    curr = zoo.split(',')
    itr = 0
    while itr < len(curr):
        if curr[itr] in animals and len(curr) > 1:
            if itr > 0 and curr[itr - 1] in meals[animals.index(curr[itr])][1:]:
                ans.append(f'{curr[itr]} eats {curr[itr - 1]}')
                curr.pop(itr - 1)
                itr = max(0, itr - 2)
            elif itr < len(curr) - 1 and curr[itr + 1] in meals[animals.index(curr[itr])][1:]:
                ans.append(f'{curr[itr]} eats {curr[itr + 1]}')
                curr.pop(itr + 1)
            else:
                itr += 1
        else:
            itr += 1
    ans.append(','.join(curr))
    print(zoo)
    print(ans)
    return ans

who_eats_who("fox,bug,chicken,grass,sheep")
who_eats_who('leaves,lion,antelope,fox,fox,leaves,bug,bicycle')