import signal

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def nonBlockingRawInput(prompt='', timeout=5):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = input(prompt)
        signal.alarm(0)
        return text
    except AlarmException:
        print('\nPrompt timeout. Continuing...')
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

print(nonBlockingRawInput())
print('hello')
