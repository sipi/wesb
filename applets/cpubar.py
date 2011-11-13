
from core.AppletView import AppletView
from CpuModel import CpuModel


class cpubar(AppletView):


  def __init__(self):
    AppletView.__init__(self)
    self.bar_width = 2
    self.space_width = 1
    self.border_size = 0
    self.bar_color = "#FF0000"
    self.bg_color = "#555555"
    self.border_color = "#000000"
    self.img_path = ""
    self.img_width = 0


  def init(self):
    self.refresh_period = float(self.refresh_period)
    self.bar_width = int(self.bar_width)
    self.space_width = int(self.space_width)
    self.border_size = int(self.border_size)
    self.bar_color = str(self.bar_color)
    self.bg_color = str(self.bg_color)
    self.border_color = str(self.border_color)
    self.img_path = str(self.img_path)
    self.img_width = int(self.img_width)
    self.setModel( CpuModel( self.refresh_period ) )
    self.__nbr_cpu = self.model.getNbrCpu()


  def paint(self, g):
    size = self.bar_width + self.space_width
    g.x -= size * self.__nbr_cpu 
    for i in range(1, self.__nbr_cpu + 1):
      g.drawVBar(g.x + (i-1)*size , 1, self.bar_width, g.height - 1, self.model.getCpuUsage(i)/100.0, self.bg_color, self.bar_color, self.border_color, self.border_size) 

    if(len(self.img_path) > 0):
      g.x -= self.img_width + self.space_width
      g.drawImg(g.x, 1, 0, 0, self.img_path)
