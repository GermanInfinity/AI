from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[412,449,359,15]
draw.ellipse(c,'#ffffff','#000000')
c=[457,89,324,299]
draw.ellipse(c,'#ffffff','#000000')
c=[62,70,173,323]
draw.ellipse(c,'#ffffff','#000000')
c=[401,123,337,298]
draw.ellipse(c,'#ffffff','#000000')
c=[242,270,96,49]
draw.ellipse(c,'#ffffff','#000000')
c=[88,92,209,340]
draw.ellipse(c,'#ffffff','#000000')
c=[168,186,291,137]
draw.ellipse(c,'#ffffff','#000000')
c=[359,396,182,341]
draw.ellipse(c,'#ffffff','#000000')
c=[243,224,261,280]
draw.ellipse(c,'#ffffff','#000000')
c=[143,125,149,253]
draw.ellipse(c,'#ffffff','#000000')
c=[140,61,150,78]
draw.ellipse(c,'#ffffff','#000000')
l=[114,417,31,84]
draw.line(l,'#000000')
l=[92,95,114,217]
draw.line(l,'#000000')
l=[435,303,88,345]
draw.line(l,'#000000')
l=[439,133,243,214]
draw.line(l,'#000000')
l=[10,405,250,271]
draw.line(l,'#000000')
l=[125,36,154,296]
draw.line(l,'#000000')
image1.save('Artist6.png')