from selenium import webdriver

driver=webdriver.Chrome(r"C:\Users\Kushal Raju\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.co.in")
#driver.find_element_by_id("twotabsearchtextbox").send_keys("Apple charger")

#driver.find_element_by_name("field-keywords").send_keys("iphone")

#driver.find_element_by_link_text("Mobiles").click()

# driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("iphone")

driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone")
driver.find_element_by_xpath("//header/div[@id='navbar']/div[@id='nav-belt']/div[2]/div[1]/form[1]/div[3]/div[1]").click()