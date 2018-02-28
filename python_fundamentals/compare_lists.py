"""
LIST1 = [1, 2, 5, 6, 2]
LIST2 = [1, 2, 5, 6, 2]

LIST1 = [1, 2, 5, 6, 5]
LIST2 = [1, 2, 5, 6, 5, 3]

LIST1 = [1, 2, 5, 6, 5, 16]
LIST2 = [1, 2, 5, 6, 5]

LIST1 = ['celery', 'carrots', 'bread', 'milk']
LIST2 = ['celery', 'carrots', 'bread', 'cream']
"""

LIST1 = ['celery', 'carrots', 'bread', 'milk']
LIST2 = ['celery', 'carrots', 'bread', 'cream']
COMP = cmp(LIST1, LIST2)
if COMP == 0:
    print "Lists are identical"
else:
    print "Lists are not the same"
