
from AppletView import AppletView
from BatteryModel import BatteryModel

class Battery(AppletView):

  def __init__(self, bat_num):
    AppletView.__init__(self, BatteryModel(bat_num))

    self.active_blink = True
    self.periode_blink = 30
    self.count_blink = 0
    self.border_color = "#FFFFFF"
    self.background_color = "#555555"
    self.barcolor_charge = "#FFFFFF"
    self.barcolor_normal = "#00FF00"
    self.barcolor_medium = "#FF6F00"
    self.barcolor_low = "#FF0000"
    self.barcolor = self.barcolor_charge



  def paint(self, g):
    percent = self.model.getPercent()
    blink = False
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
    g.drawHBar(g.x + 2, y, width, height, percent/100, self.background_color, self.border_color, self.barcolor);
    g.drawRect(g.x + 2 + width, y + (height/3), 2, height/2, self.border_color) 
