from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)
c=[329,139,265,213]
draw.ellipse(c,'#ffffff','#000000')
c=[102,381,194,350]
draw.ellipse(c,'#ffffff','#000000')
c=[412,172,238,29]
draw.ellipse(c,'#ffffff','#000000')
l=[406,479,153,246]
draw.line(l,'#000000')
l=[202,366,65,214]
draw.line(l,'#000000')
l=[345,21,329,133]
draw.line(l,'#000000')
l=[159,149,323,359]
draw.line(l,'#000000')
l=[137,376,286,239]
draw.line(l,'#000000')
l=[278,388,106,284]
draw.line(l,'#000000')
l=[272,395,41,347]
draw.line(l,'#000000')
l=[274,442,46,120]
draw.line(l,'#000000')
l=[139,299,25,175]
draw.line(l,'#000000')
l=[64,430,347,257]
draw.line(l,'#000000')
l=[395,480,51,88]
draw.line(l,'#000000')
l=[160,440,240,41]
draw.line(l,'#000000')
l=[316,286,130,324]
draw.line(l,'#000000')
l=[274,108,144,315]
draw.line(l,'#000000')
l=[123,210,83,70]
draw.line(l,'#000000')
l=[357,73,230,227]
draw.line(l,'#000000')
l=[271,361,360,317]
draw.line(l,'#000000')
image1.save('Artist02.png')