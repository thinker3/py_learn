## {{{ http://code.activestate.com/recipes/578481/ (r1)
def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    c = eval(eq1,{var:1j})
    return -c.real/c.imag
## end of http://code.activestate.com/recipes/578481/ }}}

print solve("2*x = 6")