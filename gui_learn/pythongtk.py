import gtk
import egg.trayicon     # egg == python-gnome2-extras

def callback(widget, ev):
        print("Button %i pressed!" % ev.button)


tray = egg.trayicon.TrayIcon("TrayIcon")
box = gtk.EventBox()
label = gtk.Label("Click Me!")
box.add(label)
tray.add(box)
tray.show_all()

box.connect("button-press-event", callback)

gtk.main()
