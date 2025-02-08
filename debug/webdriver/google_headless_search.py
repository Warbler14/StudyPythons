from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pip install selenium
# pip install webdriver_manager

# 1. Chrome 옵션 설정 (Headless 모드)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # UI 없이 실행
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 2. WebDriver 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")

# 검색창 요소 찾기
search_box = driver.find_element(By.ID, "APjFqb")

search_box.send_keys("what is WebDriver")

# 검색 버튼 클릭
search_box.submit()

# 검색 결과 출력
print(driver.title)

driver.quit()
