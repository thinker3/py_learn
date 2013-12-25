from splinter.browser import Browser
b = Browser('firefox')
b.visit('http://www.baidu.com')
#b.fill('wd', 'test\r')
#b.fill('wd', 'test\n')
#b.fill('wd', 'test\r\n')

b.fill('wd', 'test')
#b.execute_script('document.getElementsByName("f")[0].submit()')

script = '''
    var e = document.createEvent('KeyboardEvent');
    e.initKeyEvent('keydown', true, true, window, false, false, false, false, 13, 0);
    document.getElementsByName('wd')[0].dispatchEvent(e)
'''
b.execute_script(script)

