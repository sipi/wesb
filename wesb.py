
import sys
from time import time, sleep

import util
from Screen import Screen
from AppletView import AppletView
from AppletModel import AppletModel
from Graphics import Graphics
from Separator import Separator

###########################
#  FUNCTIONS              #
###########################

def readConf(path):
  tokens = util.tokenizeFile(path)
  
  screens = []
  state = 0
  i = -1
  while i < len(tokens) - 1:
    i += 1
    token = tokens[i]

    if(state == 0):
      if(token == '[screen]'):
        screen = Screen()
        screens.append(screen)
        state = 1;
  
    elif(state == 1):
      if(token == '[/screen]'):
        state = 0
      elif(token[0] == "["): #add an applet to the current screen
        package_name = "applets."
        module_name = token[1:-1]
        mod = __import__(package_name + module_name)
        applet = getattr(sys.modules[package_name + module_name], module_name)()
        screen.addApplet(applet)
        state = 2
      else:
        screen.__setattr__(token, tokens[i+2]) #set an attribut of the current screen
        i += 2
  
    elif(state == 2):
      if(token == '[/' + module_name + ']'):
        state = 1
      else:
        applet.__setattr__(token, tokens[i+2]) #set an attribut of the current applet
        i += 2

  return screens

# End readConf
################


##############################
#  MAIN                      #
##############################

screens = readConf("wesb.conf")
applets_models = set()

for screen in screens:
  screen.init()
  for applet in screen.applets:
    applet.init()
    applets_models.add(applet.getModel())


############
# MAIN LOOP
while True: 
  sleep(0.1)

  new_time = time()
  for model in applets_models:
    model.setTime(new_time) #triggers the update if necessary
    
  for screen in screens:
    screen.paint()


