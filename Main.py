# Fibonacci-sequence-in-Python
# Creating the most easy way of creating Fibonacci sequence in python less than 10 lines of code
NumberofLetters = []
k = 10  #Number of sequence you want
for item in range(k):
    if len(NumberofLetters) >= 2:
        NumberofLetters.append(NumberofLetters[-1]+NumberofLetters[-2])
    else:
        NumberofLetters = [0,1]
        
 
