
import time

from AppletView import AppletView
from AppletModel import AppletModel

class Clock(AppletView, AppletModel):
 
 
  def __init__(self):
    AppletView.__init__(self, self)
    AppletModel.__init__(self, 10)
    self.text = ""

  def getModel(self):
    return self

  def update(self):
    self.text = time.strftime("%a %d %b %H:%M")

  def paint(self,g):
    g.x -= g.getTextLength(self.text)
    g.drawText(self.text,g.x,12,"#FFFFFF"); 
