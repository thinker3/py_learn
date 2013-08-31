import wx
print wx.version()
from time import sleep


class GUI(object):
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Hello")
    def __init__(self):
        self.frame.Bind(wx.EVT_CLOSE, self._close)
        self.frame.Show(True)
        self.app.MainLoop()

    def _close(self, e):
        self.frame.Hide()
        sleep(2)
        #exit() # works
        self.frame.Destroy()

gui = GUI()
