from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# pip install selenium
# pip install webdriver_manager

# 1. Chrome 옵션 설정 (Headless 모드)
chrome_options = Options()
chrome_options.add_argument("--headless")  # UI 없이 실행
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. WebDriver 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 3. ChatGPT 웹사이트 접속
# driver.get("https://chat.openai.com/")
driver.get("https://chatgpt.com/")
time.sleep(5)  # 웹페이지 로딩 대기

# 4. 로그인 페이지 확인 및 자동 로그인 (필요할 경우 추가)
# 로그인 버튼을 클릭하는 과정이 필요할 수 있음

# 5. 프롬프트 입력란 찾기
try:
    # time.sleep(5)  # 응답 대기
    print("start")

    # _name = driver.name

    textarea = driver.find_element(By.ID, "prompt-textarea")

    textarea.send_keys("안녕! 너는 누구야?")  # 메시지 입력
    textarea.send_keys(Keys.ENTER)  # 전송
    time.sleep(5)  # 응답 대기

    # 6. ChatGPT의 응답 가져오기
    responses = driver.find_elements(By.CLASS_NAME, "markdown")
    if responses:
        print("ChatGPT 응답:", responses[-1].text)  # 마지막 응답 출력
    else:
        print("응답을 찾을 수 없습니다.")

except Exception as e:
    print("오류 발생:", e)

# 7. WebDriver 종료
driver.quit()
