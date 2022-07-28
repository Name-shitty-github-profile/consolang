class Error(Exception):
  """
  The js error for error handling
  ```py
  from consolang import js
  console = js.console
  try:
    console.error("Hello,", "World !")
  except js.Error:
    console.log("Error handled !")
  """
  pass

def error(message: any, *optionalParams):
  '''
  Represent the `console.error()`, raise an the Error Exception when with the message you want to display
  '''
  message = str(message)
  for i in optionalParams: message += f'\n{str(i)}'
  raise Error(message)
