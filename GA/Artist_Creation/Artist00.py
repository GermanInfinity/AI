from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[454,11,71,320]
draw.ellipse(c,'#ffffff','#000000')
c=[67,91,158,223]
draw.ellipse(c,'#ffffff','#000000')
c=[24,61,217,334]
draw.ellipse(c,'#ffffff','#000000')
c=[374,450,214,148]
draw.ellipse(c,'#ffffff','#000000')
c=[140,253,43,146]
draw.ellipse(c,'#ffffff','#000000')
c=[284,13,77,200]
draw.ellipse(c,'#ffffff','#000000')
c=[228,452,302,19]
draw.ellipse(c,'#ffffff','#000000')
c=[35,326,6,57]
draw.ellipse(c,'#ffffff','#000000')
c=[366,367,267,102]
draw.ellipse(c,'#ffffff','#000000')
c=[74,353,222,283]
draw.ellipse(c,'#ffffff','#000000')
l=[467,299,116,266]
draw.line(l,'#000000')
l=[30,68,241,79]
draw.line(l,'#000000')
l=[323,429,311,98]
draw.line(l,'#000000')
l=[36,100,52,335]
draw.line(l,'#000000')
l=[76,136,240,206]
draw.line(l,'#000000')
l=[440,80,76,174]
draw.line(l,'#000000')
image1.save('Artist00.png')