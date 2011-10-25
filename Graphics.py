import os

WMFS_BIN_PATH = "/usr/local/bin/wmfs"

class Graphics:

  def __init__(self, num_screen):
    self.value = ""
    self.num_screen = num_screen #All screen 
    self.x = 0;


  def send(self):
    command = WMFS_BIN_PATH + " -s "
    if self.num_screen >= 0:
      command += str(self.num_screen) + " "
      
    os.system(command + "'" + self.value + " '")
    self.value = ""


  def getTextLength(self, text):
    return int(len(text)*7.5)
    
  def drawText(self, text, x, y, color):
    self.value += "\\s["+str(x)+";"+str(y)+";"+color+";"+text+"]\\"  #\\s[x;y;color;text]\\

  def drawRect(self, x, y, width, height, color):
    self.value += "\\b["+str(x)+";"+str(y)+";"+str(width)+";"+str(height)+";"+color+"]\\"

  ##
  # draw a Horizontal percent bar
  # @param percent the percent between 0 and 1
  def drawHBar(self, x, y, width, height, percent, bg_color, fg_color, border_color, border_size = 1):
    self.drawRect( x, y, width, height, border_color)
    self.drawRect( x + border_size, y + border_size, width - 2*border_size, height - 2*border_size, bg_color)  
    self.drawRect( x + border_size, y + border_size, int((width - 2*border_size)*percent), height - 2*border_size, fg_color)
  
  ##
  # draw a vertical percent bar
  # @param percent the percent between 0 and 1
  def drawVBar(self, x, y, width, height, percent, bg_color, fg_color, border_color, border_size = 1):
    self.drawRect( x, y, width, height, border_color)
    self.drawRect( x + border_size, y + border_size, width - 2*border_size, height - 2*border_size, bg_color)  
    self.drawRect( x + border_size, y + border_size, width - 2*border_size, (height - 2*border_size)*percent, fg_color)
