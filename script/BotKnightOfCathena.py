#!/usr/bin/python3
from weakref import proxy
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import names
import pyperclip
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

def ProxyConnection():
    f = open("Proxies.txt", "r")
    list_of_lines = f.readlines()
    if not any("x " in s for s in list_of_lines):
        list_of_lines[0] = "x " + list_of_lines[0]
    for index, line in enumerate(list_of_lines):
        if "x " in line:
            next_index = index + 1
            if index == len(list_of_lines) -1:
                next_index = 0

            list_of_lines[index] = list_of_lines[index].split("x ").pop()
            proxy = list_of_lines[index]
            list_of_lines[next_index] = "x " + list_of_lines[next_index]
            return (proxy)

def Suivant(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(random.randint(1,1))

def Suivant1(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(random.randint(1,1))

def CreateKnightsAcc(driver):
    try:
        link_to = "https://knights-of-cathena.com/waitinglist/ref/623b950a70cd312d27a41628"
        driver.get(link_to)
        driver.maximize_window()
        sleep(random.randint(1,1))
        email = driver.find_element_by_id("email")
        email.send_keys(Keys.CONTROL, 'v')
        s = pyperclip.paste() 
        with open('result.txt','a') as g:
            g.write(s + "\n\n")
            g.close()
        sleep(random.randint(1,1))
        password = driver.find_element_by_id("password")
        password.send_keys("Gorille123456789@")
        password_confirm = driver.find_element_by_id("password-confirm")
        password_confirm.send_keys("Gorille123456789@")
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="css-s2to3c"]')[0].click()
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="koc-button css-z7f218"]')[0].click()
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="koc-button css-1jb9frs"]')[1].click()
        """ sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-1karmn2 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')[10].click()
        sleep(random.randint(1,1)) """
    except NoSuchElementException:
        print("Error")

def CreateTwitterAcc(driver):
    try:
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')[0].click()
        sleep(random.randint(1,1))
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
        sleep(random.randint(1,1))
        for _ in range(RandomMonth):
            month.send_keys(Keys.DOWN)
        sleep(random.randint(1,1))
        day = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[1]
        for _ in range(RandomMonth):
            day.send_keys(Keys.DOWN)
        sleep(random.randint(1,1))
        years = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[2]
        for _ in range(RandomYear):
            years.send_keys(Keys.DOWN)
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
        sleep(random.randint(1,1))
        Suivant(driver)
        Suivant(driver)
        driver.switch_to.window(driver.window_handles[0])
        sleep(15)
        CodeText = driver.find_elements_by_xpath('//*[@class="inboxSubject subject-title"]')[1].text
        CodeText = CodeText.split(' ')
        Text = CodeText[0]
        driver.switch_to.window(driver.window_handles[1])
        sleep(random.randint(1,1))
        CodeVerif = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
        CodeVerif.send_keys(Text)
        print(Text)
        sleep(random.randint(1,1))
        Suivant(driver)
        sleep(random.randint(1,1))
        PasswordField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        
        for element in PasswordField:
            try:
                element.send_keys("Gorille123456789@")
            except:
                print("not found")
        FinalizeAccount(driver)
    except(NoSuchElementException):
        exit(84)

def FinalizeAccount(driver):
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
    """ 
    Suivant(driver)
    print("done6")
    Suivant1(driver)  
    print("done7")  
    Suivant1(driver)
    print("done8")
    Suivant(driver)
    print("done9") 
    """

def GetEmail(driver):
    LinkToGenerateEmail = "https://temp-mail.org/fr/"
    try:
        driver.get(LinkToGenerateEmail)
        driver.set_page_load_timeout(30)
        sleep(10)
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()
        sleep(random.randint(1,1))
    except NoSuchElementException:
        print("Error")

