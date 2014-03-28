import simplejson as json

json_str = '["foo", "bar"]'
obj = json.loads(json_str)
print obj, type(obj)

json_str = "['foo', 'bar']"  # simplejson.decoder.JSONDecodeError
json_str = json_str.replace("'", '"')
obj = json.loads(json_str)
print obj, type(obj)

#json_str = '[True, False, None]'  # error
json_str = '[true, false, null]'
obj = json.loads(json_str)
print obj, type(obj)

json_str = '["foo", {"bar":["baz", null, 1.0, 2]}]'
obj = json.loads(json_str)
print obj, type(obj)

obj = json.dumps(obj)
print obj, type(obj)

import ast
json_str = "['foo', 'bar']"
obj = ast.literal_eval(json_str)
print obj, type(obj)

#json_str = '[true, false, null]'  # ValueError: malformed string
json_str = '[True, False, None]'
obj = ast.literal_eval(json_str)
print obj, type(obj)
