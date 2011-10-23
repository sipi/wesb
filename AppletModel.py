

class AppletModel(object):

  
  def __init__(self, refresh_time):
    self.refresh_time = refresh_time
    self.last_time = 0;

  def run(self, new_time):
    if (not self.refresh_time == -1) and new_time - self.last_time > self.refresh_time:
     self.last_time = new_time
     self.update()

  def update(self):
    raise NotImplementedError

    
