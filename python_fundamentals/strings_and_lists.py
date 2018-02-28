words = "I'ts thanksgiving day. It's my birthday, too!"
print words.find("day")
new_words = words.replace(" day", " month")
print new_words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
z1 = z[:len(z)/2]
z2 = z[len(z)/2:]
newList = [0]
newList[0] = z1
newList += z2
print newList