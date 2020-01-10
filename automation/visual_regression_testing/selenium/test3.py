from PIL import Image, ImageDraw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from time import sleep
import os
import sys

class ScreenAnalysis:

    STAGING_URL = ''  # make dynamic
    PRODUCTION_URL = ''
    driver = None

    def __init__(self, url1, url2):
        self.set_up()
        self.STAGING_URL = url1
        self.PRODUCTION_URL = url2
        self.capture_screens()
        self.analyze()
        self.clean_up()

    def set_up(self):
        ''' Set browser options '''
        ua = UserAgent()['Chrome']
        options = Options()
        options.add_argument('--headless')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument(f'user-agent={ua}')
        self.driver = webdriver.Chrome(chrome_options=options)

    def clean_up(self):
        ''' Close browser after you\'re done '''
        self.driver.close()

    def capture_screens(self):
        ''' Called to capture both staging and production '''
        self.screenshot(self.STAGING_URL, 'screen_staging.png')  # TODO: Make user input
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')  # TODO: Make user input

    def screenshot(self, url, file_name):
        ''' Takes full-page screenshot of given URL '''
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get(url)

        # Offset required to correctly resize browser
        # w_offset, h_offset, total_height = self.driver.execute_script("""
        #     return [window.outerWidth - window.innerWidth, window.outerHeight - window.innerHeight, document.body.parentNode.scrollHeight]
        # """)
        w_offset, h_offset, total_height = self.driver.execute_script("""
            return [window.outerWidth - window.innerWidth, window.outerHeight - window.innerHeight,
            Math.max(
                document.body.parentNode.scrollHeight,
                document.body.parentNode.offsetHeight,
                document.documentElement.clientHeight,
                document.documentElement.scrollHeight,
                document.documentElement.offsetHeight
            )]
        """)
        self.driver.set_window_size(1400 + w_offset, total_height + h_offset)

        # sleep(10)
        while (self.driver.execute_script('return jQuery(":animated").length !== 0')):
            sleep(1)


        self.driver.save_screenshot(os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'screenshots', file_name))
        self.driver.get_screenshot_as_png()

        print("Done.")

    def analyze(self):
        screenshot_staging = Image.open("screenshots/screen_staging.png")
        screenshot_production = Image.open("screenshots/screen_production.png")
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_staging.size

        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:  # This checks pixels, but I can also do average brightness
                    draw = ImageDraw.Draw(screenshot_staging)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")

        screenshot_staging.save("result.png")

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 500  # this can be controlled

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor

ScreenAnalysis('https://www.sandhillglobaladvisors.com/', 'https://www.sandhillglobaladvisors.com/')
# ScreenAnalysis('http://dev-fish-on.pantheonsite.io/', 'http://test1-fish-on.pantheonsite.io/')
