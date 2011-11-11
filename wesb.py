#    WESB - Wmfs extensible status bar
#
#    Copyright (C) 2011  Clement Sipieter <c.sipieter@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    
import sys
import os
from time import time, sleep

import core.util as util
from core.Screen import Screen
from core.AppletView import AppletView
from core.AppletModel import AppletModel
from core.Graphics import Graphics
from core.Separator import Separator

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

home_path = os.environ['HOME']

try:
  screens = readConf(home_path + "/.config/wmfs/wesb.conf")
except IOError:
  screens = readConf("./wesb.conf")


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


