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

def process_match(m):
    return '<li></li>'

print p.sub(process_match, s, re.S)

print p.sub('<li></li>', s, re.S)
print re.sub(r'<li>.*?</li>', '<li></li>', s, re.S)
