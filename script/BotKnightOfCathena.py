#!/usr/bin/python3
from urllib.request import proxy_bypass
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

proxy_actual = []

def ProxyConnection():
    global proxy_actual
    temp = 0

    f = open("Proxies.txt", "r")
    list_of_lines = f.readlines()
    for line in enumerate(list_of_lines):
        if (line == proxy_actual):
            temp += 1
            continue
        elif (proxy_actual == []):
            proxy_actual = line
            f.close()
            return (line)
        elif(line != proxy_actual and temp > 0):
            proxy_actual = line
            f.close()
            return (line)
        else:
            continue

def Suivant(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(random.randint(2,2))

def Suivant1(driver):
    buttons = driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')
    for button in buttons:
        try:
            button.click()
        except:
            print("failed")
    sleep(random.randint(2,2))

def CreateKnightsAcc(driver):
    try:
        link_to = "https://knights-of-cathena.com/waitinglist/ref/623b950a70cd312d27a41628"
        ###---------NAVIGATE TO KNIGHT OF CATHENA---------###
        driver.get(link_to)
        ###---------MAXIMIZE WINDOW---------###
        driver.maximize_window()
        sleep(random.randint(2,2))
        ###---------FIND EMAIL FIELD AND PASTE EMAIL---------###
        email = driver.find_element_by_id("email")
        email.send_keys(Keys.CONTROL, 'v')
        s = pyperclip.paste() 
        with open('result.txt','a') as g:
            g.write(s + "\n\n")
            g.close()
        sleep(random.randint(2,2))
        ###---------FIND PASSWORD FIELD AND PUT PASSWORD---------###
        password = driver.find_element_by_id("password")
        password.send_keys("Gorille123456789@")
        password_confirm = driver.find_element_by_id("password-confirm")
        password_confirm.send_keys("Gorille123456789@")
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-s2to3c"]')[0].click()
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="koc-button css-z7f218"]')[0].click()
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="koc-button css-1jb9frs"]')[1].click()
        """ sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-1karmn2 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')[10].click()
        sleep(random.randint(2,2)) """
    except NoSuchElementException:
        print("Error")

def CreateTwitterAcc(driver):
    try:
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')[0].click()
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-901oao r-k200y r-1cvl2hr r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-1wzrnnt r-bcqeeo r-qvutc0"]')[0].click()
        name = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
        ###---------GENERATE RANDOM TWITTER NAME---------###
        name.send_keys(names.get_full_name())
        email = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[1]   
        ###---------PASTE GENERATE EMAIL---------###
        email.send_keys(Keys.CONTROL, 'v')
        ###---------GENERATE RANDOM DAY, MONTH, YEAR---------###
        RandomDay = random.randint(0,27)
        RandomMonth = random.randint(0,11)
        RandomYear = random.randint(30,50)
        #print(RandomDay, RandomMonth, RandomYear)
        month = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[0]
        sleep(random.randint(2,2))
        for _ in range(RandomMonth):
            month.send_keys(Keys.DOWN)
        sleep(random.randint(2,2))
        day = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[1]
        for _ in range(RandomMonth):
            day.send_keys(Keys.DOWN)
        sleep(random.randint(2,2))
        years = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-18jsvk2 r-1loqt21 r-37j5jr r-1inkyih r-rjixqe r-crgep1 r-1wzrnnt r-1ny4l3l r-t60dpp r-xd6kpl r-1pn2ns4 r-ttdzmv"]')[2]
        for _ in range(RandomYear):
            years.send_keys(Keys.DOWN)
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
        sleep(random.randint(2,2))
        Suivant(driver)
        Suivant(driver)
        ###---------GET THE CODE OF EMAIL VERIFICATION FOR TWITTER---------###
        driver.switch_to.window(driver.window_handles[0])
        sleep(15)
        CodeText = driver.find_elements_by_xpath('//*[@class="inboxSubject subject-title"]')[1].text
        CodeText = CodeText.split(' ')
        Text = CodeText[0]
        driver.switch_to.window(driver.window_handles[1])
        sleep(random.randint(2,2))
        CodeVerif = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
        CodeVerif.send_keys(Text)
        print(Text)
        sleep(random.randint(2,2))
        Suivant(driver)
        sleep(random.randint(2,2))
        PasswordField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        ###---------FIND PASSWORD FIELD AND WRITE PASSWORD---------###
        for element in PasswordField:
            try:
                element.send_keys("Gorille123456789@")
            except:
                print("not found")
        FinalizeAccount(driver)
    except(NoSuchElementException):
        exit(84)

