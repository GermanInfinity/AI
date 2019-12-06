from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[178,298,342,122]
draw.ellipse(c,'#ffffff','#000000')
l=[57,194,187,285]
draw.line(l,'#000000')
l=[109,226,151,174]
draw.line(l,'#000000')
l=[178,346,67,69]
draw.line(l,'#000000')
l=[232,286,123,69]
draw.line(l,'#000000')
image1.save('Artist3.png')