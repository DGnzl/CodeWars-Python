def wave(people):
    letters = list(people)
    ans = []
    for i in range(len(letters)):
        if letters[i].isalpha():
            letters[i] = letters[i].upper()
            ans.append(''.join(letters))
            letters[i] = letters[i].lower()

wave('code')