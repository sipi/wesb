
from core.AppletModel import AppletModel
from core.util import array2d, array

class CpuModel(AppletModel):

  def __init__(self, refresh_period):
    AppletModel.__init__(self, refresh_period)
    self.__stat_path = "/proc/stat"
    self.__nbr_cpu = self.__countNbrCpu()
    self.__cpu_usage = array( self.__nbr_cpu + 1, 0)
    self.__old_cpu_stat = array2d( self.__nbr_cpu + 1, 2, 0)

  def __countNbrCpu(self):
    nbr = -1
    f = open(self.__stat_path)
    while(f.readline()[0] == 'c'):
      nbr += 1
    
    f.close()
    return nbr

  def getNbrCpu(self):
    return self.__nbr_cpu

  def getCpuUsage(self, cpu):
    return self.__cpu_usage[cpu]

  def update(self):
    f = open("/proc/stat")
    new_cpu_stat = array2d( self.__nbr_cpu + 1, 2, 0)
    
    for i in xrange(self.__nbr_cpu + 1):
      s = f.readline()
      tab = s.split() 
      new_cpu_stat[i][0] = int(tab[1]) + int(tab[2]) + int(tab[3])
      new_cpu_stat[i][1] = int(tab[4])

    f.close()

    for i in xrange(self.__nbr_cpu + 1):
      other_time = new_cpu_stat[i][0] - self.__old_cpu_stat[i][0]
      idle_time = new_cpu_stat[i][1] - self.__old_cpu_stat[i][1]
      try:
        self.__cpu_usage[i] = (other_time*100) / (other_time + idle_time)
      except ZeroDivisionError:
        self.__cpu_usage[i] = 0;

    self.__old_cpu_stat = new_cpu_stat

