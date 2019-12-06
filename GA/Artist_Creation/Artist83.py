from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[167,87,310,213]
draw.ellipse(c,'#ffffff','#000000')
c=[445,441,233,271]
draw.ellipse(c,'#ffffff','#000000')
c=[401,287,70,155]
draw.ellipse(c,'#ffffff','#000000')
c=[60,92,146,241]
draw.ellipse(c,'#ffffff','#000000')
c=[372,15,110,40]
draw.ellipse(c,'#ffffff','#000000')
l=[283,68,4,12]
draw.line(l,'#000000')
l=[423,15,184,132]
draw.line(l,'#000000')
l=[245,246,167,259]
draw.line(l,'#000000')
l=[36,63,260,341]
draw.line(l,'#000000')
l=[322,300,94,239]
draw.line(l,'#000000')
l=[424,330,136,271]
draw.line(l,'#000000')
l=[287,471,282,351]
draw.line(l,'#000000')
l=[376,199,75,139]
draw.line(l,'#000000')
image1.save('Artist83.png')