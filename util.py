
def isBlank(char):
  return char == ' ' or char == '\t' or char == '\n'


def tokenizeFile(path):
  tokens = []
  
  f= open(path,'r')
  for line in f:
    for token in tokenize(line):
      tokens.append(token)
  f.close()

  return tokens



##
# Tokenize a string
# a token is a sequence of character separate by a blank
# or a sequence of characters surrounded by quotes ( ' or " ) 
# All characters between a # and a carriage return are omitted 
# @return an array of token
def tokenize(string):
  tokens = []
  deb = 0
  state = 0
  for i in range(len(string)):
    if( state == 0):
      if(not isBlank(string[i])):
        if(string[i] == '"'):
          deb = i+1
          state = 2
        elif(string[i] == "'"):
          deb = i+1
          state = 3
        elif(string[i] == "#"):
          state = 9
        else:
          deb = i
          state = 1

    elif( state == 1 ):
      if(isBlank(string[i])):
        tokens.append( string[deb: i] )
        state = 0
    
    elif( state == 2 ):
      if(string[i] == '"'):
        tokens.append( string[deb: i] )
        state = 0
  
    elif( state == 3 ):
      if(string[i] == "'"):
        tokens.append( string[deb: i] )
        state = 0

    elif( state == 9 ):
      if(string[i] == "\n"):
        state = 0

  if( state == 1 ):
    tokens.append(string[deb:i+1])

  return tokens

# End tokenize 
########################


