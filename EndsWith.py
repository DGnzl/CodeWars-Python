def solution(string, ending):
    return string.endswith(ending)
    return string[-len(ending):] == ending or ending == ''
    
print(solution('abc', 'c'))
print(solution('abcde', 'cde'))