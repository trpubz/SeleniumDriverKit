import unittest
import os
from DriverKit import DriverKit as DK
import selenium.webdriver


class TestDKConfigs(unittest.TestCase):
    def setUp(self) -> None:
        self.test_driver: selenium.webdriver.Chrome = DK.DKDriverConfig(headless=False)

    def tearDown(self) -> None:
        self.test_driver.quit()

    def test_open_nonheadless(self):
        self.test_driver.get("http://www.google.com")
        assert self.test_driver.title == "Google"

    def test_download_dir(self):
        root_dir = DK.DKDirBuilder()
        os.makedirs(root_dir, exist_ok=True)

        with open(os.path.join(root_dir, "temp.py"), "w"):
            os.remove(os.path.join(root_dir, "temp.py"))
        self.assertTrue(root_dir.endswith("DriverKit/temp/"))


if __name__ == '__main__':
    unittest.main()
