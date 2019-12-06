from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
l=[20,237,2,89]
draw.line(l,'#000000')
l=[422,126,278,185]
draw.line(l,'#000000')
l=[469,102,84,247]
draw.line(l,'#000000')
l=[50,107,165,220]
draw.line(l,'#000000')
l=[393,321,9,136]
draw.line(l,'#000000')
l=[474,244,198,68]
draw.line(l,'#000000')
l=[472,84,97,18]
draw.line(l,'#000000')
l=[8,297,33,65]
draw.line(l,'#000000')
l=[166,317,347,355]
draw.line(l,'#000000')
l=[280,453,130,266]
draw.line(l,'#000000')
l=[220,226,12,326]
draw.line(l,'#000000')
l=[304,382,105,332]
draw.line(l,'#000000')
image1.save('Artist50.png')