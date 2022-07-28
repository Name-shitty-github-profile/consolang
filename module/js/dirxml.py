from .log import log
def dirxml(*optionalParams) -> None:
  '''
  This method calls `console.log()` passing it the arguments received. This method does not produce any XML formatting.
  '''
  log(*optionalParams)
