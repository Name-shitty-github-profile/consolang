class Error(Exception):
  pass

def error(message: any, *optionalParams):
  message = str(message)
  message.replace('%d', '')
  for i in optionalParams: message += f'\n{str(i)}'
  raise Error(message)