def FinalizeAccount(driver):
    ###---------CLICK ON NEXT FOR FINALIZE TWITTER ACCOUNT---------###
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
        ###---------NAVIGATE TO EMAIL GENERATOR PAGE---------###
        driver.get(LinkToGenerateEmail)
        driver.set_page_load_timeout(30)
        sleep(10)
        ###---------COPY THE EMAIL THAT IS GENERATE---------###
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()
        driver.find_elements_by_xpath('//*[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')[0].click()
        sleep(random.randint(2,2))
    except NoSuchElementException:
        print("Error")

def SetConnection(driver, email_twitter, password_twitter):
    driver.find_elements_by_xpath('//*[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-1karmn2 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')[0].click()
    sleep(random.randint(2,2))
    TexField = driver.find_elements_by_xpath('//*[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')[0]
    TexField.send_keys(email_twitter)
    sleep(random.randint(2,2))
    driver.find_elements_by_xpath('//*[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')[6].click()
    sleep(random.randint(2,2))
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
        ###---------NAVIGATE TO KNIGHT OF CATHENA PAGE---------###
        link_to = "https://knights-of-cathena.com/waitinglist/"
        driver.get(link_to)
        sleep(random.randint(2,2))
        email = driver.find_element_by_id("email")
        ###---------PUT EMAIL TO CONNECT ACCOUNT---------###
        email.send_keys(email_twitter)
        sleep(random.randint(2,2))
        password = driver.find_element_by_id("password")
        ###---------PUT PASSWORD TO CONNECT ACCOUNT---------###
        password.send_keys(password_twitter)
        sleep(random.randint(2,2))
        driver.find_elements_by_xpath('//*[@class="koc-button css-n62otd"]')[0].click()
        sleep(random.randint(2,2))
        missions = driver.find_elements_by_xpath("//*[@class='koc-button css-1jb9frs']")
        exepection_discord = driver.find_elements_by_xpath("//*[@class='text-secondary css-1ijvcmh']")[3].text
        ###---------CHECK IF THE DISCORD MISSION IS HERE---------###
        if ("Discord" in exepection_discord):
            not_good = 0
        print (not_good)
        print (exepection_discord)
        for mission in missions:
            ###---------CLICK ON MISSIONS AFTER THE DISCORD FIELD---------###
            if temp != 0:
                mission.click()
                sleep(random.randint(2,2))
                ###---------SET CONNECTION TO TWITTER---------###
                SetConnection(driver, email_twitter, password_twitter)
                driver.switch_to.window(driver.window_handles[1])
                sleep(random.randint(2,2))
                if (temp1 == 0):
                    EmailInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[0]
                    ###---------ENTER TWITTER EMAIL---------###
                    EmailInput.send_keys(email_twitter)
                    PasswordInput = driver.find_elements_by_xpath("//*[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")[1]
                    ###---------ENTER TWITTER PASSWORD---------###
                    PasswordInput.send_keys(password_twitter)
                    sleep(random.randint(2,2))
                    driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")[0].click()
                    temp1 += 1
                sleep(random.randint(2,2))
                ###---------CLICK ON LIKE OR RETWEET TO DO THE MISSION---------###
                LikeClick = driver.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-1m3jxhj r-42olwf r-sdzlij r-1phboty r-rs99b7 r-16y2uox r-6gpygo r-peo1c r-1ps3wis r-1ny4l3l r-1udh08x r-1guathk r-1udbk01 r-o7ynqc r-6416eg r-lrvibr r-3s2u2q']")
                for element in LikeClick:
                    try:
                        sleep(random.randint(2,2))
                        element.click()
                    except:
                        print("fail")
                sleep(random.randint(2,2))
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                sleep(random.randint(2,2))
            if (not_good == 0):
                temp = 1
            else:
                temp == 2
            sleep(random.randint(2,2))
    except(NoSuchElementException):
        exit(84)

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

