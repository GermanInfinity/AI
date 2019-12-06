from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[144,305,230,195]
draw.ellipse(c,'#ffffff','#000000')
c=[103,198,103,263]
draw.ellipse(c,'#ffffff','#000000')
c=[134,63,79,326]
draw.ellipse(c,'#ffffff','#000000')
c=[330,410,195,166]
draw.ellipse(c,'#ffffff','#000000')
c=[184,59,145,94]
draw.ellipse(c,'#ffffff','#000000')
c=[205,174,178,51]
draw.ellipse(c,'#ffffff','#000000')
c=[96,303,102,79]
draw.ellipse(c,'#ffffff','#000000')
c=[108,36,294,294]
draw.ellipse(c,'#ffffff','#000000')
c=[285,236,268,83]
draw.ellipse(c,'#ffffff','#000000')
c=[463,325,100,353]
draw.ellipse(c,'#ffffff','#000000')
l=[39,344,43,9]
draw.line(l,'#000000')
l=[399,237,350,232]
draw.line(l,'#000000')
l=[339,357,80,208]
draw.line(l,'#000000')
l=[259,198,132,116]
draw.line(l,'#000000')
l=[356,400,98,30]
draw.line(l,'#000000')
image1.save('Artist30.png')