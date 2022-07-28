from sys import stdout
def log(message: any, *optionalParams) -> None:
  '''
  Represent the console.log of javascript work the same as javascript except it's not really formated because to learn python you need to use python formating a bit
  Only print the character in the params, here's an example
  ```python
  > console.log("Hello, world !");
  > Hello, world !
  > console.log("Hello,", " world !")
  > Hello, world !
  '''
  message = str(message)
  for i in optionalParams: message += f' {str(i)}'
  stdout.write(message + '\n')
