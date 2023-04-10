from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.get("https://biz.hira.or.kr/index.do?sso=ok")
time.sleep(5);

target = wait.until(EC.presence_of_element_located((By.ID, "MainFrame_VFrameSet0_HFrameSet0_VFrameSet1_MainFrame_form_divMain_div_board1ScrollableInnerContainerElement_inner")))
prev_text = target.text
print(prev_text)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(prev_text)
while True:
    time.sleep(60) # 60초 대기
    target = wait.until(EC.presence_of_element_located((By.ID, "MainFrame_VFrameSet0_HFrameSet0_VFrameSet1_MainFrame_form_divMain_div_board1ScrollableInnerContainerElement_inner")))
    curr_text = target.text

    # 이전 데이터와 현재 데이터가 다르면 결과 파일에 저장
    if curr_text != prev_text:
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(curr_text)
        prev_text = curr_text
browser.quit()