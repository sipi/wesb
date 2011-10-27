
import time

from AppletView import AppletView
from AppletModel import AppletModel

class clock(AppletView, AppletModel):
 
 
  def __init__(self):
    AppletView.__init__(self)
    AppletModel.__init__(self, 0.1)
    self.__text = ""
    self.color = "#FFFFFF"
    self.date_format = "%a %d %b %H:%M"

  def init(self):
    self.refresh_period = float(self.refresh_period)
    self.color = str(self.color)
    self.date_format = str(self.date_format)

  #Override AppletView
  def getModel(self):
    return self

  #Override AppletModel
  def update(self):
    self.__text = time.strftime(self.date_format)

  #Override AppletView
  def paint(self,g):
    g.x -= g.getTextLength(self.__text)
    g.drawText(self.__text,g.x,12,self.color); 
