#coding=utf8
from splinter import Browser
import sys

content = str(sys.argv[1], 'utf-8')
url = 'http://weibo.com'

browser = Browser('firefox', extensions=['firebug.xpi',])
browser.visit(url)
browser.fill('username','thinker3@qq.com')
browser.find_by_name('password').click()
browser.fill('password','tui123')
browser.find_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div[6]/a').click()
#browser.find_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/textarea').click()
browser.fill('', content)
browser.find_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/div/div/div/div[3]/div/a').click()

