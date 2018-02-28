
import random
def grades():
    #this function returns 10 random scores and grades
    print "Scores and Grades"
    for i in range(0, 10):
        random_num = random.randint(60, 100)
        if random_num < 70:
            grade = 'D'
        elif random_num >= 70 and random_num < 80:
            grade = 'C'
        elif random_num >= 80 and random_num < 90:
            grade = 'B'
        elif random_num >= 90 and random_num < 100:
            grade = 'A'
        print "Score:", random_num, " Your grade is", grade
    print "End of program. Bye!"
grades()
