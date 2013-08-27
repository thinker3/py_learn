#import gtk
#def _clipboard_changed(clipboard, event):
#    text = clipboard.wait_for_text()
#
#clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
#print clip.get_data()
#print dir(clip)
#clip.connect("owner-change", _clipboard_changed)
import os
var = os.popen('xsel').read()
print var
