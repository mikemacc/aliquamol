from selenium import webdriver

driver = webdriver.Chrome()
close = driver.find_element(By.ID, "close_button")
