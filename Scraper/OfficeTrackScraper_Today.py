#<OfficeTrack Web Scraper>
#Copyright (C) <2020>  <Mauricio Urrego>
#Full licensing in included License.txt file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from credentials_paths import otusername, otpassword, otcompany, chromedriverpath, defaultdownloadpath, oturl
import time

chromedriver = chromedriverpath #r'C:\Users\Aliece\github\OfficeTrack-Scraper\Scraper\WebDriver\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_experimental_option("prefs", {
    "download.default_directory": defaultdownloadpath,
    "download.prompt_for_download": False,
})

driver = webdriver.Chrome(executable_path = chromedriver, options = options)

driver.get(oturl)

username = driver.find_element_by_xpath('//*[@id="txtUserName"]')
username.send_keys(otusername)

password = driver.find_element_by_xpath('//*[@id="txtPassword"]')
password.send_keys(otpassword)

companyname = driver.find_element_by_xpath('//*[@id="txtCompany"]')
companyname.send_keys(otcompany)

login = driver.find_element_by_id('LogonButton')
login.click()

#driver.implicitly_wait(15)
time.sleep(15)

driver.switch_to.frame('ToolbarFrame')

tasks = driver.find_element_by_xpath('//*[@id="tlbMain"]/div/div/div/ul/li[3]/a/span/span/span/img')
tasks.click()

#change the wait time after delete of below
#driver.implicitly_wait(20)
time.sleep(20)

driver.switch_to.default_content()
driver.switch_to.frame('MainContents')

#delete below after test
view = driver.find_element_by_xpath('//*[@id="tlbTasks"]/div/div/div/ul/li[9]/a/span/span/span/span[2]')
view.click()
#driver.implicitly_wait(20)
time.sleep(20)
tasklistview = driver.find_element_by_xpath('//*[@id="frmMain"]/div[1]/div/ul/li[2]/a/span')
tasklistview.click()
#delete above after test

#delete wait below after above delete
time.sleep(15)
#driver.implicitly_wait(15)

#delete below after test
view = driver.find_element_by_xpath('//*[@id="tlbTasks"]/div/div/div/ul/li[9]/a/span/span/span/span[2]')
view.click()
#driver.implicitly_wait(20)
time.sleep(20)
tasklistview = driver.find_element_by_xpath('//*[@id="frmMain"]/div[1]/div/ul/li[2]/a/span')
tasklistview.click()
#delete above after test

#below is for today date
todaydatestart = date.today().strftime('%m/%d/%Y')
todaydatetimestart = todaydatestart + ' 12:00 AM'

startdate = driver.find_element_by_xpath('//*[@id="TaskFilter_rdpFrom_dateInput"]')
startdate.clear()
startdate.send_keys(todaydatetimestart)

todaydateend = date.today().strftime('%m/%d/%Y')
todaydatetimeend = todaydateend + ' 11:59 PM'

enddate = driver.find_element_by_xpath('//*[@id="TaskFilter_rdpTo_dateInput"]')
enddate.clear()
enddate.send_keys(todaydatetimeend)
#

#below is for yesterday date
#yesterdaydatestart = date.today() - timedelta(days=1)
#datestr = yesterdaydatestart.strftime('%m/%d/%Y')
#yesterdaydatetimestart = datestr + ' 12:00 AM'

#startdate = driver.find_element_by_xpath('//*[@id="TaskFilter_rdpFrom_dateInput"]')
#startdate.clear()
#startdate.send_keys(yesterdaydatetimestart)

#yesterdaydateend = date.today() - timedelta(days=1)
#datestr = yesterdaydateend.strftime('%m/%d/%Y')
#yesterdaydatetimeend = datestr + ' 11:59 PM'

#enddate = driver.find_element_by_xpath('//*[@id="TaskFilter_rdpTo_dateInput"]')
#enddate.clear()
#enddate.send_keys(yesterdaydatetimeend)
#

#driver.switch_to.default_content()
#driver.switch_to.frame('ToolbarFrame')

refresh = driver.find_element_by_xpath('//*[@id="tlbTasks"]/div/div/div/ul/li[11]/a/span/span/span/span[1]/span')
refresh.click()

#driver.implicitly_wait(5)
time.sleep(5)

excel = driver.find_element_by_xpath('//*[@id="tlbTasks"]/div/div/div/ul/li[9]/a/span/span/span/span[1]/img')
excel.click()

#let it download
time.sleep(10)

print('Done')

driver.quit()
