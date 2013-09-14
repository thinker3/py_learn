import re
p = re.compile(r'abc')
s = '123 abc abc efg'
print p.findall(s)
s = '123 abc abc abc abc efg'
print p.findall(s)

s = '''
    <ul>
        <li>something</li>
        <li>something else</li>
        <li>and more</li>
        <li>even more</li>
    </ul>
    '''

p = re.compile(r'<li>.*?</li>')
print p.findall(s)
p = re.compile(r'<li>(.*?)</li>')
print p.findall(s)

