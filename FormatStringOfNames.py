def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0].get('name')
    lst = []
    for n in names:
        lst.append(n.get('name'))
    
    ans = ', '.join(lst[:-1])
    ans =  f"{ans} & {lst[-1]}"
    return ans

# def namelist(names):
#     if len(names)==0: return ''
#     if len(names)==1: return names[0]['name']
#     return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

test = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(namelist(test))