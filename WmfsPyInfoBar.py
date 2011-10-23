
import time #sleep
from Screen import Screen
from AppletView import AppletView
from AppletModel import AppletModel
from Graphics import Graphics
from Separator import Separator

applets_views = []
applets_models = set()

f= open('WmfsPyInfoBar.conf','r')
for line in f:
  tokens = line.split()
  name = tokens[0]
  mod = __import__(name)
  if len(tokens) == 1:
    instance = getattr(mod, name)()
  else: 
    instance = getattr(mod, name)(tokens[1])
  applets_views.append(instance)
  applets_models.add(instance.getModel())


f.close()



screen_width = 1366;
g = Graphics()
separator = Separator(1,16, '#AAAAAA')

while 1==1:
  time.sleep(0.01)
  g.x = screen_width

  new_time = time.time()
  for model in applets_models:
    model.run(new_time)
    
  for app in applets_views:
    separator.paint(g)
    app.paint(g);

  g.send() 
