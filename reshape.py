import os
from PIL import Image

count = 0
new_width  = 257
new_height = 257
#direc = "./fruit_data/train/oranges"
direc = "../imagesCelline/images2/train/HC11"

for filename in os.listdir(direc):
	if filename.endswith(".png") or filename.endswith(".jpg"):
		img = Image.open(direc + '/' + filename)
		img = img.resize((new_width, new_height), Image.ANTIALIAS)
		count += 1
		img = img.convert('RGB')
		img.save(direc + filename)


