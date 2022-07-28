from sys import stdout
def log(message: any, *optionalParams) -> None:
  message = str(message)
  message.replace('%d', '')
  for i in optionalParams: message += f' {str(i)}'
  stdout.write(message + '\n')
