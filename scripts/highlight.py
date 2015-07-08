from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter

code = 'print "Hello World"'
print highlight(code, PythonLexer(), RtfFormatter())
