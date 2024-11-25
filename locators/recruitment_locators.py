
from selenium.webdriver.common.by import By

class RecruitmentLocators:
    RECRUITMENT_TAB = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
    ADD_BUTTON = (By.XPATH, "//button[text()='+ Add']")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.NAME, "email")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANDIDATE_LIST = (By.XPATH, "//div[@class='oxd-table-card']")
