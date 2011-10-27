
from AppletModel import AppletModel

class BatteryModel(AppletModel):

  
  def __init__(self, bat_num, refresh_period):
    AppletModel.__init__(self, refresh_period)
    self.bat_num = bat_num
    self.is_discharging = False
    self.bat_dir = "/sys/class/power_supply/BAT"+str(self.bat_num)+"/"
    self.energy_full = 0
    self.energy_now = 0
    self.percent = 100
    self.__initEnergyFull()


  def getBatNum(self):
    return self.bat_num

  def isDischarging(self):
    return self.is_discharging

  def getPercent(self):
    return self.percent

  def update(self):
    self.__updateStatus()
    self.__updateEnergyNow()
    self.percent = (self.energy_now * 100) / self.energy_full


  def __updateStatus(self):
    f = open(self.bat_dir+"status", "r")
    if 'D' == f.readline()[0]:
      self.is_discharging = True
    else:
      self.is_discharging = False
    f.close()

  def __updateEnergyNow(self):
    f = open(self.bat_dir+"energy_now", "r")
    self.energy_now = int(f.readline())
    f.close()

  def __initEnergyFull(self):
    f = open(self.bat_dir+"energy_full", "r")
    self.energy_full = int(f.readline())
    f.close()



