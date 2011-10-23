
class AppletView:

  def __init__(self, model):
    self.model = model

  def paint(self, g):
    raise NotImplementedError

  def getModel(self):
    return self.model
