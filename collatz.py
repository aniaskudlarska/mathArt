import sys
import matplotlib.pyplot
import numpy


fig = matplotlib.pyplot.figure()
ax = matplotlib.pyplot.axes()
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

    return(counter)

#this keeps track of how many steps, so we can graph how many steps Y it takes to collatz a value X
dataList = []
for i in range(1,1000):
    dataList.append(Collatz(i))

xVal = numpy.linspace(0,1000, 999) # Creates x values 1,2,3.....999
yVal = dataList


matplotlib.pyplot.scatter(xVal,yVal)
matplotlib.pyplot.show()

