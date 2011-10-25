
from AppletModel import AppletModel
from AppletView import AppletView

class Separator(AppletView, AppletModel):

  def __init__(self, width, height, color):
    AppletView.__init__(self)
    AppletModel.__init__(self)
    self.refresh_period = -1
    self.width = width
    self.height = height
    self.color = color

  def getModel(self):
    return self

  def paint(self, g):
    g.x -= 3
    g.drawRect(g.x, 0, self.width, self.height, self.color)

