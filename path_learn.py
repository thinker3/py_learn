#!/usr/bin/env python
# encoding: utf-8

import os
from path import Path as path


def path_move():
    testdir = path('~/testdir').expanduser()
    print type(testdir)

    assert isinstance(testdir, path)
    testdir = testdir.normpath()
    print type(testdir)

    abspath = testdir.abspath()
    basename = testdir.basename()
    print type(abspath)
    print type(basename)

    print testdir[2:]
    print 'test' in basename

    if not testdir.exists():
        testdir.makedirs()

    # TypeError: unbound method expanduser() must be called with Path instance
    # as first argument (got str instance instead)
    #print path.expanduser('~/temp')

    testfile = path('~/testfile').expanduser()
    assert isinstance(testfile, path)

    if not testfile.exists():
        testfile.touch()
        testfile.move(testdir)

    testfile = path('~/testfile2').expanduser()
    if not testfile.exists():
        testfile.touch()
        path.move(testfile, testdir)

    testfile = path('~/testfile3').expanduser()
    if not testfile.exists():
        testfile.touch()
        path.copy(testfile, testdir)
        #testfile.rename('abcd')  # move to the working folder and renamed

        # TypeError: descriptor 'join' requires a 'unicode' object but received a 'list'
        #new_name = path.join([testfile.dirname(), 'abcd'])

        new_name = path.join(testfile.dirname(), 'abcd')
        print new_name  # a/Users/kenb/Users/kenc/Users/kend

        new_name = os.path.join(testfile.dirname(), 'abcd')
        print new_name
        testfile.rename(new_name)  # no error even the file exists

    testfile.remove_p()

    for f in testdir.files():
        assert isinstance(f, path)
        f.remove()
    testdir.rmdir()

path_move()
