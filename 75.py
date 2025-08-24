Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import math
math.pi
3.141592653589793
import math as m
m.pi
3.141592653589793
m.exp
<built-in function exp>
m.exp(1)
2.718281828459045
m.exp(0)
1.0
m.factorial(5)
120
m.log(2)
0.6931471805599453
math.log10(2)
0.3010299956639812
math.pow(2,3)
8.0
math.remainder(10,20)
10.0
math.remainder(10,2)
0.0
math.sqrt(3)
1.7320508075688772
math.sqrt(25)
5.0
math.ciel(5.2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    math.ciel(5.2)
AttributeError: module 'math' has no attribute 'ciel'
>>> math.ciel(5.2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    math.ciel(5.2)
AttributeError: module 'math' has no attribute 'ciel'
>>> math.ceil(5.2)
6
>>> m.ceil(5.25)
6
>>> math.floor(4.2)
4
>>> math.trunc(10.23)
10
>>> math.trunc(10.6)
10
>>> math.isfinite(10/0)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    math.isfinite(10/0)
ZeroDivisionError: division by zero
>>> math.isfinte(10/2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    math.isfinte(10/2)
AttributeError: module 'math' has no attribute 'isfinte'. Did you mean: 'isfinite'?
>>> math.isfinite(10/2)
True
>>> math.isnan("surya")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    math.isnan("surya")
TypeError: must be real number, not str
>>> eal number, not str
... >>> m
SyntaxError: invalid syntax
>>>  math.isnan(12)
...  
SyntaxError: unexpected indent
>>> math.isnan(12)
False
>>> math.isfinite(10/3)
True
>>> round(2.345,2)
2.35
>>> round(2.34,1)
2.3
