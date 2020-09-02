import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_for_add_to_basket(browser):
    # browser.implicitly_wait(10)
    try:
        browser.get(link)
        time.sleep(30)
        # находим кнопку
        browser.find_elements_by_css_selector(".btn-add-to-basket")
        return True
    except:
        return False

button = test_guest_should_see_button_for_add_to_basket
# с помощью assert проверяем, что кнопка есть
assert button, "Кнопка не найдена"

# Проверяется количество elements, и тест НЕ падает при проверке. А результат наличия/отсутствия элемента теперь контролируется ASSERT
#button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
#assert button > 0, "нет элемента"

