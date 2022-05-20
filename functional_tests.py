from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r"C:\Users\11237\AppData\Local\Mozilla Firefox\firefox.exe")

browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://localhost:8000')
assert 'Django' in browser.title