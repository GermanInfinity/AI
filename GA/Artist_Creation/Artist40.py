from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[163,435,229,280]
draw.ellipse(c,'#ffffff','#000000')
c=[386,419,344,29]
draw.ellipse(c,'#ffffff','#000000')
c=[392,423,88,204]
draw.ellipse(c,'#ffffff','#000000')
l=[478,277,7,248]
draw.line(l,'#000000')
l=[69,110,209,257]
draw.line(l,'#000000')
l=[64,432,231,8]
draw.line(l,'#000000')
l=[386,453,119,20]
draw.line(l,'#000000')
l=[160,32,332,114]
draw.line(l,'#000000')
l=[240,474,307,230]
draw.line(l,'#000000')
l=[180,106,244,99]
draw.line(l,'#000000')
l=[188,340,60,308]
draw.line(l,'#000000')
image1.save('Artist40.png')