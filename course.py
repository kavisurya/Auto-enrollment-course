from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time
import re

driver = webdriver.Chrome("/home/baby/PycharmProjects/selenium/chromedriver")
driver.maximize_window()
driver.get("https://web.telegram.org/#/login")

def login():
    time.sleep(10)
    driver.find_element_by_xpath("//input[@name='phone_number']").send_keys("999999999")
    driver.find_element_by_xpath("//input[@name='phone_number']").send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='btn btn-md btn-md-primary']").click()
    otp =  input("Enter Your OTP : ")
    time.sleep(20)
    driver.find_element_by_xpath("//input[@name='phone_code']").send_keys(otp)
    driver.find_element_by_xpath("//input[@name='phone_code']").send_keys(Keys.RETURN)
    time.sleep(20)


#whois = "https://web.telegram.org/#/im?p=@indians_hackers2"
whois = "https://web.telegram.org/#/im?p=@Udemy_Blaster"
def group():
    # Initial deleting previous datas
    get_previous = open("output.txt","r+")
    get_previous.truncate(0)
    get_previous.close()

    # Getting group message's from Telegram
    contents = []
    write_file = open("output.txt","a")
    #driver.get("https://web.telegram.org/#/im?p=@Udemy_Blaster")
    driver.get(whois)

    time.sleep(20)
    cont_resp = driver.find_elements_by_xpath("//div[@class='im_message_text']")
    for i in cont_resp:
        # Storing the got group messages
        contents.append(i.text)
        write_file.write(i.text)

    write_file.close()
    print(contents)




def goto_login():
    driver.get("https://www.udemy.com")
    time.sleep(3)
    driver.find_element_by_xpath("//a[@data-purpose='header-login']").click()


def login_udemy():
    email = "email@gmail.com"
 
    password = input("Hii "+ email + " Enter your password continue to login : ")
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@id='id_password']").send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath("//input[@type = 'submit']").click()

def enroll_course(given_url):
    price = []
    time.sleep(5)
    driver.get(given_url)
    time.sleep(5)
    try:
        check_paid_given = driver.find_element_by_xpath("//div[@class='price-text--price-part--Tu6MH udlite-clp-discount-price udlite-heading-xxl']").text
    except NoSuchElementException:
        try:
            check_paid_given = driver.find_element_by_xpath("//div[@class='price-text--price-part--Tu6MH udlite-clp-discount-price udlite-heading-lg']").text
        except NoSuchElementException:
            check_paid_given = "Already Purchased"

    except KeyboardInterrupt:
        print("User Pressed Ctrl+C \nExiting...")
    finally:
        mystr = check_paid_given
        price.append(str(mystr).replace("Current price\n",""))
        check_paid_or_not = str(mystr).replace("Current price\n","")
        # print(str(mystr).replace("Current price\n",""))
        print(check_paid_or_not)

        if check_paid_or_not == "Free" or check_paid_or_not == "free":
            driver.find_element_by_xpath("//button[@data-purpose='buy-this-course-button']").click()
            time.sleep(8)

            try:
                driver.find_element_by_xpath("//select[@id='billingAddressSecondarySelect']/option[text()='Tamil Nadu']").click()
                time.sleep(3)
                test = driver.find_elements_by_xpath("//button[@type='submit']")
                test[2].click()
            except Exception as e:
                print(e)

            time.sleep(3)
        else:
            pass



def filter_url():
    okurl = []
    # Read a file
    file = open("output.txt", "r")
    read_file = file.read()
    # Filter the URL it returns a list
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', read_file)

    test = []
    # Create a array of array based on length ex:[[],[],[]]
    for k in urls:
        test.append(list())

    # Filtering unwanted text in url
    start = 0
    end = 8
    for x in range(0, len(urls)):
        '''Here using substring algorithm to removing a unwanted 
        text in URL's'''
        cyc = 0
        for i in urls[x]:
            '''finding the unwanted text'''
            if ":cyclone" in "".join(urls)[start:end]:
                cyc = 1

            else:
                test[x].append(i)
                if cyc == 1:
                    test[x].pop()
                else:
                    pass

            start = start + 1
            end = end + 1

    # joining array char to string
    for t in test:
        okurl.append("".join(t))

    if whois == "https://web.telegram.org/#/im?p=@indians_hackers2":
        okurl_string = "".join(okurl)
        okurl_replace = okurl_string.replace("https", "$$https")
        okurl = okurl_replace.split("$$")

        print(okurl)
        for len_ok_url in okurl:
            try:
                # if okurl[len_ok_url][0:21] == "https://www.udemy.com" or okurl[len_ok_url][0:17] == "https://udemy.com" or okurl[len_ok_url][0:9] == "udemy.com":
                if len_ok_url[0:21] == "https://www.udemy.com"or len_ok_url[0:17] == "https://udemy.com" or len_ok_url[0:9] == "udemy.com":
                    pass
                else:
                    okurl.remove(len_ok_url)
            except IndexError:
                print("index error !!")

        # return (okurl)

    goto_login()
    login_udemy()

    print(okurl)
    for inpURL in okurl:
        # print(inpURL)
        enroll_course(inpURL)

login()
group()
filter_url()
