Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={3,1,2,3,5,1}
s
{1, 2, 3, 5}
type(s)
<class 'set'>
len(s)
4
min(s)
1
max(s)
5
s1={10,20}
s
{1, 2, 3, 5}
s1
{10, 20}
s+s
Traceback (most recent call last):
 File "<pyshell#9>", line 1, in <module>
 s+s
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s*3
Traceback (most recent call last):
 File "<pyshell#10>", line 1, in <module>
 s*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
s
{1, 2, 3, 5}
s[2]
Traceback (most recent call last):
 File "<pyshell#12>", line 1, in <module>
 s[2]
TypeError: 'set' object is not subscriptable
s2=set()
s2
set()
s
{1, 2, 3, 5}
s1
{10, 20}
s1={2,4}
s
{1, 2, 3, 5}
s1
{2, 4}
s.add(6)
s
{1, 2, 3, 5, 6}
s.add(1)
s
{1, 2, 3, 5, 6}
s2=s.copy()
s2
{1, 2, 3, 5, 6}
s.pop()
1
s
{2, 3, 5, 6}
s.pop()
2
s
{3, 5, 6}
s.discard(3)
s
{5, 6}
s.discard(10)
s
{5, 6}
s.remove(10)
Traceback (most recent call last):
 File "<pyshell#34>", line 1, in <module>
 s.remove(10)
KeyError: 10
s.remove(5)
s
{6}
s.update({1,2,3,6})
s
{2, 1, 3, 6}
s1={10,20}
s.update(s1)
s
{2, 1, 3, 6, 10, 20}
s1={3,4,6,10}
s
{2, 1, 3, 6, 10, 20}
s1
{10, 3, 4, 6}
s.union(s1)
{1, 2, 3, 4, 6, 10, 20}
s.intersection(s1)
{10, 3, 6}
s.difference(s1)
{1, 2, 20}
s1.difference(s)
{4}
s.isdisjoint(s1)
False
s.issubset(s1)
False
s.issuperset(s1)
False
s3={{1,2},{3}}
Traceback (most recent call last):
 File "<pyshell#52>", line 1, in <module>
 s3={{1,2},{3}}
TypeError: unhashable type: 'set'
s
{2, 1, 3, 6, 10, 20}
s1
{10, 3, 4, 6}
s.difference(s1)
{1, 2, 20}
s.difference_update(s1)
s
{2, 1, 20}
s1
{10, 3, 4, 6}
s.add(3)
s
{2, 1, 3, 20}
s1
{10, 3, 4, 6}
s.intersection(s1)
{3}
s.intersection_update(s1)
s
{3}
s.update({1,3,5})
s
{1, 3, 5}
s
s1
{10, 3, 4, 6}
>>> s.difference(s1)
{1, 5}
>>> s1.difference(s)
{10, 4, 6}
>>> s.symmetric_difference(s1)
{1, 4, 5, 6, 10}
>>> nameset={"surya","klu","ceo"}
>>> demoset={1,2.3,"surya",3}
>>> s.symmetric_difference_update(s1)
>>> s
{1, 4, 5, 6, 10}
