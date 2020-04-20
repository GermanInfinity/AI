import os
from PIL import Image

count = 0
new_width  = 224
new_height = 224
direc = "./fruit_data/train/oranges"

for filename in os.listdir(direc):
	if filename.endswith(".png") or filename.endswith(".jpg"):
		img = Image.open(direc + '/' + filename)
		img = img.resize((new_width, new_height), Image.ANTIALIAS)
		count += 1
		img.save(direc + '/orange' + str(count) + '.png')

