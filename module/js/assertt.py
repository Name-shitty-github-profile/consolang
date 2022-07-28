from .log import log
def assertt(value: bool, message: any = "Assertion failed", *optionalParams) -> None:
  '''
  Represent `console.assert()`<br>
  The value tested for being truthy.<br>

console.assert() writes a message if value is falsy or omitted. It only writes a message and does not otherwise affect execution. The output always starts with "Assertion failed". If provided, message is will be displayed in the console.<br>

If value is truthy, nothing happens.
```python
console.assert(true, 'does nothing');

console.assert(false, 'Whoops %s work', 'didn\'t');
# Assertion failed: Whoops didn't work

console.assert();
# Assertion failed
```
  '''
  if not value:
    log(message if message == "Assertion failed" else "Assertion failed" + message, *optionalParams)
