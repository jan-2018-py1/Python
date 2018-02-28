
for num in range(100, 1001):
    if all(num%i!=0 for i in range(2,num)):
        print num, 'Foo'
    elif int(num**0.5)**2 == int(num):
        print num, 'Bar'
    else:
        print num, 'FooBar'