

class AppletModel(object):

  
  def __init__(self):
    self.refresh_period = 0.01; #-1 => no refres
    self.last_time = 0;

  def run(self, new_time):
    if (not self.refresh_period == -1) and new_time - self.last_time > self.refresh_period:
     self.last_time = new_time
     self.update()

  def update(self):
    raise NotImplementedError

    
