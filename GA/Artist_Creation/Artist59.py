from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[250,24,284,172]
draw.ellipse(c,'#ffffff','#000000')
c=[426,327,242,358]
draw.ellipse(c,'#ffffff','#000000')
c=[230,248,288,336]
draw.ellipse(c,'#ffffff','#000000')
c=[464,426,204,174]
draw.ellipse(c,'#ffffff','#000000')
c=[329,317,274,10]
draw.ellipse(c,'#ffffff','#000000')
c=[184,5,194,176]
draw.ellipse(c,'#ffffff','#000000')
c=[62,55,82,19]
draw.ellipse(c,'#ffffff','#000000')
c=[183,339,31,79]
draw.ellipse(c,'#ffffff','#000000')
c=[218,261,145,191]
draw.ellipse(c,'#ffffff','#000000')
c=[305,428,174,137]
draw.ellipse(c,'#ffffff','#000000')
c=[105,381,81,25]
draw.ellipse(c,'#ffffff','#000000')
c=[444,246,341,39]
draw.ellipse(c,'#ffffff','#000000')
c=[266,44,260,182]
draw.ellipse(c,'#ffffff','#000000')
c=[36,258,218,185]
draw.ellipse(c,'#ffffff','#000000')
c=[379,231,226,146]
draw.ellipse(c,'#ffffff','#000000')
c=[62,163,208,27]
draw.ellipse(c,'#ffffff','#000000')
c=[175,162,256,93]
draw.ellipse(c,'#ffffff','#000000')
c=[269,316,214,210]
draw.ellipse(c,'#ffffff','#000000')
c=[423,237,360,110]
draw.ellipse(c,'#ffffff','#000000')
l=[66,16,39,52]
draw.line(l,'#000000')
l=[352,365,194,239]
draw.line(l,'#000000')
l=[116,286,148,84]
draw.line(l,'#000000')
l=[115,20,331,266]
draw.line(l,'#000000')
image1.save('Artist59.png')