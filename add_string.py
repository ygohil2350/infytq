#lex_auth_0127135739583692801137

def add_string(str1):
  #start writing your code here
  length = len(str1)
  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  

  
  return str1

str1="com"
print(add_string(str1))
