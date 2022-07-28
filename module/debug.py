from .log import log
def debug(message: any, *optionalParams) -> None:
  log(message, *optionalParams)
