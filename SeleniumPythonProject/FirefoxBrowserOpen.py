from selenium import webdriver

driver= webdriver.Firefox()

driver.get("https://www.google.co.in/")

print(driver.title)

print(driver.current_url)

driver.close()


