from splinter.browser import Browser
b = Browser('firefox')
b.visit('http://www.baidu.com')
b.fill('wd', 'test')
b.execute_script('document.getElementsByName("f")[0].submit()')

