import sys
import matplotlib

#Rewriting my old Collatz code
#Make a graph of this and make it pretty

def Collatz(num, counter=0):

    while num != 1:
        if num % 2==0:
            num = num // 2
            counter += 1

        elif num % 2 == 1:
            num = (3*num) +1
            counter += 1

    return("Reached end in " + str(counter) + " steps")

print(Collatz(22))

#this keeps track of how many steps, so we can graph how many steps Y it takes to collatz a value X


