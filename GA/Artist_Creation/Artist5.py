from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[368,420,59,34]
draw.ellipse(c,'#ffffff','#000000')
c=[450,398,269,221]
draw.ellipse(c,'#ffffff','#000000')
c=[334,259,56,346]
draw.ellipse(c,'#ffffff','#000000')
c=[153,118,303,342]
draw.ellipse(c,'#ffffff','#000000')
c=[378,118,90,155]
draw.ellipse(c,'#ffffff','#000000')
c=[10,317,81,111]
draw.ellipse(c,'#ffffff','#000000')
c=[61,392,269,273]
draw.ellipse(c,'#ffffff','#000000')
l=[341,294,81,298]
draw.line(l,'#000000')
l=[245,0,358,70]
draw.line(l,'#000000')
l=[156,60,310,9]
draw.line(l,'#000000')
l=[60,398,72,223]
draw.line(l,'#000000')
l=[58,244,182,87]
draw.line(l,'#000000')
l=[33,331,343,281]
draw.line(l,'#000000')
l=[141,229,295,266]
draw.line(l,'#000000')
l=[253,218,133,207]
draw.line(l,'#000000')
l=[233,93,257,136]
draw.line(l,'#000000')
image1.save('Artist5.png')