#!/usr/bin/python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def Suivant(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(1)

def Suivant1(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(1)

def SetConnection(driver, email_twitter, password_twitter):
    driver.find_elements_by_xpath('//*[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-1karmn2 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
    sleep(2)
    TexField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
    TexField.send_keys(email_twitter)
    sleep(2)
    driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')[6].click()
    sleep(2)
    PasswordField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[1]
    PasswordField.send_keys(password_twitter)
    Suivant(driver)
    driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()

def main():
    not_good = 1
    temp = 0
    temp1 = 0
    email_twitter = "maliye3585@f1xm.com"
    password_twitter = "Gorille123456789@"
    try:
        link_to = "https://knights-of-cathena.com/waitinglist/"
        s = "C:\\WebDriver\\bin\\chromedriver.exe"
        driver = webdriver.Chrome(s)
        driver.set_page_load_timeout(10)
        driver.get(link_to)
        driver.maximize_window()
        sleep(1)
        email = driver.find_element_by_id("email")
        email.send_keys(email_twitter)
        sleep(1)
        password = driver.find_element_by_id("password")
        password.send_keys(password_twitter)
        sleep(1)
        driver.find_elements_by_xpath('//*[@class="koc-button css-n62otd"]')[0].click()
        sleep(1)
        missions = driver.find_elements_by_xpath("//*[@class='koc-button css-1jb9frs']")
        exepection_discord = driver.find_elements_by_xpath("//*[@class='text-secondary css-1ijvcmh']")[3].text
        if ("Discord" in exepection_discord):
            not_good = 0
        print (not_good)
        print (exepection_discord)
        for mission in missions:
            if temp != 0:
                mission.click()
                sleep(2)
                SetConnection(driver, email_twitter, password_twitter)
                driver.switch_to.window(driver.window_handles[1])
                sleep(5)
                if (temp1 == 0):
                    EmailInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[0]
                    EmailInput.send_keys(email_twitter)
                    PasswordInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[1]
                    PasswordInput.send_keys(password_twitter)
                    sleep(2)
                    driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")[0].click()
                    temp1 += 1
                sleep(5)
                LikeClick = driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-1m3jxhj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-16y2uox r-6gpygo r-peo1c r-1ps3wis r-1ny4l3l r-1udh08x r-1guathk r-1udbk01 r-o7ynqc r-6416eg r-lrvibr r-3s2u2q']")
                for element in LikeClick:
                    try:
                        sleep(3)
                        element.click()
                    except:
                        print("fail")
                sleep(3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                sleep(1)
            if (not_good == 0):
                temp = 1
            else:
                temp == 2
            sleep(1)
        sleep(500)
    except(NoSuchElementException):
        exit(84)
main()