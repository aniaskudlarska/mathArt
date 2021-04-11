from PIL import Image
import numpy as np



var1 = int(input("Enter a value for var 1 (37 is default): "))
var2 = int(input("Enter a value for var 2 (7 is default): "))
var3 = int(input("Enter a value for var 3 (higher than 100):  "))

var4 = int(input("Enter a size for the bitmap (Default is 1024): "))

var5 = int(input("Enter an int 1-8: "))

r = range(1024) #make this a var

x, y = np.meshgrid(r, r)

i = (var5 == (abs(x+y)^abs(x-y)+1)**var1 % var2) * var3



Image.fromarray(i).convert('L').save('1.png')
im = Image.open('1.png')
im.show()



