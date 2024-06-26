from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/') # open URL

# enter 'shirts' in search field
driver.find_element(By.ID, 'search').send_keys('shirts')

#click search btn
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(10)

# verification
actual_text = driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
print(actual_text)
assert 'shirts' in actual_text, f'Error! Text shirts is {actual_text}'
print('Test case passed')
driver.quit()
