from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[72,189,301,53]
draw.ellipse(c,'#ffffff','#000000')
c=[280,365,311,82]
draw.ellipse(c,'#ffffff','#000000')
c=[312,381,292,111]
draw.ellipse(c,'#ffffff','#000000')
c=[351,467,180,190]
draw.ellipse(c,'#ffffff','#000000')
c=[386,125,7,110]
draw.ellipse(c,'#ffffff','#000000')
c=[199,302,132,61]
draw.ellipse(c,'#ffffff','#000000')
c=[175,140,5,7]
draw.ellipse(c,'#ffffff','#000000')
c=[268,251,216,182]
draw.ellipse(c,'#ffffff','#000000')
c=[403,201,21,72]
draw.ellipse(c,'#ffffff','#000000')
c=[459,270,306,309]
draw.ellipse(c,'#ffffff','#000000')
l=[380,317,136,100]
draw.line(l,'#000000')
l=[125,165,122,214]
draw.line(l,'#000000')
image1.save('Artist80.png')