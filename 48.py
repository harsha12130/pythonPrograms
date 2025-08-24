Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(2,3,1,4,5,5)
t
(2, 3, 1, 4, 5, 5)
type(t)
<class 'tuple'>
len(t)
6
sum(t)
20
min(t)
1
max(t)
5
t+t
(2, 3, 1, 4, 5, 5, 2, 3, 1, 4, 5, 5)
t*3
(2, 3, 1, 4, 5, 5, 2, 3, 1, 4, 5, 5, 2, 3, 1, 4, 5, 5)
t1=(1,2,3)
t+t1
(2, 3, 1, 4, 5, 5, 1, 2, 3)
t+t1
(2, 3, 1, 4, 5, 5, 1, 2, 3)
t*t1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t*t1
TypeError: can't multiply sequence by non-int of type 'tuple'
t1*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(2, 3, 1, 4, 5, 5)
t[-1]
5
t[4]
5
t[-3]
4
t[2]
1
t[9]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t[9]
IndexError: tuple index out of range
t[1:5]
(3, 1, 4, 5)
t
(2, 3, 1, 4, 5, 5)
t[1:5:1]
(3, 1, 4, 5)
t[2:5:-1]
()
()
()
t[1:6:2]
(3, 4, 5)
t{6:2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
t[6:2]
()
t[1:5:0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t[1:5:0]
ValueError: slice step cannot be zero
t[-1:5;-1]
SyntaxError: invalid syntax
t[-1:5:-1]
()
>>> t[-1:-5:-1]
(5, 5, 4, 1)
>>> t[2]=10
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t[2]=10
TypeError: 'tuple' object does not support item assignment
>>> l=list(t)
>>> l
[2, 3, 1, 4, 5, 5]
>>> type(t)
<class 'tuple'>
>>> type(l)
<class 'list'>
>>> l.extend([10,20])
>>> l
[2, 3, 1, 4, 5, 5, 10, 20]
>>> t=tuple(l)
>>> type(t)
<class 'tuple'>
>>> t
(2, 3, 1, 4, 5, 5, 10, 20)
>>> t[::-1]
(20, 10, 5, 5, 4, 1, 3, 2)
>>> l[::-1]
[20, 10, 5, 5, 4, 1, 3, 2]
>>> t
(2, 3, 1, 4, 5, 5, 10, 20)
>>> t1
(1, 2, 3)
>>> t.count(5)
2
>>> t.clear()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> t.index(5)
4
>>> t.count(25)
0
>>> t
(2, 3, 1, 4, 5, 5, 10, 20)
>>> t1
(1, 2, 3)
>>> t2=("nikhil","klu","cse")
