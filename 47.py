Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={"id":4654,'name':'surya',101:102}
type(d)
<class 'dict'>
len(d)
3
d1=d.copy()
d1
{'id': 4654, 'name': 'surya', 101: 102}
d1.clear()
d1
{}
d
{'id': 4654, 'name': 'surya', 101: 102}
d.items()
dict_items([('id', 4654), ('name', 'surya'), (101, 102)])
d.keys()
dict_keys(['id', 'name', 101])
type(d.keys())
<class 'dict_keys'>
d.values()
dict_values([4654, 'surya', 102])
d.get(101)
102
d.get(id)
d.get('id')
4654
d.get('location')
d['id']
4654
d[101]
102
d["location"]
Traceback (most recent call last):
 File "<pyshell#18>", line 1, in <module>
 d["location"]
KeyError: 'location'
d1=d.copy()
d1
{'id': 4654, 'name': 'surya', 101: 102}
d
{'id': 4654, 'name': 'surya', 101: 102}
d1
{'id': 4654, 'name': 'surya', 101: 102}
d.popitem()
(101, 102)
d1.pop(101)
102
d1
{'id': 4654, 'name': 'surya'}
d
{'id': 4654, 'name': 'surya'}
d1.pop("location")
Traceback (most recent call last):
 File "<pyshell#27>", line 1, in <module>
 d1.pop("location")
KeyError: 'location'
d
{'id': 4654, 'name': 'surya'}
d
1
1
d
{'id': 4654, 'name': 'surya'}
d1
{'id': 4654, 'name': 'surya'}
d.setdefault('id')
4654
d.setdefault('location')
d
{'id': 4654, 'name': 'surya', 'location': None}
d.get('location')='vja'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead
of '='?
d['location']='vja'
d
{'id': 4654, 'name': 'surya', 'location': 'vja'}
type(d['name

SyntaxError: incomplete input
type(d['name'])

<class 'str'>
d

{'id': 4654, 'name': 'surya', 'location': 'vja'}
d.setdefault('gender')

d

{'id': 4654, 'name': 'surya', 'location': 'vja', 'gender': None}
d['gender']='male'

d

{'id': 4654, 'name': 'surya', 'location': 'vja', 'gender': 'male'}
type(d.get['gender'])

Traceback (most recent call last):
 File "<pyshell#45>", line 1, in <module>
 type(d.get['gender'])
TypeError: 'builtin_function_or_method' object is not subscriptable
type(d.get('gender'))

<class 'str'>
d.update({"cgpa":2})

d

{'id': 4654, 'name': 'surya', 'location': 'vja', 'gender': 'male', 'cgpa': 2}
d.update({"name":"klu","maritalstatus":True})

d

{'id': 4654, 'name': 'klu', 'location': 'vja', 'gender': 'male', 'cgpa': 2, 'maritalstatus':
True}
>>> d
...
{'id': 4654, 'name': 'klu', 'location': 'vja', 'gender': 'male', 'cgpa': 2, 'maritalstatus':
True}
>>> len(d)
...
6
>>> d.keys()
...
dict_keys(['id', 'name', 'location', 'gender', 'cgpa', 'maritalstatus'])
>>> d.setdefault('cgpa')
...
2
