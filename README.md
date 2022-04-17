# Auto-enrollment-course

## About
Hi Folks,

Hope you are all doing well.

I just made a tool for enrolling the course. I daily getting 20 to 30 UDEMY courses with free course coupons. In this way ,
I can able to enroll the paid courses to free. So i am daily spent around 30 to 60 minutes. So i made a tool for this issues. 
This tool 1st fetches data's and course links and coupons codes from telegram. After that, It will enroll the courses in your udemy account using those links and copons.

## Before-run the tool

1) You have to replace your telegram mobile number in that 13 line code. 


        Ex: ...umber']").send_keys("999999999") to  umber']").send_keys("your_telegram_mobile_number")
 
2) And 58 line also you have to replace your udemy registered email.


          Ex: email = "email@gmail.com"
          
3) You should be installed chrome.

4) You should be download and install chromewebdriver. And change the chromewebdriver path at 7 th line code.

## Installation

Make sure you should be installed python updated version in your system.

```pip install selenium```

```pip3 install selenium```

More info : (Selenium Installation) [https://selenium-python.readthedocs.io/installation.html]

## Run

```Python3 course.py```


Thank you guys.
Cheers !!
