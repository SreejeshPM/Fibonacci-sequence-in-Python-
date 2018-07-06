# Fibonacci-sequence-in-Python
# Creating the most easy way of creating Fibonacci sequence in python less than 10 lines of code
FibanocciSeries = []
k = 10  #Number of sequence you want
for item in range(k):
    if len(FibanocciSeries) >= 2:
        FibanocciSeries.append(FibanocciSeries[-1]+FibanocciSeries[-2])
    else:
        FibanocciSeries = [0,1]
print (FibanocciSeries)
 
