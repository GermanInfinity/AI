from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[456,421,6,70]
draw.ellipse(c,'#ffffff','#000000')
c=[464,181,251,158]
draw.ellipse(c,'#ffffff','#000000')
l=[427,330,154,255]
draw.line(l,'#000000')
l=[146,226,0,95]
draw.line(l,'#000000')
l=[268,480,210,229]
draw.line(l,'#000000')
l=[190,102,159,141]
draw.line(l,'#000000')
l=[308,99,299,148]
draw.line(l,'#000000')
l=[431,148,13,78]
draw.line(l,'#000000')
l=[103,69,154,309]
draw.line(l,'#000000')
image1.save('Artist09.png')