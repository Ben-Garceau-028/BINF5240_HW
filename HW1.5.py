#original complement function
def complement(nuc):
    nuc = nuc.upper() # this allows us
    # to change all of out lowercase nucleotides into uppercase
    if nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'C':
        comp = 'G'
    elif nuc == 'G':
        comp = 'C'
    else:
        comp = nuc
    return comp
def revcomplement (codon):
    recvomp = ''5
    for nuc in codon:
        recvomp += complement(nuc)
    return recvomp[::-1]
print(revcomplement('ATG'))
print(revcomplement('atgTC'))






