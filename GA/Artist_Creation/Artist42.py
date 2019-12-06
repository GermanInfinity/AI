from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
l=[12,247,251,92]
draw.line(l,'#000000')
l=[333,167,71,292]
draw.line(l,'#000000')
l=[455,171,13,80]
draw.line(l,'#000000')
l=[344,461,29,239]
draw.line(l,'#000000')
l=[166,422,154,317]
draw.line(l,'#000000')
image1.save('Artist42.png')