import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_youtube_title(browser):
    browser.get("https://www.youtube.com")
    title = browser.title
    assert "YouTube" in title, f"Expected 'YouTube' in title, but got '{title}'"

def test_youtube_video_title(browser):
    browser.get("https://www.youtube.com") 
    # time.sleep(2)
    video_title_element = browser.find_element(By.ID, "video-title")
    video_title_element.click()
    page_title = browser.title
    video_title_text = video_title_element.text
    assert page_title == video_title_text, f"Expected page title '{video_title_text}', but got '{page_title}'"

def send_message(browser):
    """
    К сожалению, для того, чтобы протестировать в ютубе большую часть опций, нужно залогиниться в гугл аккаунте.
    Это не представляется возможным из-за того, что на номер телефона приходит код.
    Именно поэтому я написал ещё один тест для отправки сообщения в веб-приложении.
    """
    browser.get("https://erofeev.com/application")
    chats_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "chats")))
    chats_button.click()
    chats_list = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.chat-list"))
    )
    first_chat = chats_list.find_element(By.CSS_SELECTOR, "li.chat-item:first-child")
    first_chat.click()
    message_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
    )
    message = "Максим, привет!"
    message_input.send_keys(message)
    send_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "send-message"))
    )
    send_button.click()
    message_list = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.message-list"))
    )
    messages = message_list.find_elements(By.CSS_SELECTOR, "li")
    last_message = messages[-1].text
    assert message == last_message
