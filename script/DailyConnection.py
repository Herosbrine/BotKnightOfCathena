#!/usr/bin/python3
from selenium import webdriver
from time import sleep

def DoConnection(email_twitter, password_twitter):
    s = "C:\\WebDriver\\bin\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=s)
    driver.set_page_load_timeout(10)
    link_to = "https://knights-of-cathena.com/waitinglist/"
    driver.get(link_to)
    sleep(1)
    email = driver.find_element_by_id("email")
    email.send_keys(email_twitter)
    sleep(1)
    password = driver.find_element_by_id("password")
    password.send_keys(password_twitter)
    sleep(1)
    driver.find_elements_by_xpath('//*[@class="koc-button css-n62otd"]')[0].click()
    sleep(1)
    VerifyMission(driver)
    driver.quit()

def VerifyMission(driver):
    BoutonMissions = driver.find_elements_by_xpath("//*[@class='koc-button css-1jb9frs']")
    AllMission = driver.find_elements_by_xpath("//*[@class='text-secondary css-1ijvcmh']")
    for i, mission in enumerate(AllMission):
        if mission.text == "Hello There Traveler":
            index = int((i-3) / 2)
            BoutonMissions[index].click()
            sleep(1)
        else:
            continue

def main():
    email_twitter = ""
    password_twitter = "Gorille123456789@"

    try:
        f = open("email_account.txt", "r")
        list_of_lines = f.readlines()
        f.close()
        for line in list_of_lines:
            email_twitter = line.replace("\n", '')
            if (email_twitter != ""):
                print(email_twitter)
                DoConnection(email_twitter, password_twitter)
                sleep(1)
            else:
                continue
    except:
        print("failed")
        exit(84)
main()