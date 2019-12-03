from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import conf


driver = webdriver.Chrome(chrome_dirver_path)

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

user = driver.find_element_by_name('session_key')

password = driver.find_element_by_name('session_password')

user.send_keys(conf.linkedin_username)

password.send_keys(conf.linkedin_password)

log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

log_in_button.click()

#google dorks after sigin 

driver.get('https://google.com')

search_query = driver.find_element_by_name('q')

#keyword = sys.argv[1]

search_query.send_keys('site:linkedin.com Ajith ')

search_query.send_keys(Keys.RETURN)

results = driver.find_elements_by_css_selector('div.g')
i=0
urls =[]
for x in results:
  link = results[i].find_element_by_tag_name("a")
  href = link.get_attribute("href")
  urls.append(href)
  i=i+1
  
  
sleep(2)

for url in urls:
  driver.get(url)
  sleep(2)
  driver.page_source
