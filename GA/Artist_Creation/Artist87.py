from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[177,365,128,352]
draw.ellipse(c,'#ffffff','#000000')
c=[101,14,181,107]
draw.ellipse(c,'#ffffff','#000000')
c=[456,47,192,205]
draw.ellipse(c,'#ffffff','#000000')
c=[267,97,18,179]
draw.ellipse(c,'#ffffff','#000000')
c=[164,126,208,169]
draw.ellipse(c,'#ffffff','#000000')
c=[76,456,107,290]
draw.ellipse(c,'#ffffff','#000000')
c=[21,51,207,6]
draw.ellipse(c,'#ffffff','#000000')
c=[153,303,346,309]
draw.ellipse(c,'#ffffff','#000000')
l=[406,239,350,163]
draw.line(l,'#000000')
l=[323,72,223,32]
draw.line(l,'#000000')
l=[342,293,162,29]
draw.line(l,'#000000')
l=[476,76,175,347]
draw.line(l,'#000000')
l=[249,181,212,87]
draw.line(l,'#000000')
l=[225,114,335,40]
draw.line(l,'#000000')
l=[290,116,19,292]
draw.line(l,'#000000')
l=[346,332,54,263]
draw.line(l,'#000000')
image1.save('Artist87.png')