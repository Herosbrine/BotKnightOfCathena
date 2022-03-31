from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
binary = FirefoxBinary(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\firefox.exe")
profile = FirefoxProfile(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default")

driver = webdriver.Firefox(profile, binary)
driver.get("http://stackoverflow.com")
sleep(100)
driver.quit()

""" profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
driver = webdriver.Firefox(profile) """