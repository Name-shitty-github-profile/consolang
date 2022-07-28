from sys import stdout
def log(message: any, *optionalParams) -> None:
  message.replace('%d', '')
  for i in optionalParams: message += i
  stdout.write(message + '\n')
