def assert_test(num):
    try:
        num = int(num)
        assert num > 0
    except (AssertionError, Exception) as e:
        print('The number must be a positive integer,', e)


assert_test('1')
assert_test('0')
assert_test('a')

try:
    assert 1 > 2
except AssertionError as e:
    print('No error msg', e)

assert issubclass(AssertionError, Exception)
