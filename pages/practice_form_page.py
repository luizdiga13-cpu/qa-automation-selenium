from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PracticeFormPage(BasePage):

    URL = "https://demoqa.com/forms"

    # Locators
    PRACTICE_FORM_MENU = (By.XPATH, "//span[text()='Practice Form']")

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")

    MALE_GENDER = (By.XPATH, "//label[text()='Male']")

    PHONE = (By.ID, "userNumber")

    ADDRESS = (By.ID, "currentAddress")

    SUBMIT_BUTTON = (By.ID, "submit")

    SUCCESS_MODAL = (
        By.ID,
        "example-modal-sizes-title-lg"
    )

    def open(self):
        self.driver.get(self.URL)

    def open_practice_form(self):
        self.click(*self.PRACTICE_FORM_MENU)

    def fill_form(
        self,
        first_name,
        last_name,
        email,
        phone,
        address
    ):

        self.write(*self.FIRST_NAME, first_name)

        self.write(*self.LAST_NAME, last_name)

        self.write(*self.EMAIL, email)

        self.click(*self.MALE_GENDER)

        self.write(*self.PHONE, phone)

        self.write(*self.ADDRESS, address)

    def submit_form(self):

        self.scroll_to_element(*self.SUBMIT_BUTTON)

        self.click(*self.SUBMIT_BUTTON)

    def get_success_message(self):

        return self.get_text(*self.SUCCESS_MODAL)