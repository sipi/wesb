
class AppletView(object):

  
  def __init__(self):
    self.refresh_period = 0.01

  def init(self):
    raise NotImplementedError

  def paint(self, x):
    raise NotImplementedError

  def getModel(self):
    return self.model
  
  def setModel(self, model):
    self.model = model
