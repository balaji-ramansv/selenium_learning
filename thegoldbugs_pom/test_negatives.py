import unittest
import random
import time
from unittest import TestCase
from settings import GOLDBUGS_URL, CHROMEDRIVER_PATH
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from thegoldbugs_pom.pages import TheGoldBugsPage
from thegoldbugs_pom.locators import TheGoldBugsPageLocators


class TheGoldBugsNegativeTest(TestCase):
    def setUp(self):
        service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(GOLDBUGS_URL)

    def test_negative_submit(self):
        thegoldbugs_page = TheGoldBugsPage(driver=self.driver)
        required = [
            (*TheGoldBugsPageLocators.first_name_text, "Balaji"),
            (*TheGoldBugsPageLocators.last_name_text, "Ramakrishnan"),
            (*TheGoldBugsPageLocators.email_text, "email@email.com"),
            (*TheGoldBugsPageLocators.subject_text, "some subject")
        ]
        del required[random.choice(range(len(required)))]
        print(required)
        for element_locator_value_tuple in required:
            thegoldbugs_page.enter_text(*element_locator_value_tuple)
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.message_text, "Hey come to the b'day party and play the band.")
        thegoldbugs_page.click(*TheGoldBugsPageLocators.response_required_checkbox)
        thegoldbugs_page.click(*TheGoldBugsPageLocators.no_response_required_checkbox)
        thegoldbugs_page.click(*TheGoldBugsPageLocators.public_show_radio)
        thegoldbugs_page.select_an_option_from_dropdown(*TheGoldBugsPageLocators.info_source_dropdown, "Google")
        thegoldbugs_page.click(*TheGoldBugsPageLocators.strongly_agree_radio)
        thegoldbugs_page.submit(*TheGoldBugsPageLocators.form)
        time.sleep(5)
        self.assertNotEqual(
            thegoldbugs_page.get_element(*TheGoldBugsPageLocators.thank_you_label).text,
            "Thanks to all the people in the world who use their knowledge and skills to help others."
            "Submit succeeded unexpectedly.")
        print("Submitted failed - this is expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
