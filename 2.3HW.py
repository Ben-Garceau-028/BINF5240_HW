#file_name = "/path/to/your/DNA_SEQ_22.txt" #(Linux, MAC)
#file_name = '/Users/benjamingarceau/Downloads/DNASEQUENCE/TP_53.txt'
import sys
filename = sys.argv[1]
with open(filename, "r") as f:
    lines = f.readlines()
    input_seq = "".join(lines)

def G_content(seq):
    countG = 0
    for nuc in seq:
        if nuc == 'G':
            countG = countG + 1
    return countG
def C_content(seq):
    countC = 0
    for nuc in seq:
        if nuc == 'C':
            countC = countC + 1
    return countC
whole_seq = input("Would you like to view the whole sequence?: ")
if whole_seq == "Yes":
    print(input_seq)
if whole_seq == "No":
    print("Moving onto GC content")
GCcontent_yn_input = input ("Would you like to calculate the GC Content?: ")
if GCcontent_yn_input == "Yes":
    print('The GC content of the SASP is', G_content(input_seq) + C_content(input_seq)/ len(input_seq) * 100)

import sys
filename2 = sys.argv[2]
with open(filename2, "r") as f:
    lines = f.readlines()
    input_seq2 = "".join(lines)
met = 'ATG'
indexmionine = input_seq2.find(met)
frame = indexmionine % 3 + 1
met_pos = input("Would you like to find the met codon?: ")
if met_pos == "Yes":
    print("methionine is positioned within the DNA sequence at position:", indexmionine + 1)
met_frame = input("Would you like to find the frame of the met codon?: ")
if met_frame == "Yes":
    print("methionine is positioned within the DNA sequence a frame:", frame)


import sys
filename = sys.argv[3]
with open(filename, "r") as f:
    lines = f.readlines()
    input_seq = "".join(lines)
first_last_nuc = input("Would you like to know the first nucleotide(enter first) or the last nucleotide(enter last)?: ")
if first_last_nuc == "first":
    first_nuc = input_seq[0]
    print('The first nucleotide of the sequence is:', first_nuc)
if first_last_nuc == "last":
    last_nuc = input_seq[-1]
    print('The last nucleotide of the sequence is:', last_nuc)
start_codon_question = input("Are you looking for a specific start codon: ")
if start_codon_question == "Yes":
    start_codon = input("what start codon do you want to look for: ")
    start_pos = input_seq.find(start_codon)
    frame= start_pos % 3 + 1
    print('reading frame of', start_codon, 'is', frame)
    print('That is all for now thank you')



