from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[79,142,172,65]
draw.ellipse(c,'#ffffff','#000000')
c=[71,84,106,105]
draw.ellipse(c,'#ffffff','#000000')
c=[244,259,232,60]
draw.ellipse(c,'#ffffff','#000000')
c=[116,5,105,205]
draw.ellipse(c,'#ffffff','#000000')
l=[165,71,48,220]
draw.line(l,'#000000')
l=[212,156,309,199]
draw.line(l,'#000000')
l=[15,304,229,352]
draw.line(l,'#000000')
l=[343,323,75,237]
draw.line(l,'#000000')
l=[149,86,128,204]
draw.line(l,'#000000')
l=[356,322,252,109]
draw.line(l,'#000000')
l=[285,50,32,132]
draw.line(l,'#000000')
l=[249,117,338,283]
draw.line(l,'#000000')
l=[445,86,51,310]
draw.line(l,'#000000')
l=[401,87,10,349]
draw.line(l,'#000000')
l=[376,258,70,168]
draw.line(l,'#000000')
l=[279,433,217,319]
draw.line(l,'#000000')
image1.save('Artist61.png')