from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
l=[40,86,234,350]
draw.line(l,'#000000')
image1.save('Artist60.png')