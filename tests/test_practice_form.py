from pages.practice_form_page import PracticeFormPage


def test_submit_practice_form(driver):

    form_page = PracticeFormPage(driver)

    # Abre página
    form_page.open()

    # Abre formulário
    form_page.open_practice_form()

    # Preenche
    form_page.fill_form(
        first_name="Luiz",
        last_name="Souza",
        email="luiz@email.com",
        phone="8599999999",
        address="Fortaleza Ceará"
    )

    # Envia
    form_page.submit_form()

    # Validação
    success_message = form_page.get_success_message()

    assert (
        "Thanks for submitting the form"
        in success_message
    )

    # Screenshot
    driver.save_screenshot(
        "screenshots/formulario_enviado.png"
    )