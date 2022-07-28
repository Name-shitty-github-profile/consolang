from sys import stdout
def info(message: any, *optionalParams) -> None:
  '''
  The `console.info()` function is an alias for `console.log`.
  '''
  message = str(message)
  for i in optionalParams: message += f' {str(i)}'
  stdout.write(message + '\n')
