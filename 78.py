Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random()
0.11563476113757354
>>> random.random()
... 
0.7110426749832398
>>> random.random()
... 
0.31192021825471883
>>> random.randint(10,50)
19
>>> print(random.randint(10,50))
16
>>> random.randint(10,50)
18
>>>  random.randint(10,50)
...  
SyntaxError: unexpected indent
>>> random.randint(10,50)
16
>>> l=[10,20,30,40,50]
>>> type(l)
<class 'list'>
>>> l[::-1}#slice operator
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l[::-1]
[50, 40, 30, 20, 10]
>>> random.choice(l)
50
>>> random.choice(l)
20
>>> random.shuffle(l)
>>> l
[40, 30, 10, 50, 20]
>>> random.randrange(1,10)
6
>>> random.randrange(1,10,2)
9
>>> random.randrange(-1,-2,-1)
-1
>>> random.choice(l)
10
>>> l
[40, 30, 10, 50, 20]
random.choices(l,k=2)
[30, 20]
random.choices(l,k=3)
[50, 10, 20]
