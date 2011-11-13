
from core.AppletView import AppletView
from SoundModel import SoundModel


class sound(AppletView):


  def __init__(self):
    AppletView.__init__(self)
    self.width = 40
    self.height = 10
    self.border_size = 1
    self.bar_color = "#3F8EB4"
    self.bg_color = "#555555"
    self.border_color = "#000000"
    self.img_path = ""
    self.img_width = 0


  def init(self):
    self.refresh_period = float(self.refresh_period)
    self.width = int(self.width)
    self.height = int(self.height)
    self.border_size = int(self.border_size)
    self.bar_color = str(self.bar_color)
    self.bg_color = str(self.bg_color)
    self.border_color = str(self.border_color)
    self.img_path = str(self.img_path)
    self.img_width = int(self.img_width)
    self.setModel( SoundModel( self.refresh_period ) )


  def paint(self, g):
    g.x -= self.width
    y = (g.height - self.height) / 2
    g.drawHBar(g.x, y, self.width, self.height, self.model.getVol()/100.0, self.bg_color, self.bar_color, self.border_color, self.border_size);
    
    if(len(self.img_path) > 0):
      g.x -= self.img_width
      g.drawImg(g.x, 1, 0, 0, self.img_path); 
