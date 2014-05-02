import sys
import pyhk
import win32clipboard
 
def fun():
    print "Do something"

def exit():
    sys.exit()

def get_selected_text():
    '''
    import win32gui
    hwnd = win32gui.GetForegroundWindow()
    text = win32gui.GetWindowText(hwnd)
    return text
    '''
    from get_sel import get_selected_text_from_front_window
    text = get_selected_text_from_front_window()
    print 'text: %s,' % text
    return text

def get_original_text():
    win32clipboard.OpenClipboard()
    try:
        original_text = win32clipboard.GetClipboardData()
    except TypeError as e:
        original_text = None
    finally:
        win32clipboard.CloseClipboard()
    print 'original_text: %s' % original_text
    return original_text

def print_selection():
    try:
        original_text = get_original_text()
        win32clipboard.OpenClipboard()
        if original_text is not None:
            win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(get_selected_text())
        selected_text = win32clipboard.GetClipboardData()
        print selected_text
        win32clipboard.EmptyClipboard()
        if original_text is not None:
            win32clipboard.SetClipboardText(original_text)
    except Exception as e:
        pass
    finally:
        win32clipboard.CloseClipboard()

 
hot = pyhk.pyhk()
 
# letters must be upper
#hot.addHotkey(['Ctrl', 'Alt', 'Z'], fun)
#hot.addHotkey(['Ctrl', 'Lwin', '7'], fun)  # c-Lwin or c-7 works
#hot.addHotkey(['Ctrl', 'Lwin'], fun)  # this is problematic
#hot.addHotkey(['Ctrl', 'Alt', '1'], fun)
hot.addHotkey(['Ctrl', 'Lwin', '1'], print_selection)
hot.addHotkey(['Ctrl', 'Alt', 'Q'], exit)
 
hot.start()
