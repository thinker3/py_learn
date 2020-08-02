#!/usr/bin/env python
# encoding: utf-8


def for_exception_catch_outer():
    try:
        for i in range(10):
            if i % 3 == 0:
                raise Exception('Exception %s' % i)
            else:
                print(i)
    except Exception as e:
        print(e)


def for_exception_catch_inner():
    for i in range(10):
        try:
            if i % 3 == 0:
                raise Exception('Exception %s' % i)
            else:
                print(i)
        except Exception as e:
            print(e)

for_exception_catch_outer()
print('*' * 30)
for_exception_catch_inner()


def how_many_exceptions_catched():
    try:
        for i in range(10):
            try:
                if i % 3 == 0:
                    raise Exception('Exception %s' % i)
                else:
                    print(i)
            except Exception as e:
                print(e)
                raise e
    except Exception as e:
        pass

print('*' * 30)
how_many_exceptions_catched()


def throw():
    try:
        1 / 0
    #except:
    #    pass
    finally:
        pass

# throw()


def only_raise():
    try:
        what
    except:
        raise

only_raise()
