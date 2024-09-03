import os
from _pydatetime import datetime
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


class ScreenshotListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, screenshot_dir="screenshots"):
        self.current_test_tags = None
        self.screenshot_dir = screenshot_dir
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def end_keyword(self, name, attrs):
        logger.info(f"Ending keyword: {name}")
        logger.info(f"Keyword tags: {attrs['tags']}")
        if 'screenshot' in attrs['tags']:
            common_instance = BuiltIn().get_library_instance('CommonKeywords')
            if common_instance.driver:
                screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
                common_instance.driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot taken: {screenshot_path}")
