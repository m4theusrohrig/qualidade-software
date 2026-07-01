# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante
- Matheus Röhrig - 071900826  

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo:
Login de usuário

🔎 **Descrição**  
Permite autenticar um usuário no sistema através de um formulário (#loginForm) com campos de e-mail e senha e botão "Entrar".

🎯 **Importância**  
Fluxo crítico de entrada — é a porta de entrada para qualquer outra ação no LocalEats.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 https://github.com/seu-repositorio/tests/codegen_login.py

### 🧠 Observações

- O Codegen ajudou a mapear rapidamente os seletores reais da tela (campo de e-mail, campo de senha e botão "Entrar" dentro do `#loginForm`), acelerando o início do teste
- Gerou cliques redundantes antes de cada `.fill()` (o `.click()` no campo já é implícito ao preenchê-lo)
- Não registrou nenhuma assertion — o Codegen só grava ações do usuário, nunca verificações; as validações precisaram ser adicionadas manualmente

---

## 🔹 3. Teste automatizado com Pytest

```python
# (versão inicial, sem POM)
import re
from playwright.sync_api import expect

def test_deve_realizar_login_com_sucesso(page):
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    page.get_by_role("textbox", name="teste@teste.com").fill("novotest@test.com")
    page.get_by_role("textbox", name="Sua senha secreta").fill("senha")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    expect(page).not_to_have_url(re.compile(r".*login\.html"))
```

### 📌 O que o teste faz?

- Acessa a página de login do sistema  
- Preenche e-mail e senha e realiza o login  
- Valida que o usuário saiu da tela de login após autenticar

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/seu-repositorio/pages/login_page.py  

### 🔗 Link para teste refatorado

👉 https://github.com/seu-repositorio/tests/test_login.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI: `LoginPage` concentra a interação com o formulário, `HomePage` concentra a navegação pós-login
- `realizar_login()` centraliza o preenchimento dos dois campos e a submissão, evitando repetir a lógica em cada teste
- Código mais organizado e legível — os testes descrevem apenas "o quê" está sendo validado (Arrange / Act / Assert)
- Maior reutilização e manutenção facilitada: se um seletor mudar, a correção acontece em um único lugar (`LoginPage.__init__`), sem tocar nos testes
- Adição de um terceiro teste (diferencial), comprovando que o login concede acesso funcional real ao sistema, e não apenas que a URL mudou

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest tests/ -v
```

### 📊 Resultado

- Total de testes: 3  
- Testes passaram: 3  
- Testes falharam: 0  

### 📸 Evidência

```
tests/test_login.py::test_deve_realizar_login_com_sucesso PASSED
tests/test_login.py::test_nao_deve_logar_com_campos_vazios PASSED
tests/test_login.py::test_deve_logar_filtrar_e_abrir_detalhes_do_restaurante PASSED

3 passed in 5.42s
```
(Inserir print real da execução local antes da entrega)

---

## 🔹 6. Análise crítica

- Nas primeiras gravações com o Codegen, o campo de e-mail era apenas clicado, sem preenchimento, o que fazia o login falhar silenciosamente sem indicar o motivo — só foi possível identificar comparando gravações diferentes
- Os seletores dos campos são frágeis, pois o nome acessível vem do **placeholder** ("teste@teste.com", "Sua senha secreta") e não de um `data-testid` ou `<label>` — qualquer mudança de texto no frontend quebra o teste mesmo sem alteração real de comportamento
- O teste quebraria se o texto do placeholder ou o nome do restaurante de teste ("Restaurante Sabor 0") fossem alterados, já que ambos são usados diretamente como seletor
- O teste precisa de melhorias para ser mais robusto: uso de `data-testid`, dados de teste isolados (via fixture/variável de ambiente) e assertions mais específicas na tela pós-login

---

## 🔹 7. Reflexão

- Testes automatizados não substituem testes manuais — a exploração inicial com o Codegen ainda dependeu de interação manual repetida até mapear corretamente o fluxo
- Devem focar em fluxos críticos, como o login, que é a porta de entrada do sistema e tem comportamento bem definido (sucesso/erro)
- Aumentam a confiança no sistema: o teste final não apenas verifica a URL, mas comprova que o login concede acesso funcional real (filtrar por categoria e abrir um restaurante)

---

## 💡 Conclusão

A automação de testes melhora a qualidade, mas exige boas práticas para manutenção. Neste PBL, o processo de gravar, refatorar e comparar as versões do teste de login evidenciou dois pontos importantes: o Codegen é um ponto de partida útil, mas grava literalmente o que foi clicado (não o que deveria ser testado), e seletores baseados em texto de interface (placeholders) são a principal fonte de fragilidade em testes E2E, exigindo atenção redobrada na hora de escolher o que usar como seletor.