
from Graphics import Graphics
from Separator import Separator

class Screen(object):
  
  def __init__(self):
    self.num = -1
    self.width = 600
    self.height = 15
    self.space = 2
    self.separator_color = "#555555"
    self.separator_width = 1
    self.separator_active = True
    self.applets = []

  
  def init(self):
    self.num = int(self.num)
    self.width = int(self.width)
    self.height = int(self.height)
    self.space = int(self.space)
    self.g = Graphics(self.num, self.height)
    self.separator = Separator(self.separator_width , self.height, self.separator_color)

  def paint(self):
    self.g.x = self.width
    for applet in self.applets:
      self.g.x -= self.space
      if(self.separator_active):
        self.separator.paint(self.g)
        self.g.x -= self.space
      applet.paint(self.g)

    self.g.x -= self.space
    if(self.separator_active):
      self.separator.paint(self.g)
    self.g.send()


  def addApplet(self,applet):
    self.applets.append(applet)

