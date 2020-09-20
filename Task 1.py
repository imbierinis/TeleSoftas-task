from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.tiketa.lt/EN/search')

login = 'retryt@gmail.com'
password = 'ihqnxeq6'

# loging
try:
    login_link = browser.find_element_by_xpath("//a[contains(text(), 'Prisijunk')]")
except NoSuchElementException:
    login_link = browser.find_element_by_xpath("//a[contains(text(), 'Login')]")
login_link.click()

login_name = browser.find_element_by_id('txtLoginName')
login_name.send_keys(login)

login_password = browser.find_element_by_id('txtLoginPsw')
login_password.send_keys(password)

browser.find_element_by_id('btnLogin').click()
sleep(2)

# finding Caption element
a = browser.find_elements_by_name("sf_TextFilter")
for element in a:
    placeholder = element.get_attribute('placeholder')
    if placeholder == 'Search ...':
        element.send_keys('Forum')
        sleep(1)
        element.send_keys(Keys.TAB)
sleep(2)

# selecting Kaunas in City
city_list = browser.find_element_by_id('dropdownMenu3')
city_list.click()
browser.find_element_by_xpath("//a[contains(text(), 'Kaunas')]").click()
sleep(1)

# selecting date from
date_from = browser.find_element_by_name('sf_DateFrom')
date_from.send_keys('2020-09-15')
sleep(1)

# selecting date to
date_to = browser.find_element_by_name('sf_DateTo')
date_to.send_keys('2020-12-31')
date_to.send_keys(Keys.TAB)
sleep(1)

# pressing Search button
search_button = browser.find_element_by_xpath("//button[contains(text(), 'Search')]").click()
sleep(1)

# selecting Intelligent Forum
buy_button = browser.find_element_by_id('btnBuy-23125')
buy_button.click()

buy_button_inside = browser.find_element_by_xpath("//a[contains(text(), 'Buy')]")
buy_button_inside.click()
sleep(1)

# select 40 euros
# couldn't find correct way to click button under label

sleep(10)
browser.close()

