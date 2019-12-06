from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[110,177,292,22]
draw.ellipse(c,'#ffffff','#000000')
c=[194,443,162,254]
draw.ellipse(c,'#ffffff','#000000')
c=[377,201,136,207]
draw.ellipse(c,'#ffffff','#000000')
c=[280,268,215,169]
draw.ellipse(c,'#ffffff','#000000')
c=[25,190,293,292]
draw.ellipse(c,'#ffffff','#000000')
c=[374,94,55,28]
draw.ellipse(c,'#ffffff','#000000')
c=[44,464,336,180]
draw.ellipse(c,'#ffffff','#000000')
l=[58,19,322,160]
draw.line(l,'#000000')
l=[257,211,334,228]
draw.line(l,'#000000')
l=[453,57,353,161]
draw.line(l,'#000000')
image1.save('Artist8.png')