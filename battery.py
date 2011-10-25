
from AppletView import AppletView
from BatteryModel import BatteryModel

class battery(AppletView):

  
  
  def __init__(self):
    AppletView.__init__(self)
    self.num_bat = 0
    self.active_blink = True
    self.periode_blink = 30
    self.count_blink = 0
    self.border_color = "#FFFFFF"
    self.background_color = "#555555"
    self.barcolor_charge = "#FFFFFF"
    self.barcolor_normal = "#00FF00"
    self.barcolor_medium = "#FF6F00"
    self.barcolor_low = "#FF0000"

  def init(self):
    self.refresh_period = float(self.refresh_period)
    self.num_bat = int(self.num_bat)
    self.active_blink = bool(self.active_blink)
    self.periode_blink = int(self.periode_blink)
    self.border_color = str(self.border_color)
    self.background_color = str(self.background_color)
    self.barcolor_charge = str(self.barcolor_charge)
    self.barcolor_normal = str(self.barcolor_normal)
    self.barcolor_medium = str(self.barcolor_medium)
    self.barcolor_low = str(self.barcolor_low)
    self.setModel( BatteryModel( self.num_bat, self.refresh_period ) ) 

  def paint(self, g):
    percent = self.model.getPercent()
    blink = False
    self.barcolor = self.barcolor_charge
    if self.model.isDischarging():
      self.barcolor = self.barcolor_normal
      if percent < 30:
        if percent < 15:
          self.barcolor = self.barcolor_low
          blink = self.active_blink
        else:
          self.barcolor = self.barcolor_medium
    
    if blink:
      self.count_blink += 1
      if self.count_blink > self.periode_blink:
        self.count_blink = 0


    g.x -= 37
    if (not blink) or self.count_blink > self.periode_blink/2:
      self.__drawBatteryBar(g, self.model.getPercent(), 2, 30, 11) 



  def __drawBatteryBar(self, g, percent, y, width, height):
    g.drawHBar(g.x + 2, y, width, height, percent/100.0, self.background_color, self.barcolor, self.border_color);
    g.drawRect(g.x + 2 + width, y + (height/3), 2, height/2, self.border_color) 
