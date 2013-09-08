import signal
from time import sleep

class TimeoutException(Exception):
    pass

def do_something_else(**kwargs):
    time = kwargs['time']
    sleep(time)
    return 'do_something_else has to run for %d seconds' % time

def handler(signum, frame):
    raise TimeoutException 

def do_something_with_timeout(timeout, callback, **kwargs):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    try:
        value = callback(**kwargs)
        signal.alarm(0)
        return value
    except TimeoutException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return 'time out'

def main():
    print 'hello'
    print do_something_with_timeout(3, do_something_else, time=2)
    print 'world'

main()
