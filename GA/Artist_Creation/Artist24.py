from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[263,446,251,328]
draw.ellipse(c,'#ffffff','#000000')
c=[144,420,68,283]
draw.ellipse(c,'#ffffff','#000000')
c=[216,386,353,285]
draw.ellipse(c,'#ffffff','#000000')
c=[219,285,1,123]
draw.ellipse(c,'#ffffff','#000000')
c=[90,51,343,23]
draw.ellipse(c,'#ffffff','#000000')
c=[54,225,182,130]
draw.ellipse(c,'#ffffff','#000000')
c=[396,473,150,176]
draw.ellipse(c,'#ffffff','#000000')
c=[10,40,334,343]
draw.ellipse(c,'#ffffff','#000000')
c=[117,1,184,233]
draw.ellipse(c,'#ffffff','#000000')
c=[386,230,231,104]
draw.ellipse(c,'#ffffff','#000000')
c=[409,273,128,137]
draw.ellipse(c,'#ffffff','#000000')
c=[314,198,19,273]
draw.ellipse(c,'#ffffff','#000000')
c=[220,304,245,153]
draw.ellipse(c,'#ffffff','#000000')
c=[205,458,279,91]
draw.ellipse(c,'#ffffff','#000000')
c=[262,41,270,319]
draw.ellipse(c,'#ffffff','#000000')
c=[128,73,60,141]
draw.ellipse(c,'#ffffff','#000000')
c=[67,236,97,129]
draw.ellipse(c,'#ffffff','#000000')
c=[108,267,149,85]
draw.ellipse(c,'#ffffff','#000000')
c=[216,274,240,270]
draw.ellipse(c,'#ffffff','#000000')
l=[425,226,336,125]
draw.line(l,'#000000')
l=[323,389,271,212]
draw.line(l,'#000000')
image1.save('Artist24.png')