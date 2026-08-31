#exercise 1.1
dna_sequence = 'gcatcacgttatgtcgactctgtgtggcgtctgctggg'
mionine = 'ATG'
mionine_LC = mionine.lower()
mionine_backwardsLC = mionine_LC[::-1]
PositionOfmionine = dna_sequence.find(mionine_LC)
frame = PositionOfmionine % 3 + 1
print('The DNA sequence is as follows:', dna_sequence)
print('Methionine positioned baclwards in lowercase:', mionine_backwardsLC)
print("methionine is positioned within the DNA sequence at position:", PositionOfmionine)
print("methionine is positioned within the DNA sequence a frame:", frame)
#WRITE-UP
#First have to make dna sequence and methionine variables into strings.
#Then I decided to make a new variable for each change we make to methionine: new for lowercase, then using the new lowercase variable for backwards.
#Position was used by using the lowercase variable and .find function
