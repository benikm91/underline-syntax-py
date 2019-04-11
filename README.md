# Underline Syntax

Underline syntax enables shorter lambda syntax for python (inspired by Scala).

First import:

```python
from pyext.underline_syntax.underline_syntax import __
```

Then use it:

```python
map(__ + 5, [5, 10, 15])
# instead of 
map(lambda x: x + 5, [5, 10, 15])
```

Or 

```python
map(__.upper(), ['Hello', 'World'])
# instead of 
map(lambda x: x.upper(), ['Hello', 'World'])
```

There are some problems with instance variables. You have to call .done() to signal the end:

```python
class A:
    @property
    def inner(self):
        return "inner"
map(__.inner.done(), [A()])
# instead of
map(lambda a: a.inner, [A()])
```
