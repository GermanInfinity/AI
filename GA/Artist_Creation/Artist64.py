from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[341,255,72,234]
draw.ellipse(c,'#ffffff','#000000')
c=[26,421,85,355]
draw.ellipse(c,'#ffffff','#000000')
c=[411,268,50,340]
draw.ellipse(c,'#ffffff','#000000')
c=[198,166,24,161]
draw.ellipse(c,'#ffffff','#000000')
c=[217,6,130,329]
draw.ellipse(c,'#ffffff','#000000')
c=[284,72,351,52]
draw.ellipse(c,'#ffffff','#000000')
c=[445,99,348,145]
draw.ellipse(c,'#ffffff','#000000')
c=[257,145,241,111]
draw.ellipse(c,'#ffffff','#000000')
c=[89,109,16,5]
draw.ellipse(c,'#ffffff','#000000')
c=[447,32,123,116]
draw.ellipse(c,'#ffffff','#000000')
c=[282,393,77,40]
draw.ellipse(c,'#ffffff','#000000')
c=[93,393,196,326]
draw.ellipse(c,'#ffffff','#000000')
c=[148,404,224,15]
draw.ellipse(c,'#ffffff','#000000')
c=[443,300,78,25]
draw.ellipse(c,'#ffffff','#000000')
c=[57,383,344,38]
draw.ellipse(c,'#ffffff','#000000')
l=[49,96,127,178]
draw.line(l,'#000000')
l=[147,470,80,281]
draw.line(l,'#000000')
l=[280,456,287,182]
draw.line(l,'#000000')
l=[375,453,342,139]
draw.line(l,'#000000')
l=[360,321,264,21]
draw.line(l,'#000000')
l=[76,219,178,324]
draw.line(l,'#000000')
l=[270,288,168,263]
draw.line(l,'#000000')
l=[432,35,215,122]
draw.line(l,'#000000')
image1.save('Artist64.png')