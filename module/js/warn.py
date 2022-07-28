from warnings import warn as warne
def warn(message, *optionalParams) -> None:
  message = str(message)
  message.replace('%d', '')
  for i in optionalParams: message += f' {str(i)}'
  warne(message + '\n')
