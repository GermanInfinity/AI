from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[277,453,71,143]
draw.ellipse(c,'#ffffff','#000000')
c=[368,116,141,320]
draw.ellipse(c,'#ffffff','#000000')
c=[279,342,186,210]
draw.ellipse(c,'#ffffff','#000000')
c=[52,49,220,5]
draw.ellipse(c,'#ffffff','#000000')
c=[55,3,220,336]
draw.ellipse(c,'#ffffff','#000000')
c=[312,291,126,167]
draw.ellipse(c,'#ffffff','#000000')
c=[428,437,35,238]
draw.ellipse(c,'#ffffff','#000000')
c=[439,311,262,355]
draw.ellipse(c,'#ffffff','#000000')
c=[356,98,315,151]
draw.ellipse(c,'#ffffff','#000000')
c=[202,434,44,261]
draw.ellipse(c,'#ffffff','#000000')
c=[66,19,169,148]
draw.ellipse(c,'#ffffff','#000000')
c=[371,92,125,360]
draw.ellipse(c,'#ffffff','#000000')
c=[371,279,94,81]
draw.ellipse(c,'#ffffff','#000000')
c=[276,94,88,43]
draw.ellipse(c,'#ffffff','#000000')
c=[11,306,250,278]
draw.ellipse(c,'#ffffff','#000000')
l=[64,402,236,289]
draw.line(l,'#000000')
l=[222,320,141,201]
draw.line(l,'#000000')
l=[96,174,323,152]
draw.line(l,'#000000')
l=[37,289,226,217]
draw.line(l,'#000000')
image1.save('Artist52.png')