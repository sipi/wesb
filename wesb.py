
import time #sleep
from Screen import Screen
from AppletView import AppletView
from AppletModel import AppletModel
from Graphics import Graphics
from Separator import Separator

screens = []
applets_models = set()

#Tokenize

def isBlank(char):
  return char == ' ' or char == '\t' or char == '\n'

def tokenize(line):
  tokens = []
  deb = 0
  state = 0
  for i in range(len(line)):
    if( state == 0):
      if(not isBlank(line[i])):
        if(line[i] == '"'):
          deb = i+1
          state = 2
        elif(line[i] == "'"):
          deb = i+1
          state = 3
        elif(line[i] == "#"):
          state = 9
        else:
          deb = i
          state = 1

    elif( state == 1 ):
      if(isBlank(line[i])):
        tokens.append( line[deb: i] )
        state = 0
    
    elif( state == 2 ):
      if(line[i] == '"'):
        tokens.append( line[deb: i] )
        state = 0
  
    elif( state == 3 ):
      if(line[i] == "'"):
        tokens.append( line[deb: i] )
        state = 0

    elif( state == 9 ):
      if(line[i] == "\n"):
        state = 0

  if( state == 1 ):
    tokens.append(line[deb:i+1])

  return tokens

# End tokenize 
########################


tokens = []
f= open('wesb.conf','r')
for line in f:
  for token in tokenize(line):
    tokens.append(token)
f.close()


state = 0;
i = -1;
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
    elif(token[0] == "["):
      module_name = token[1:-1]
      mod = __import__(module_name)
      applet = getattr(mod, module_name)()
      screen.addApplet(applet)
      state = 2
    else:
      screen.__setattr__(token, tokens[i+2])
      i += 2
  
  elif(state == 2):
    if(token == '[/' + module_name + ']'):
      state = 1
    else:
      applet.__setattr__(token, tokens[i+2])
      i += 2
  #applets_views.append(instance)
  #applets_models.add(instance.getModel())


for screen in screens:
  screen.init()
  for applet in screen.applets:
    applet.init()
    applets_models.add(applet.getModel())



while 1==1:
  time.sleep(0.1)

  new_time = time.time()
  for model in applets_models:
    model.run(new_time)
    
  for screen in screens:
    screen.run()    

