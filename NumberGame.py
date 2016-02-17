from random import *
from timeit import default_timer as timer



print """This is a simple test to determine how fast
python can reach a user generated number from a
random number."""
print ""

# Assigning variables  
a = randint(0, 1000)

b = int(raw_input("Let's start by typing a number from 1 to 1000: "))


# Creating a while loop, to loop until the random number is the same as the input number.
# Haven't placed it in a definition due to just playing around with the code.

while a!=b:
    # Starting timer to count how long the loop lasts
    start = timer()
    print "The current random number is: %s" % a
    # if random number is 10 digits away (+ or -)
    if b == a+11:
        print "Nearly there! 10 more to go."
    elif b == a-11:
        print "Nearly there! 10 more to go."
    # if random number is greater than input, then decrease value until it reaches input
    if a>b:
        a-=1
    # if random number is less than input, then increase value until it reaches input    
    elif a<b:
        a+=1
    if a== b:
        end = timer()
        # Attempting to check timer and printing correct time measurement (Needs a bit of work)
        if end-start<0.06:
            print """Your number has been reached! Your number was: %s.
It only took %s seconds for it to be reached.""" % (b, end-start)
        elif end-start>0.06:
                        print """Your number has been reached! Your number was: %s.
It only took %s hours for it to be reached.""" % (b, end-start)
        
        
