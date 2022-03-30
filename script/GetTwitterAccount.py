#!/usr/bin/python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import names

def Suivant(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")

def Suivant1(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(1)
def main():
    try:
        link_to = "https://twitter.com/i/flow/signup"
        LinkToGenerateEmail = "https://temp-mail.org/fr/"
        s = "C:\\WebDriver\\bin\\chromedriver.exe"
        driver = webdriver.Chrome(s)
        driver.set_page_load_timeout(10)
        driver.get(LinkToGenerateEmail)
        sleep(10)
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()

        sleep(2)
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link_to)
        driver.maximize_window()
        sleep(1)
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')[0].click()
        sleep(0.5)
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-901oao r-k200y r-1cvl2hr r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-1wzrnnt r-bcqeeo r-qvutc0"]')[0].click()
        name = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
        
        name.send_keys(names.get_full_name())
        email = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[1]   
        email.send_keys(Keys.CONTROL, 'v')
        RandomDay = random.randint(0,27)
        RandomMonth = random.randint(0,11)
        RandomYear = random.randint(30,50)
        print(RandomDay, RandomMonth, RandomYear)
        month = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[0]
        sleep(2)
        for _ in range(RandomMonth):
            month.send_keys(Keys.DOWN)
        sleep(0.5)
        day = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[1]
        for _ in range(RandomMonth):
            day.send_keys(Keys.DOWN)
        sleep(0.5)
        years = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[2]
        for _ in range(RandomYear):
            years.send_keys(Keys.DOWN)
        sleep(1)
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
        sleep(1)
        Suivant(driver)
        Suivant(driver)
        driver.switch_to.window(driver.window_handles[0])
        sleep(15)
        CodeText = driver.find_elements_by_xpath('//*[@class="inboxSubject subject-title"]')[1].text
        CodeText = CodeText.split(' ')
        Text = CodeText[0]
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)
        CodeVerif = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
        CodeVerif.send_keys(Text)
        print(Text)
        sleep(1)
        Suivant(driver)
        sleep(2)
        PasswordField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        
        for element in PasswordField:
            try:
                element.send_keys("Gorille123456789@")
            except:
                print("not found")
        
        Suivant1(driver)
        print("done")
        Suivant1(driver)
        print("done1")
        Suivant1(driver)
        print("done2")
        Suivant1(driver)
        print("done3")
        Suivant1(driver)
        print("done4")
        Suivant1(driver)
        print("done5")
        Suivant(driver)
        print("done6")
        Suivant1(driver)  
        print("done7")  
        Suivant1(driver)
        print("done8")
        Suivant(driver)
        print("done9")
        sleep(500)
    except(NoSuchElementException):
        exit(84)

main()