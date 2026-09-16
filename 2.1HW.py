#Write a program to test whether a PCR primer is a reverse complement palindrome.
#Such a primer might fold and self-hybridize!
#Test your program on at least the following primers
primer1= 'TTGAGTAGACGCGTCTACTCAA'
primer2= 'TTGAGTAGACGTCGTCTACTCAA'
primer3 = 'ATATATATATATATAT'
primer4 = 'ATCTATATATATGTA'

#test for whether primer is a palindrome
def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp
def reverseComplement(seq):
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

def palindrome(primer):
    first5 = primer[:5] #used gemini to help define reverse palindrome and consider palindrome as something like
    #GGCCNNNNGGCC. In this sequence it can still fold and self hybridize
    last5 = primer[-5:]
        #print(first5)
        #print(last5)
    if first5 == reverseComplement(last5):
        print("Primer", primer, "is a palindrome")
    else:
        print(primer, "is not a palindrome")

palindrome(primer1)
palindrome(primer2)
palindrome(primer3)
palindrome(primer4)