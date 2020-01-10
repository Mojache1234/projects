from selenium import webdriver
import os


class ScreenCapture:
    STARTING_URL = 'http://www.yahoo.com'
    PRODUCTION_URL = 'http://www.yahoo.com'
    driver = None

    def __init__(self):
        self.set_up()
        self.capture_screens()
        self.clean_up()

    def set_up(self):
        self.driver = webdriver.Chrome()

    def clean_up(self):
        self.driver.close()

    def capture_screens(self):
        self.screenshot(self.STARTING_URL, 'screen_staging.png')
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')

    def screenshot(self, url, file_name):
        print('Capturing', url, 'screenshot as', file_name, '...')
        self.driver.get(url)
        self.driver.set_window_size(1400, 768)
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name)
        self.driver.save_screenshot(path)
        print('Saving', path, '...')
        self.driver.get_screenshot_as_png()
        print('Done.')


ScreenCapture()
