class Error(Exception):
  pass

def error(message: any, *optionalParams):
  '''
  Represent the `console.error()`, raise an the Error Exception when with the message you want to display
  '''
  message = str(message)
  for i in optionalParams: message += f'\n{str(i)}'
  raise Error(message)
