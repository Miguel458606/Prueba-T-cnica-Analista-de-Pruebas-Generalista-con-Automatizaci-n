
from behave import given, when, then
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from utils.driver_setup import setup_driver

@given("el usuario accede al sistema con credenciales válidas")
def step_login(context):
    context.driver = setup_driver()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(context.driver)
    login_page.login("Admin", "admin123")

@when("el usuario navega a la funcionalidad 'Recruitment'")
def step_navigate_to_recruitment(context):
    recruitment_page = RecruitmentPage(context.driver)
    recruitment_page.navigate_to_recruitment()

@when("agrega un candidato con información válida")
def step_add_candidate(context):
    recruitment_page = RecruitmentPage(context.driver)
    context.candidate_name = "John Doe"
    recruitment_page.add_candidate("John", "Doe", "johndoe@example.com")

@then("el candidato aparece en la lista con estado 'Hired'")
def step_validate_candidate(context):
    recruitment_page = RecruitmentPage(context.driver)
    assert recruitment_page.validate_candidate_status(context.candidate_name), "El candidato no fue contratado"
