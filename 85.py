Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> value=re.match("^klu","kluniversity")
>>> value
<re.Match object; span=(0, 3), match='klu'>
>>> value=re.match("^klu","klef")
>>> value
>>> value=re.match("klu$","cseklu")
>>> value
>>> value=re.search("klu$","cseklu")
>>> value
<re.Match object; span=(3, 6), match='klu'>
>>> value=re.search("k*","kluniversity")
>>> value
<re.Match object; span=(0, 1), match='k'>
>>> value=re.search("k+","luniversity")
>>> value
>>> value=re.search("k+","kluniversity")
>>> value
<re.Match object; span=(0, 1), match='k'>
>>> value=re.search("[a-z]+","abc123")
>>> value
<re.Match object; span=(0, 3), match='abc'>
>>> value=re.search("[a-z]+","123")
>>> value
>>> value=re.search("k?lu","lu")
>>> value
<re.Match object; span=(0, 2), match='lu'>
>>> value=re.search("k?lu","klu")
>>> value
<re.Match object; span=(0, 3), match='klu'>
>>> value=re.search("k{3}lu","kkklu")
>>> value
<re.Match object; span=(0, 5), match='kkklu'>
>>> value=re.search("k{3}lu","klu")
>>> value
>>> value=re.search("klu | cse","klu")
>>> value
>>> value=re.search("klu|cse","klu")
>>> value
<re.Match object; span=(0, 3), match='klu'>
>>> value=re.search("klu|cse","klef")
>>> value
>>> value=re.search("[a-z][0-9]","a1")
>>> value
<re.Match object; span=(0, 2), match='a1'>
value=re.search("klu.cse","klucse")
value
value=re.search("klu.cse","kluacse")
value
<re.Match object; span=(0, 7), match='kluacse'>
value=re.search("klu..cse","kluabcse")
value
<re.Match object; span=(0, 8), match='kluabcse'>
value=re.search("klu\d{3}","klu123")
value
<re.Match object; span=(0, 6), match='klu123'>
value=re.search("klu*","klucseklu")
value
<re.Match object; span=(0, 3), match='klu'>
value=re.findall("klu*","klucseklu")
value
['klu', 'klu']
value=re.findall("klu{2}cse?","kluucs")
value
['kluucs']
value=re.findall("klu{2}cse?","kluucscsekluucse")
value
['kluucs', 'kluucse']
value=re.sub("klu|cse","KLEF","klu")
value
'KLEF'
value=re.sub("klu*","CSE","klucseklu")
value
'CSEcseCSE'
import re
text="My native place is vizag"
value=re.split('a',text)
value
['My n', 'tive pl', 'ce is viz', 'g']
value=re.split('a',text,1)
value
['My n', 'tive place is vizag']
value=re.split('a',text,2)
value
['My n', 'tive pl', 'ce is vizag']
value=re.search("klu|cse","KLUCsE")
value
value=re.search("klu|cse","KLUCsE",re.IGNORECASE)
value
<re.Match object; span=(0, 3), match='KLU'>
