
import random
def coin_toss():
    print "Starting the program..."
    heads = 0
    tails = 0
    for i in range(0, 5001):
        value = ""
        x = random.random()
        x_rounded = round(x)
        if x_rounded == 0.0:
            heads += 1
            value = "head!"
        elif x_rounded == 1.0:
            tails += 1
            value = "tail!"
        print "Attempt #", i, "  Throwing a coin...  It's a", value, "    Got", heads, "head(s) so far and", tails, "tail(s) so far"
    print "Ending the program, gracias!"
coin_toss()
