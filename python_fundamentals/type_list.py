L = ['magical unicorns',19,'hello',98.98,'world']
I = 0
S = 0
SUM = 0
STRING = ""
for i in L:
    T = type(i)
    if T == int:
        I += 1
        SUM += i
    if T == float:
            SUM += i
    elif T == str:
        S += 1
        STRING += i
        STRING += " "
if I != 0 and S == 0:
    print "The list you entered is of integer type"
    print SUM
elif I == 0 and S != 0:
    print "The list you entered is of string type"
    print STRING
elif I != 0 and S != 0:
    print "The list you entered is of mixed type"
    print STRING
    print SUM