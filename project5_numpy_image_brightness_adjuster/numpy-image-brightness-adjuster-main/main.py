import numpy as np
images= np.random.randint(0,256,(5,5))

#adding a constant value to increase the brightness of the image using broadcasting
brighter = np.clip(images + 40,0,255) #clip is used to ensure that the pixel values do not exceed 255
#print(brighter)

#subtracting a constant value to decrease the brightness of the image using broadcasting
darker = np.clip(images - 40,0,255)
print(darker)

print("Original Image:\n", images)
print("Brighter Image:\n", brighter)
print("Darker Image:\n", darker)
