from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.maximize_window()

host = "https://www.shoppersstop.com/louis-philippe-mens-printed-formal-shirt/p-206764048/colorChange/206764048_9654"
driver.get(host)
time.sleep(4)
driver.find_element_by_xpath("//button[@class = 'variant-size-button-206764092']").click()
time.sleep(2)

input_tag = driver.find_element_by_xpath("//input[@id = 'addToCartButton']")

print(input_tag.get_attribute('value'))
input_tag.click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class = 'minicart bags bag bag-container']").click()
time.sleep(4)


driver.get("https://www.shoppersstop.com/cart")
print(type(driver.page_source))

file1 = open("cart_page.txt","w")
file1.writelines(driver.page_source) 
file1.close() 


driver.quit()
