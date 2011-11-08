
from core.AppletModel import AppletModel

try:
  import alsaaudio as alsa
except:
  print "Module alsaaudio not found"

class SoundModel(AppletModel):

  def __init__(self, refresh_period):
    AppletModel.__init__(self, refresh_period)
    self.__vol = 0


  def getVol(self):
    return self.__vol


  def update(self):
    self.__vol = alsa.Mixer('Master').getvolume()[0]
