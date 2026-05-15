DemoQA Automation Framework

Projeto de automação de testes web utilizando Python + Selenium + Pytest, com padrão Page Object Model (POM).

O objetivo do projeto é simular testes reais de QA Automation em um site de prática (DemoQA), automatizando o preenchimento de formulário, validação de resultados e geração de evidências.

🚀 Tecnologias utilizadas
Python
Selenium WebDriver
Pytest
WebDriver Manager
Page Object Model (POM)
📁 Estrutura do projeto
demoqa_automation/
│
├── pages/
│   ├── base_page.py
│   └── practice_form_page.py
│
├── tests/
│   └── test_practice_form.py
│
├── screenshots/
│
├── conftest.py
├── requirements.txt
└── pytest.ini
⚙️ Funcionalidades

✔ Automação de navegação no site DemoQA
✔ Preenchimento automático de formulário
✔ Seleção de elementos (inputs, botões, radio buttons)
✔ Validação de mensagem de sucesso
✔ Captura de screenshot após execução
✔ Estrutura baseada em Page Object Model (POM)
✔ Execução via Pytest

▶️ Como executar o projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/demoqa-automation.git
cd demoqa-automation
2. Instalar dependências
pip install -r requirements.txt
3. Executar os testes
pytest -v
Evidências

Após a execução dos testes, uma screenshot será gerada automaticamente na pasta:

screenshots/

Exemplo:

screenshots/formulario_enviado.png
Conceitos aplicados
Automação de testes web
Selenium WebDriver
Estrutura POM (Page Object Model)
Boas práticas de QA Automation
Testes automatizados com Pytest
Esperas explícitas (WebDriverWait)
Validação com asserts
📌 Site utilizado para testes
https://demoqa.com
🎯 Objetivo do projeto

Este projeto foi desenvolvido para fins de estudo e portfólio, simulando um fluxo real de automação de testes utilizado em empresas de QA.

Autor

Projeto desenvolvido por [Luiz Felipe]

GitHub: https://github.com/luizdiga13-cpu

 Próximas melhorias
Implementação de testes de login
Integração com Allure Report
Execução em CI/CD (GitHub Actions)
Massa de dados com CSV/JSON
Testes de API com Requests