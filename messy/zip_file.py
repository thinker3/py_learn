#!/usr/bin/env python
# encoding: utf-8

import os
import zipfile

dirname = os.path.dirname(os.path.abspath(__file__))
target_dirname = os.path.expanduser('~')
target_filename = 'test_zipfile.zip'
output = os.path.join(target_dirname, target_filename)
if os.path.exists(output):
    os.remove(output)


def one_file_zipped():
    basename = 'class_static_method.py'
    fullname = os.path.join(dirname, basename)

    dst = zipfile.ZipFile(output, 'w')
    dst.write(fullname, basename)
    dst.close()


def more_files_zipped():
    files = ['class_static_method.py', 'matrix.py', 'get_obj_by_method.py']

    dst = zipfile.ZipFile(output, 'w')
    for basename in files:
        fullname = os.path.join(dirname, basename)
        #dst.write(fullname, basename)
        arcname = os.path.join('abc', basename)
        #dst.write(fullname, arcname)
        dst.write(fullname, arcname, zipfile.ZIP_DEFLATED)
    dst.close()


def multiple_levels_zipped():
    files = [
        ['class_static_method.py', 'matrix.py'],
        ['get_obj_by_method.py'],
    ]
    first = 'abc'
    second = [
        'hello',
        'world',
    ]

    dst = zipfile.ZipFile(output, 'w')
    for i, second_dir in enumerate(second):
        for basename in files[i]:
            fullname = os.path.join(dirname, basename)
            arcname = os.path.join(first, second_dir, basename)
            dst.write(fullname, arcname, zipfile.ZIP_DEFLATED)
    print dst.filelist
    dst.close()


def zero_file_zipped():
    dst = zipfile.ZipFile(output, 'w')
    print dst.filelist
    has_content = bool(dst.filelist)
    print has_content
    dst.close()
    if not has_content:
        os.remove(output)


if __name__ == '__main__':
    #one_file_zipped()
    #more_files_zipped()
    #multiple_levels_zipped()
    #zero_file_zipped()
    pass
