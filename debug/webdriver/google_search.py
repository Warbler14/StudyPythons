from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# 검색창 요소 찾기
search_box = driver.find_element(By.ID, "APjFqb")

search_box.send_keys("WebDriver 사용법")

# 검색 버튼 클릭
search_box.submit()

# Google의 시스템이 컴퓨터 네트워크에서 비정상적인 트래픽을 감지했습니다. 이 페이지는 로봇이 아니라 실제 사용자가 요청을 보내고 있는지를 확인하는 페이지입니다. 왜 이런 현상이 발생하는 거죠?
#
#
# IP주소: 000.000.000.000
# 시간: 2025-02-08T16:42:46Z
#URL: https://www.google.com/search?q=WebDriver+%EC%82%AC%EC%9A%A9%EB%B2%95&sca_esv=aac09e88d3bc5d88&source=hp&ei=aImnZ5C1Bd7a2roPtMT0MA&iflsig=ACkRmUkAAAAAZ6eXeDpXRNPAn3_KKUoaXZR1ENDJjWnD&sei=hYmnZ7e5K-68vr0Ps66eiAU
#WebDriver+사용법&sca_esv=aac09e88d3bc5d88&source=hp&ei=aImnZ5C1Bd7a2roPtMT0MA&iflsig=ACkRmUkAAAAAZ6eXeDpXRNPAn3_KKUoaXZR1ENDJjWnD&sei=hYmnZ7e5K-68vr0Ps66eiAU

# 검색 결과 출력
print(driver.title)

driver.quit()
