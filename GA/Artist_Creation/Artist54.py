from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[293,234,352,236]
draw.ellipse(c,'#ffffff','#000000')
c=[14,386,1,125]
draw.ellipse(c,'#ffffff','#000000')
c=[42,479,249,40]
draw.ellipse(c,'#ffffff','#000000')
c=[183,461,117,196]
draw.ellipse(c,'#ffffff','#000000')
c=[354,179,3,9]
draw.ellipse(c,'#ffffff','#000000')
c=[395,291,102,170]
draw.ellipse(c,'#ffffff','#000000')
c=[349,100,93,130]
draw.ellipse(c,'#ffffff','#000000')
c=[22,250,102,111]
draw.ellipse(c,'#ffffff','#000000')
c=[58,295,89,357]
draw.ellipse(c,'#ffffff','#000000')
c=[100,13,315,27]
draw.ellipse(c,'#ffffff','#000000')
c=[121,361,178,91]
draw.ellipse(c,'#ffffff','#000000')
c=[472,331,245,207]
draw.ellipse(c,'#ffffff','#000000')
c=[267,241,348,211]
draw.ellipse(c,'#ffffff','#000000')
c=[220,26,76,286]
draw.ellipse(c,'#ffffff','#000000')
c=[282,105,114,286]
draw.ellipse(c,'#ffffff','#000000')
c=[348,63,274,242]
draw.ellipse(c,'#ffffff','#000000')
image1.save('Artist54.png')