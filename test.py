import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to the chromedriver
driver_path = 'C:/Users/vanda/AppData/Local/Google/Chrome/Application'

# Initialize the Chrome driver
driver = webdriver.Chrome(https://vandana-m08.github.io/Food_ordering_web/)

# Open Google
driver.get('https://www.google.com')

# Find the search box
search_box = driver.find_element(By.NAME, 'q')

# Type the search query
search_box.send_keys('Selenium WebDriver')

# Press Enter
search_box.send_keys(Keys.RETURN)

# Print the title of the current page
print(driver.title)

# Close the browser
driver.quit()
