from splinter import Browser
from splinter.driver.webdriver.firefox import WebDriver
br = Browser()
assert isinstance(br, WebDriver)
br.quit()
br.
