#!/usr/bin/env python
# encoding: utf-8

import os
# path.py
# there is an alias called path, don't import that, no jedi hints
from path import Path as pathpy


def path_file_operations():
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

        new_name = pathpy.join(testfile.dirname(), 'abcd')  # problematic
        print new_name  # a/Users/kenb/Users/kenc/Users/kend

        new_name = os.path.join(testfile.dirname(), 'abcd')
        print new_name
        testfile.rename(new_name)  # no error even the file exists

    testfile.remove_p()

    for f in testdir.files():
        assert isinstance(f, pathpy)
        f.remove()
    testdir.rmdir()


def path_dir_operations():
    outer = pathpy('~/outertestdir').expanduser()
    assert isinstance(outer, pathpy)
    inner = pathpy('~/innertestdir').expanduser()
    copydir = pathpy('~/copytestdir').expanduser()
    assert isinstance(copydir, pathpy)
    if not outer.exists():
        outer.makedirs()
    if not inner.exists():
        inner.makedirs()
    '''
    # not need to makedirs for copytree
    if not copydir.exists():
        copydir.makedirs()
    '''

    testfile = os.path.join(inner, 'testfile')
    testfile = pathpy(testfile)
    testfile.touch()
    inner.move(outer)
    for d in outer.dirs():
        assert isinstance(d, pathpy)
        print d.dirname(), d.basename(), d
        #d.copy(copydir)  # IOError: [Errno 21] Is a directory
        dst = os.path.join(copydir, d.basename())
        d.copytree(dst)  # The destination directory must not already exist
        for f in d.files():
            f.remove()
        #d.remove()  # OSError: [Errno 1] Operation not permitted
        # removedirs() tries to successively remove every parent directory
        # mentioned in path until an error is raised
        #d.removedirs()
        d.rmdir()
    outer.rmdir()  # OSError: [Errno 66] Directory not empty
    copydir.rmtree_p()

#path_file_operations()
path_dir_operations()
