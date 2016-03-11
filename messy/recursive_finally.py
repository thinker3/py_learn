print None < -1
print


denominators = [0,0,0,2,3,0,0,4,6,0,0,0,12,0,0]
max_id = len(denominators)

def divide(id):
    if id < max_id:
        sql = 'Hello, number %d' % id
        try:
            print '12/%d=%d' % (denominators[id], 12/denominators[id])
            print sql
            id += 1
            print sql # sql is not dynamic
            return id
        except:
            id += 1
            return divide(id) # The return here is important.
        finally:
            print '%d in finally' % id
    else:
        return max_id # This line is important

id = 0
while id < max_id:
    id = divide(id)
    print

