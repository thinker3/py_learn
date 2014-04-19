import Image
from PngImagePlugin import PngImageFile
from JpegImagePlugin import JpegImageFile
clz = PngImageFile
clz = JpegImageFile


def get_ext(im):
    return im.format.lower()


def resize(im):
    assert isinstance(im, clz)
    output = 'thumbnail.%s' % get_ext(im)
    x = 400
    y = x
    # im = im.resize((x, y), Image.ANTIALIAS)
    im = im.resize((x, y))  # smaller
    assert isinstance(im, Image.Image)  # im.format == None
    im.save(output)


def thumbnail(im):
    assert isinstance(im, clz)
    x, y = im.size
    x = x / 5  # how about y? no effect?
    # im.thumbnail((x, y))
    im.thumbnail((x, y), Image.ANTIALIAS)  # smaller
    # im.save('thumbnail.png', 'JPEG')  # wrong
    # im.save('thumbnail.png', 'PNG')  # ok
    output = 'thumbnail.%s' % get_ext(im)
    im.save(output, im.format)


def main(filename):
    im = Image.open(filename)
    assert isinstance(im, clz)
    # resize(im)
    thumbnail(im)

filename = 'oxygen.png'
filename = 'rail.jpg'
main(filename)
