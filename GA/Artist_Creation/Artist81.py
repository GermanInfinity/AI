from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[61,94,222,191]
draw.ellipse(c,'#ffffff','#000000')
c=[315,456,107,130]
draw.ellipse(c,'#ffffff','#000000')
c=[291,278,255,330]
draw.ellipse(c,'#ffffff','#000000')
c=[76,468,206,201]
draw.ellipse(c,'#ffffff','#000000')
c=[125,282,143,159]
draw.ellipse(c,'#ffffff','#000000')
c=[309,369,325,169]
draw.ellipse(c,'#ffffff','#000000')
c=[299,47,111,336]
draw.ellipse(c,'#ffffff','#000000')
c=[233,203,351,51]
draw.ellipse(c,'#ffffff','#000000')
c=[393,364,315,70]
draw.ellipse(c,'#ffffff','#000000')
c=[113,185,326,283]
draw.ellipse(c,'#ffffff','#000000')
c=[95,310,144,242]
draw.ellipse(c,'#ffffff','#000000')
c=[386,229,99,127]
draw.ellipse(c,'#ffffff','#000000')
l=[196,359,275,117]
draw.line(l,'#000000')
l=[241,8,286,259]
draw.line(l,'#000000')
l=[144,42,275,173]
draw.line(l,'#000000')
l=[42,248,38,26]
draw.line(l,'#000000')
l=[173,2,24,175]
draw.line(l,'#000000')
l=[349,95,304,255]
draw.line(l,'#000000')
l=[358,396,76,45]
draw.line(l,'#000000')
l=[238,60,132,319]
draw.line(l,'#000000')
l=[433,64,355,25]
draw.line(l,'#000000')
l=[307,191,119,321]
draw.line(l,'#000000')
l=[465,20,108,128]
draw.line(l,'#000000')
image1.save('Artist81.png')