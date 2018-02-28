"""
# input
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
# output
new_list = ['hello', 'world']
"""
WORD_LIST = ['hello', 'world', 'my', 'name', 'is', 'Anna']
CHAR = 'o'
NEW_LIST = []
for i in WORD_LIST:
    if i.find(CHAR) != -1:
        NEW_LIST.append(i)
print NEW_LIST
