sasp_seq= ('TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAG'
           'AAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTC'
           'AGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAAC'
           'ATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAAC'
           'AAAACCAGTAG')
length = len(sasp_seq)
#another way is to define a function that allows you to look for any codon
def find_start_codon(sasp_seq, codon):
    indx = sasp_seq.find(codon) #creates new variable(position)
    if indx != -1:
        frame = indx % 3 + 1
        print('the index of start codon', codon,':', indx)
        print(codon,'is found in frame', frame)
#Other stop codons of SASP; TGA, TAA, TAG
def find_stop_codon(sasp_seq, codon):
    indx = sasp_seq.find(codon)
    if indx != -1:
        frame = indx % 3 + 1
        print('the index of stop codon', codon,':', indx)
        print(codon,'is found in frame', frame)

#Does the SASP gene start with a Met codon?
if sasp_seq.startswith('ATG'):
    print("SASP sequence without initial Met:",sasp_seq[3:])
else:
    print("SASP sequence does not start with a MET codon")

#does the SASP gene have a frame 1 MET codon
metpos= sasp_seq.find('ATG')
frame_met = metpos % 3 + 1
if frame_met == 1:
    print('Yes,the reading frame of Methionine is', frame_met)
else:
    print('No,the reading frame of Methionine is', frame_met)


#how many nucleotides
def nuc_count(dna_seq):
    total = len(dna_seq)
    return total
print('SASP gene has' , nuc_count(sasp_seq), 'nucleotides:')


#from counting the index of ATG is 21
#I consulted Dr. Hoffman and Nikhil
# an if statement for each codon to ind the index of the Start Codon ATG
find_start_codon(sasp_seq, 'TTG')
find_start_codon(sasp_seq, 'GTG')
find_start_codon(sasp_seq, 'ATG')
find_stop_codon(sasp_seq, 'TAG')
find_stop_codon(sasp_seq, 'TGA')
find_stop_codon(sasp_seq, 'TAA')
#so now we have the position and reading frame of our start and stop codon
#we want to define a reading frame between our stop and start codons
find_ATG = sasp_seq.find("ATG") #essentially looks for position, if less than 0 it takes it out
if find_ATG < 0:
    find_ATG = len(sasp_seq) + 1000

find_TTG = sasp_seq.find("TTG")
if find_TTG < 0:
    find_TTG = len(sasp_seq) + 1000

find_GTG = sasp_seq.find("GTG")
if find_GTG < 0:
    find_GTG = len(sasp_seq) + 1000

start_index = min(find_ATG, find_TTG, find_GTG)
print('the starting index is:', start_index)
#iterating from start index to stop codon
for i in range(start_index, length, 3):
    codon = sasp_seq[i:i+3]
    if codon == 'TAG' or codon == 'TGA' or codon == 'TAA':
        end = i
        break
print('The open reading frame is:', len(sasp_seq[start_index:end]), "nucleotides")
OpenReading = sasp_seq[start_index:end]
#amino acids
Amino_acids= len(OpenReading)//3
print('the Amino Acid count is:', Amino_acids)

def G_content(OpenReading):
    countG = 0
    for nuc in OpenReading:
        if nuc == 'G':
            countG = countG + 1
    return countG
def C_content(OpenReading):
    countC = 0
    for nuc in OpenReading:
        if nuc == 'C':
            countC = countC + 1
    return countC
print('the GC content is:', (G_content(OpenReading) + C_content(OpenReading)) / len(OpenReading) * 100,'%')




