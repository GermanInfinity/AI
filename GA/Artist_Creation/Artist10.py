from graphics import *
win = GraphWin('Canvas', 480, 360)
from PIL import Image as NewImage

p=Polygon(Point(66,80),Point(212,211),Point(15,172))
p.setFill('Gold')
p.draw(win)
win.postscript(file='Artist10', colormode='color')
img = NewImage.open("Artist10")
img.save("bl.png", "png")
win.getMouse()
win.close()