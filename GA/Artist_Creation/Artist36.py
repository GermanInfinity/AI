from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[372,24,153,103]
draw.ellipse(c,'#ffffff','#000000')
c=[330,450,184,77]
draw.ellipse(c,'#ffffff','#000000')
c=[322,266,16,156]
draw.ellipse(c,'#ffffff','#000000')
c=[166,165,184,4]
draw.ellipse(c,'#ffffff','#000000')
c=[290,318,282,297]
draw.ellipse(c,'#ffffff','#000000')
c=[224,174,301,287]
draw.ellipse(c,'#ffffff','#000000')
c=[194,37,166,172]
draw.ellipse(c,'#ffffff','#000000')
c=[2,437,91,59]
draw.ellipse(c,'#ffffff','#000000')
c=[38,370,142,133]
draw.ellipse(c,'#ffffff','#000000')
c=[437,113,15,346]
draw.ellipse(c,'#ffffff','#000000')
c=[18,311,257,231]
draw.ellipse(c,'#ffffff','#000000')
c=[119,446,212,289]
draw.ellipse(c,'#ffffff','#000000')
c=[156,335,193,78]
draw.ellipse(c,'#ffffff','#000000')
c=[288,55,207,106]
draw.ellipse(c,'#ffffff','#000000')
c=[163,208,67,69]
draw.ellipse(c,'#ffffff','#000000')
l=[358,5,61,75]
draw.line(l,'#000000')
l=[304,93,326,17]
draw.line(l,'#000000')
l=[302,232,152,110]
draw.line(l,'#000000')
l=[99,39,103,222]
draw.line(l,'#000000')
l=[145,188,350,353]
draw.line(l,'#000000')
l=[374,136,214,250]
draw.line(l,'#000000')
image1.save('Artist36.png')