import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    #def test_abs1(self):
    def test_registration1(self):
        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector('.first_block input.form-control.first')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector('.first_block input.form-control.second')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector('.first_block input.form-control.third')
            input3.send_keys("123@qwe.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name('h1')
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            #assert "Congratulations! You have successfully registered!" == welcome_text
            self.assertEqual(Congratulations! You have successfully registered!, welcome_text, "Тест прошел успешно!")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
        
        
    # def test_abs2(self):
    def test_registration2(self):
        #self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        #try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector('.first_block input.form-control.first')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector('.first_block input.form-control.second')
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector('.first_block input.form-control.third')
            input3.send_keys("123@qwe.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name('h1')
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            #assert "Congratulations! You have successfully registered!" == welcome_text
            self.assertEqual(Congratulations! You have successfully registered!, welcome_text, "Тест прошел успешно!")

        #finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
        
if __name__ == "__main__":
    unittest.main()