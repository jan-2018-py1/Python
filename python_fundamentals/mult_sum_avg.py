#MULTIPLES
#this program prints all the odd numbers from 1 to 1000.
odd = range(1,10)
for i in odd:
    if i %2 != 0:
        print i

#this program prints all the multiples of 5 from 5 to 1,000,000.
mult = range(5,1000000)
for j in mult:
    if j%5 == 0:
        print j

#SUM LIST
a = [1, 2, 5, 10, 255, 3]
SUM = 0
for i in a:
    SUM += i
print SUM

#AVERAGE LIST
b = [1, 2, 5, 10, 255, 3]
AVG = 0
for i in b:
    AVG += i
AVG /= len(b)-1
print AVG