import sys
#Rewriting my old Collatz code
#Make a graph of this and make it pretty

def Collatz(num):
    print(num)
    if num == 1:
        return("Completed")

    elif num != 1:
        if num % 2==0:
            num = num // 2
        elif num % 2 == 1:
            num = (3*num) +1
        Collatz(num)

    return("Done")

print(Collatz(22))


