#!/usr/bin/env python
# encoding: utf-8

import os
# path.py
# there is an alias called path, don't import that, no jedi hints
from path import Path as pathpy


def path_move():
    testdir = pathpy('~/testdir').expanduser()
    print type(testdir)

    assert isinstance(testdir, pathpy)
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
    #print pathpy.expanduser('~/temp')

    testfile = pathpy('~/testfile').expanduser()
    assert isinstance(testfile, pathpy)

    if not testfile.exists():
        testfile.touch()
        testfile.move(testdir)

    testfile = pathpy('~/testfile2').expanduser()
    if not testfile.exists():
        testfile.touch()
        pathpy.move(testfile, testdir)

    testfile = pathpy('~/testfile3').expanduser()
    if not testfile.exists():
        testfile.touch()
        r = pathpy.copy(testfile, testdir)
        print 'New path is %s' % r  # None
        #testfile.rename('abcd')  # move to the working folder and renamed

        # TypeError: descriptor 'join' requires a 'unicode' object but received a 'list'
        #new_name = pathpy.join([testfile.dirname(), 'abcd'])

        new_name = pathpy.join(testfile.dirname(), 'abcd')
        print new_name  # a/Users/kenb/Users/kenc/Users/kend

        new_name = os.path.join(testfile.dirname(), 'abcd')
        print new_name
        testfile.rename(new_name)  # no error even the file exists

    testfile.remove_p()

    for f in testdir.files():
        assert isinstance(f, pathpy)
        f.remove()
    testdir.rmdir()

path_move()
