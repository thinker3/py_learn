import Image, inspect

im = Image.open("oxygen.png")
print im.format
print im.mode
print im.size
width, height = im.size

chars = []
for i in range(0, width, 7):
    rgba = im.getpixel((i, height//2))
    chars.append(chr(rgba[0]))

print ''.join(chars)
print ''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))
