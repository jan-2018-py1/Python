
def odd_even():
    #function that prints the odd and even numbers from 1 to 2000.
    for i in range(1, 2001):
        if i % 2 == 0:
            print 'Number is', i, '.', 'This is an even number'
        else:
            print 'Number is', i, '.', 'This is an odd number'
odd_even()

a = [2, 4, 10, 16]
def multiply(lis, mult):
    #function that multiplies a number in every element of a list.
    new_list = []
    for i in lis:
        res = i * mult
        new_list.append(res)
    return new_list
#b = multiply(a, 5)
#print b

def layered_multiples(arr):
    # your code here
    # [6, 12, 15]
    new_arr = []
    inner_arr = []
    for i in arr:
        inner_arr = []
        for j in range(1, i+1):
            inner_arr.append(1)
        new_arr.append(inner_arr)
    return new_arr
x = layered_multiples(multiply([2,4,5],3))
print x