def GetProxyInfo(proxy):
    proxy = proxy[1].split(":")
    return (proxy[0], proxy[1])

def main():
    try:
        ###----------CHROME OPTIONS----------###
        s = "C:\\WebDriver\\bin\\chromedriver.exe"
        ###----------GENERATE RANDOM USER AGENT----------###
        #ua = UserAgent()
        #userAgent = ua.random
        #chrome_options = webdriver.ChromeOptions()
        ###----------ADD AS ARGUMENT A RANDOM USER AGENT----------###
        #chrome_options.add_argument(f"user-agent={userAgent}")

        ###---------GET PORT AND IP OF PROXIES---------###
        #proxy = ProxyConnection()
        #IpProxy, Port = GetProxyInfo(proxy)
        """
        ###---------GENERATE RANDOM USER AGENT---------###
        ua = UserAgent()
        userAgent = ua.random
        ###---------CONNECTION TO TOR---------###
        binary = FirefoxBinary(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\firefox.exe")
        profile = FirefoxProfile(r"C:\\Users\\bezie\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default")
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", int(IpProxy))
        profile.set_preference("network.proxy.http_port", int(Port))
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        profile.set_preference("general.useragent.override", f'user-agent={userAgent}')
        profile.update_preferences() """
        while (1):
            #userAgent = ua.random
            ###---------NAVIGATION WITH FIREFOX OR TOR---------###
            #driver = webdriver.Firefox(profile, binary)

            ###---------PROXY ROTATION---------###
            proxy = ProxyConnection()
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument(f"user-agent={userAgent}")
            chrome_options.add_argument(f'--proxy-server={proxy[1]}')
            ###---------GET PROXY PORT---------###
            ###---------TEST PROXY CONNECTION---------###
            """driver = webdriver.Chrome(options=chrome_options, executable_path=s)
            driver.get("http://httpbin.org/ip")
            body_text = driver.find_element_by_tag_name('body').text """
            #print("proxy : ", proxy[1])
            """
            ###---------INIT CONNECTION TO CHROME---------###
            driver = webdriver.Chrome(options=chrome_options, executable_path=s)
            driver.set_page_load_timeout(30)
            ###---------SET VIEWPORT SIZE---------###
            #set_viewport_size(driver, random.randint(800, 1000), random.randint(600, 900))

            ###---------GET RANDOM EMAIL FOR TWITTER---------###
            GetEmail(driver)
            ###---------NEW TAB ON GOOGLE CHROME---------###
            driver.execute_script("window.open('');") 
            driver.switch_to.window(driver.window_handles[1])
            ###---------CREATE KNIGHT OF CATHENA ACCOUNT---------###
            CreateKnightsAcc(driver)
            ###---------CREATE TWITTER ACCOUNT---------###
            CreateTwitterAcc(driver)
            ###---------NEW TAB ON GOOGLE CHROME---------###
            driver.execute_script("window.open('');") 
            driver.switch_to.window(driver.window_handles[2])
            ###---------DO THE MISSION OF KNIGHT OF CATHENA---------###
            GetMission(driver)
            driver.quit()
            sleep(random.randint(2,2)) """
    except(NoSuchElementException):
        exit(84)
main()