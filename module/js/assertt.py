from .log import log
def assertt(value: bool, message, *optionalParams) -> None:
  if value is False:
    log(message, *optionalParams)
