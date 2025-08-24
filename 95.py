#program to convert from PYthon to JSON

import json

demo={"id":101,"name":"surya","age":25}
print(demo)
print(type(demo))

demo1=json.dumps(demo)

print(demo1)


print(type(demo1))
