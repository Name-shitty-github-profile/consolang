from .log import log
from .assertt import assertt
from .clear import clear
from .debug import debug
from .error import error
from .count import count, countReset
class console:
  info = log = log
  assertt = assertt
  clear = clear
  debug = debug
  error = error
  count = count
  countReset = countReset
