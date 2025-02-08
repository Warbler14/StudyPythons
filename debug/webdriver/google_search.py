from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# 검색창 요소 찾기
search_box = driver.find_element(By.ID, "APjFqb")

search_box.send_keys("WebDriver 사용법")

# 검색 버튼 클릭
search_box.submit()

# 검색 결과 출력
print(driver.title)

driver.quit()
