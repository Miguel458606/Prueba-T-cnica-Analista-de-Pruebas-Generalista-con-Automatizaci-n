
from locators.recruitment_locators import RecruitmentLocators
from pages.base_page import BasePage

class RecruitmentPage(BasePage):
    def navigate_to_recruitment(self):
        self.click(RecruitmentLocators.RECRUITMENT_TAB)

    def add_candidate(self, first_name, last_name, email):
        self.click(RecruitmentLocators.ADD_BUTTON)
        self.enter_text(RecruitmentLocators.FIRST_NAME, first_name)
        self.enter_text(RecruitmentLocators.LAST_NAME, last_name)
        self.enter_text(RecruitmentLocators.EMAIL, email)
        self.click(RecruitmentLocators.SAVE_BUTTON)

    def validate_candidate_status(self, candidate_name):
        candidates = self.driver.find_elements(*RecruitmentLocators.CANDIDATE_LIST)
        for candidate in candidates:
            if candidate_name in candidate.text and "Hired" in candidate.text:
                return True
        return False
