#Homework 1.3
#cars = 100
#people_per_car = 4
#drivers = 30
#passengers = 90
def carsnotdriven(cars, drivers):
    return cars - drivers
def carsdriven(drivers):
    carsdriven = drivers
    return carsdriven
def carpoolcapacity(drivers, people_per_car):
    return drivers * people_per_car
def average_people_per_car(drivers, passengers):
    return (drivers + passengers) // (drivers)
def people_in_last_car(drivers, passengers, people_per_car ):
    return (drivers + passengers - 1) % people_per_car + 1
# Output the results
print('There are', carsnotdriven(100, 30), 'cars not driven.')
print("There are only", carsdriven(30), "drivers available.")
print('There is a carpool capacity of', carpoolcapacity(30, 4))
print('There are an average of', average_people_per_car(30,90 ), 'per car.')
print('There are', people_in_last_car(30, 90,4) , 'people in the last car.')
# Functions for using DNA

def firstnucleotide(dna_sequence):
    return dna_sequence[0]
print('The first nucleotide of the DNA Sequence is:', firstnucleotide('gcatgacgttattacgactctgtgtggcgtctgctggg'))

def lastnucleotide(dna_seq):
    return dna_seq[-1]
print('The last nucleotide of the DNA Sequence is:', lastnucleotide('gcatgacgttattacgactctgtgtggcgtctgctggg'))


dna_seq= 'gcatgacgttattacgactctgtgtggcgtctgctggg'
def reverse_met(methionine):
    return methionine[::-1]
print('methionine reversed is:', reverse_met('ATG'))

def find_met(dna_seq, met):
    return dna_seq.find(met.lower())
print('Methionine is at position', find_met(dna_seq, 'ATG'))

def find_frame(dna_seq, met):
    pos = dna_seq.find(met.lower())
    return pos %3 + 1
print('Methionine is at frame', find_frame(dna_seq, 'ATG'))