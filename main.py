from PIL import Image
import numpy as np

r = range(1024)

x, y = np.meshgrid(r, r)
i = (1 == (abs(x+y)^abs(x-y)+1)**12 % 7) * 255
Image.fromarray(i).convert('L').save('1.png')


showpic = Image.open("1.png")
showpic.show()


#TODO: Make a GUI and input prompts so that a user can mess with this
