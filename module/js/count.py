from .log import log

labels: dict = {}

def count(label: str = 'Default') -> None:
  global labels
  if label not in labels: labels[label]: int = 0
  labels[label] += 1
  log(label + ":", labels[label])

def countReset(label: str = "Default") -> None:
  global labels
  labels[label]: int = 0
