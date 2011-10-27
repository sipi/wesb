

class AppletModel(object):

  
  def __init__(self, refresh_period):
    self.refresh_period = refresh_period; #-1 => no refresh
    self.last_time = 0;

  def run(self, new_time):
    if (not self.refresh_period == -1) and new_time - self.last_time > self.refresh_period:
     self.last_time = new_time
     self.update()

  def update(self):
    raise NotImplementedError

    
