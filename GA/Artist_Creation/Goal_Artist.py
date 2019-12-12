from PIL import Image, ImageDraw
image1 = Image.new('RGB', (480, 360), '#ffffff')
draw = ImageDraw.Draw(image1)


l=[200,200,250,200]
draw.line(l,'#000000')
          
l=[200,200,225,250]
draw.line(l,'#000000')
          
l=[225,250,250,200]
draw.line(l,'#000000')

image1.save('Goal_image.png')