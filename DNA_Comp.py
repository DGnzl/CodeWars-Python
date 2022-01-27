def DNA_strand(dna):
    ans = ''
    for x in range(len(dna)):
        if dna[x] == 'A':
            ans += 'T'
        elif dna[x] == 'T':
            ans += 'A'
        elif dna[x] == 'C':
            ans += 'G'
        elif dna[x] == 'G':
            ans += 'C'
    return ans