def SetConnection(driver, email_twitter, password_twitter):
    driver.find_elements_by_xpath('//*[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-1karmn2 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
    sleep(random.randint(1,1))
    TexField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
    TexField.send_keys(email_twitter)
    sleep(random.randint(1,1))
    driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')[6].click()
    sleep(random.randint(1,1))
    PasswordField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[1]
    PasswordField.send_keys(password_twitter)
    Suivant(driver)
    driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()

def GetMission(driver):
    not_good = 1
    temp = 0
    temp1 = 0
    email_twitter = pyperclip.paste() 
    password_twitter = "Gorille123456789@"
    try:
        link_to = "https://knights-of-cathena.com/waitinglist/"
        driver.get(link_to)
        sleep(random.randint(1,1))
        email = driver.find_element_by_id("email")
        email.send_keys(email_twitter)
        sleep(random.randint(1,1))
        password = driver.find_element_by_id("password")
        password.send_keys(password_twitter)
        sleep(random.randint(1,1))
        driver.find_elements_by_xpath('//*[@class="koc-button css-n62otd"]')[0].click()
        sleep(random.randint(1,1))
        missions = driver.find_elements_by_xpath("//*[@class='koc-button css-1jb9frs']")
        exepection_discord = driver.find_elements_by_xpath("//*[@class='text-secondary css-1ijvcmh']")[3].text
        if ("Discord" in exepection_discord):
            not_good = 0
        print (not_good)
        print (exepection_discord)
        for mission in missions:
            if temp != 0:
                mission.click()
                sleep(random.randint(1,1))
                SetConnection(driver, email_twitter, password_twitter)
                driver.switch_to.window(driver.window_handles[1])
                sleep(random.randint(1,1))
                if (temp1 == 0):
                    EmailInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[0]
                    EmailInput.send_keys(email_twitter)
                    PasswordInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[1]
                    PasswordInput.send_keys(password_twitter)
                    sleep(random.randint(1,1))
                    driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")[0].click()
                    temp1 += 1
                sleep(random.randint(1,1))
                LikeClick = driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-1m3jxhj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-16y2uox r-6gpygo r-peo1c r-1ps3wis r-1ny4l3l r-1udh08x r-1guathk r-1udbk01 r-o7ynqc r-6416eg r-lrvibr r-3s2u2q']")
                for element in LikeClick:
                    try:
                        sleep(random.randint(1,1))
                        element.click()
                    except:
                        print("fail")
                sleep(random.randint(1,1))
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                sleep(random.randint(1,1))
            if (not_good == 0):
                temp = 1
            else:
                temp == 2
            sleep(random.randint(1,1))
    except(NoSuchElementException):
        exit(84)

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

def main():
    try:
        ###----------CHROME OPTIONS----------###
        s = "C:\\WebDriver\\bin\\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument
        ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        +"AppleWebKit/537.36 (KHTML, like Gecko)"
        +"Chrome/87.0.4280.141 Safari/537.36")
        ###---------TOR BROWSER NAVIGATION---------###
        """ PROXY_HOST = "12.12.12.123"
        PROXY_PORT = "1234"
        ua = UserAgent()
        userAgent = ua.random
        binary = FirefoxBinary(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\firefox.exe")
        profile = FirefoxProfile(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default")
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", PROXY_HOST)
        profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        profile.set_preference("general.useragent.override", f'user-agent={userAgent}')
        profile.update_preferences() """
        while (1):
            #driver = webdriver.Firefox(profile, binary)
            #set_viewport_size(driver, random.randint(800, 1000), random.randint(600, 900))
            driver = webdriver.Chrome(options=chrome_options, executable_path=s)

            ###---------PROXY ROTATION---------###
            """ proxy = ProxyConnection()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(options=chrome_options, executable_path=s)
            driver.get("http://httpbin.org/ip")
            body_text = driver.find_element_by_tag_name('body').text """
            driver.set_page_load_timeout(30)
            GetEmail(driver)
            driver.execute_script("window.open('');") 
            driver.switch_to.window(driver.window_handles[1])
            CreateKnightsAcc(driver)
            #CreateTwitterAcc(driver)
            #driver.execute_script("window.open('');") 
            #driver.switch_to.window(driver.window_handles[2])
            #GetMission(driver)
            driver.quit()
            sleep(random.randint(1,1))
    except(NoSuchElementException):
        exit(84)
main()