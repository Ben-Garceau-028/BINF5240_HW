n = 10
total = 0
#total has to be define outside of the loop in order to add
#otherwise total will be rest to 0 after each loop
for i in range(1, n + 1): # need n+1 to include integers 1-10
    total = total + i
print(total) # this will print each addition

def cumulative_sum(numb):
    total = 0
    for i in range(1, numb + 1):
        total = total + i
    return total
print(cumulative_sum(10))

#genAI rewrites my function without loops
def cumulative_sum(numb):
    return numb * (numb + 1) // 2
print(cumulative_sum(10))
