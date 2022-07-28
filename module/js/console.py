from .log import log
from .assertt import assertt
from .clear import clear
from .debug import debug
from .error import error
from .count import count, countReset
from .warn import warn
from .dirxml import dirxml
from .info import info
class console:
  """
  Represent the javascript console, not everything is coverred but the most important are !
  """
  info = info
  dirxml = dirxml
  log = log
  assertt = assertt
  clear = clear
  debug = debug
  error = error
  count = count
  countReset = countReset
  warn = warn
