#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import pprint
try:
    import simplejson as json
except ImportError:
    import json

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
pprint.pprint(obj, indent=4, width=1)
print json.dumps(obj, indent=4, sort_keys=True)

obj = json.dumps(obj)
print obj, type(obj)

json_str = "['foo', 'bar']"
obj = ast.literal_eval(json_str)
print obj, type(obj)

#json_str = '[true, false, null]'  # ValueError: malformed string
json_str = '[True, False, None]'
obj = ast.literal_eval(json_str)
print obj, type(obj)

unicode_info = {
    'name': u'李好',
    'style': u'צקלה',
}
print json.dumps(unicode_info)
print json.dumps(unicode_info, ensure_ascii=False)
dumpped_unicode = '{"style": "צקלה", "name": "李好"}'
data = json.loads(dumpped_unicode)
print data['name'], data['style']
dumpped_unicode = '{"style": "\u05e6\u05e7\u05dc\u05d4", "name": "\u674e\u597d"}'
data = json.loads(dumpped_unicode)
print data['name'], data['style']
