import json

foo = [1,2,3,4,5]
# print(json.dumps(foo))
# print(type(foo))
# print(type(json.loads(str(foo))))
bar = {"key1":"value1","key2":"value2"}

a = json.dumps(bar) # serialization
print(a)
print(type(a))
print(type(bar))
b = json.loads(a) # de-serialization
print(b)
print(type(b))
