#file_name = "/path/to/your/DNA_SEQ_22.txt" #(Linux, MAC)
import sys
filename = sys.argv[1]
with open(filename, "r") as f:
    lines = f.readlines()
    input_seq = "".join(lines)

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
def reverse(seq):
    rev_seq = seq[::-1]
    return rev_seq
#command-line
input_manipulation = input("Would you like to find the Reverse, Reverse Complement, or Complement?: ")
if input_manipulation == "Reverse":
    print("Reverse:", reverse(input_seq))
if input_manipulation == "Complement":
    print("Complement:", reverseComplement(input_seq)[::-1])
if input_manipulation == "ReverseComplement":
    print("Reverse Complement:", reverseComplement(input_seq))

