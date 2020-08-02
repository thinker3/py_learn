#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task
import exifread


@task(default=True)
def exif(fp):
    with open(fp, 'rb') as f:
        tags = exifread.process_file(f)
        print(tags)


@task
def pil(fp):
    from PIL import Image
    with Image.open(fp) as img:
        exif_data = img._getexif()
        print(exif_data)
