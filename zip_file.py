#!/usr/bin/env python
# encoding: utf-8

import os
import zipfile


def one_file_zipped():
    dirname = os.path.dirname(os.path.abspath(__file__))
    basename = 'class_static_method.py'
    fullname = os.path.join(dirname, basename)
    output = os.path.join(dirname, 'test.zip')

    dst = zipfile.ZipFile(output, 'w')
    dst.write(fullname, basename)
    dst.close()


def more_files_zipped():
    dirname = os.path.dirname(os.path.abspath(__file__))
    files = ['class_static_method.py', 'matrix.py', 'get_obj_by_method.py']
    output = os.path.join(dirname, 'test.zip')

    dst = zipfile.ZipFile(output, 'w')
    for basename in files:
        fullname = os.path.join(dirname, basename)
        #dst.write(fullname, basename)
        arcname = os.path.join('abc', basename)
        #dst.write(fullname, arcname)
        dst.write(fullname, arcname, zipfile.ZIP_DEFLATED)
    dst.close()


if __name__ == '__main__':
    one_file_zipped()
    more_files_zipped()
