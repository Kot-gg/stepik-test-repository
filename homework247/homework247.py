import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"D:\Work\Build Automation\Drivers\chromedriver.exe")
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(browser, 12)
price = "$100"
text_condition = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), price))
button = browser.find_element_by_id("book").click()
x = float(browser.find_element_by_id("input_value").text)
# answer = math.log(abs(12*math.sin(x)))
answer = math.log(abs(12*math.sin(x)))
browser.find_element_by_id("answer").send_keys(str(answer))
browser.find_element_by_id("solve").click()
