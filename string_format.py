name = 'chen kun'

print 'hello %s' % name

# named parameters string formatting
print 'hello %(name)s' % {'name': name}
print 'hello %(name)s' % dict(name=name)


dic=dict(a='abc', b='bcd', c='cde')
print dic
