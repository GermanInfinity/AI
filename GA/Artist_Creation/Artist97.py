from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[122,337,187,159]
draw.ellipse(c,'#ffffff','#000000')
c=[102,202,2,219]
draw.ellipse(c,'#ffffff','#000000')
c=[341,253,204,287]
draw.ellipse(c,'#ffffff','#000000')
l=[69,295,32,225]
draw.line(l,'#000000')
l=[446,249,64,251]
draw.line(l,'#000000')
l=[17,194,213,145]
draw.line(l,'#000000')
l=[208,429,134,119]
draw.line(l,'#000000')
l=[270,433,271,77]
draw.line(l,'#000000')
l=[197,139,250,142]
draw.line(l,'#000000')
l=[338,199,195,164]
draw.line(l,'#000000')
l=[337,246,288,254]
draw.line(l,'#000000')
l=[321,59,114,82]
draw.line(l,'#000000')
l=[131,441,69,76]
draw.line(l,'#000000')
image1.save('Artist97.png')