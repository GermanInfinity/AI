from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[358,474,258,63]
draw.ellipse(c,'#ffffff','#000000')
c=[286,456,80,218]
draw.ellipse(c,'#ffffff','#000000')
c=[294,201,254,344]
draw.ellipse(c,'#ffffff','#000000')
c=[143,189,192,175]
draw.ellipse(c,'#ffffff','#000000')
c=[413,201,8,294]
draw.ellipse(c,'#ffffff','#000000')
c=[310,228,213,153]
draw.ellipse(c,'#ffffff','#000000')
c=[465,398,200,246]
draw.ellipse(c,'#ffffff','#000000')
c=[385,366,158,103]
draw.ellipse(c,'#ffffff','#000000')
c=[374,39,298,238]
draw.ellipse(c,'#ffffff','#000000')
c=[137,362,21,224]
draw.ellipse(c,'#ffffff','#000000')
c=[317,234,64,312]
draw.ellipse(c,'#ffffff','#000000')
l=[148,39,189,261]
draw.line(l,'#000000')
l=[360,10,328,358]
draw.line(l,'#000000')
l=[299,436,117,50]
draw.line(l,'#000000')
l=[437,89,131,189]
draw.line(l,'#000000')
l=[350,54,155,346]
draw.line(l,'#000000')
image1.save('Artist79.png')