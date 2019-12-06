from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[368,455,264,248]
draw.ellipse(c,'#ffffff','#000000')
c=[164,90,155,332]
draw.ellipse(c,'#ffffff','#000000')
c=[79,364,336,54]
draw.ellipse(c,'#ffffff','#000000')
c=[418,391,251,168]
draw.ellipse(c,'#ffffff','#000000')
c=[286,277,357,269]
draw.ellipse(c,'#ffffff','#000000')
c=[403,317,41,127]
draw.ellipse(c,'#ffffff','#000000')
c=[224,13,360,187]
draw.ellipse(c,'#ffffff','#000000')
c=[435,0,320,359]
draw.ellipse(c,'#ffffff','#000000')
c=[382,114,69,5]
draw.ellipse(c,'#ffffff','#000000')
l=[414,423,262,286]
draw.line(l,'#000000')
image1.save('Artist7.png')