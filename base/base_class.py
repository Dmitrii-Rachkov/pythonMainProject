import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)


    """Method assert word"""

    def assert_word(self, actual_word, expected_word):
        value_actual_word = actual_word.text
        assert value_actual_word == expected_word
        print("Good value word")


    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screnshot = "screenshot_" + now_date + ".png"
        self.driver.save_screenshot('D:\\Projects\\pythonMainProject\\screen\\' + name_screnshot)
        print("Screenshot is done: " + name_screnshot)


    """Method assert URL"""

    def assert_url(self, expected_url):
        get_url = self.driver.current_url
        assert get_url == expected_url
        print("Good value URL")




