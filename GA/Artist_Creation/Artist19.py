from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[476,234,104,279]
draw.ellipse(c,'#ffffff','#000000')
c=[387,418,206,15]
draw.ellipse(c,'#ffffff','#000000')
c=[403,137,207,125]
draw.ellipse(c,'#ffffff','#000000')
c=[75,166,62,0]
draw.ellipse(c,'#ffffff','#000000')
c=[115,141,258,274]
draw.ellipse(c,'#ffffff','#000000')
c=[68,96,347,337]
draw.ellipse(c,'#ffffff','#000000')
c=[320,118,37,125]
draw.ellipse(c,'#ffffff','#000000')
l=[155,301,323,16]
draw.line(l,'#000000')
l=[274,388,161,236]
draw.line(l,'#000000')
l=[177,452,190,286]
draw.line(l,'#000000')
l=[123,67,239,29]
draw.line(l,'#000000')
l=[310,37,225,256]
draw.line(l,'#000000')
l=[471,73,147,294]
draw.line(l,'#000000')
l=[133,154,180,111]
draw.line(l,'#000000')
l=[339,393,302,203]
draw.line(l,'#000000')
l=[477,397,260,225]
draw.line(l,'#000000')
l=[463,16,75,29]
draw.line(l,'#000000')
image1.save('Artist19.png')