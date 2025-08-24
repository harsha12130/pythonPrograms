#program to convert PYthon objects to JSON strings

import json

print(json.dumps({"id":101,"name":"surya"}))
print(json.dumps(["klu","cse"]))
print(json.dumps(("klu","cse")))
print(json.dumps("klu"))
print(json.dumps(13))
print(json.dumps(13.45))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
