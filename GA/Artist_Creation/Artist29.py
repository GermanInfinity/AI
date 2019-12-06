from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[206,383,264,263]
draw.ellipse(c,'#ffffff','#000000')
c=[379,108,235,13]
draw.ellipse(c,'#ffffff','#000000')
c=[240,150,272,130]
draw.ellipse(c,'#ffffff','#000000')
c=[230,332,16,67]
draw.ellipse(c,'#ffffff','#000000')
c=[130,276,124,91]
draw.ellipse(c,'#ffffff','#000000')
c=[210,98,246,335]
draw.ellipse(c,'#ffffff','#000000')
c=[67,289,329,78]
draw.ellipse(c,'#ffffff','#000000')
l=[244,341,231,82]
draw.line(l,'#000000')
l=[434,67,313,46]
draw.line(l,'#000000')
l=[195,348,294,116]
draw.line(l,'#000000')
l=[180,395,348,286]
draw.line(l,'#000000')
l=[225,67,21,146]
draw.line(l,'#000000')
l=[383,397,27,360]
draw.line(l,'#000000')
l=[273,242,102,283]
draw.line(l,'#000000')
l=[16,381,152,33]
draw.line(l,'#000000')
image1.save('Artist29.png')