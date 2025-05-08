import unittest
import time
from unittest import TestCase
from settings import GOLDBUGS_URL, CHROMEDRIVER_PATH
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from thegoldbugs_pom.pages import TheGoldBugsPage
from thegoldbugs_pom.locators import TheGoldBugsPageLocators


class TheGoldBugsHappyPathTest(TestCase):
    def setUp(self):
        service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(GOLDBUGS_URL)

    def test_happy_path_submit(self):
        thegoldbugs_page = TheGoldBugsPage(driver=self.driver)
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.first_name_text, "Balaji")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.last_name_text, "Ramakrishnan")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.email_text, "balaji@gmail.com")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.subject_text, "Test b'day party")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.message_text, "Hey come to the b'day party and play the band.")
        thegoldbugs_page.click(*TheGoldBugsPageLocators.response_required_checkbox)
        thegoldbugs_page.click(*TheGoldBugsPageLocators.no_response_required_checkbox)
        thegoldbugs_page.click(*TheGoldBugsPageLocators.public_show_radio)
        thegoldbugs_page.select_an_option_from_dropdown(*TheGoldBugsPageLocators.info_source_dropdown, "Google")
        thegoldbugs_page.click(*TheGoldBugsPageLocators.strongly_agree_radio)
        thegoldbugs_page.submit(*TheGoldBugsPageLocators.form)
        time.sleep(5)
        self.assertIsNotNone(thegoldbugs_page.get_element(*TheGoldBugsPageLocators.thank_you_label), "Submit failed")
        print("Submitted successfully")

    def test_happy_path_only_required_submit(self):
        thegoldbugs_page = TheGoldBugsPage(driver=self.driver)
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.first_name_text, "Balaji")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.last_name_text, "Ramakrishnan")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.email_text, "balaji@gmail.com")
        thegoldbugs_page.enter_text(*TheGoldBugsPageLocators.subject_text, "Test b'day party")
        thegoldbugs_page.submit(*TheGoldBugsPageLocators.form)
        time.sleep(5)
        self.assertIsNotNone(thegoldbugs_page.get_element(*TheGoldBugsPageLocators.thank_you_label), "Submit failed")
        print("Submitted successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()