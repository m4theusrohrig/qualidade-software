# Aula 12 – BDD e Automação Orientada a Comportamento
# LocalEats – Atividade PBL

## 👥 Integrantes

- Matheus Röhrig - 071900826

---

# 🔹 1. Fluxo escolhido

## Integrante: Matheus Röhrig

### Fluxo
Navegação entre páginas

### Objetivo
Validar se a navegação entre as principais páginas do LocalEats (Explorar, Meus Favoritos e Meus Pedidos) funciona corretamente, garantindo que cada página carregue sem erros e exiba seus elementos principais.

---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/navegacao_paginas.feature
```

## Conteúdo

```gherkin
Feature: Navegação entre páginas

  Scenario: Navegar para a página de Meus Favoritos
    Given que o usuário está autenticado na página inicial do LocalEats
    When ele clica no link "Meus Favoritos"
    Then a página de "Meus Favoritos" deve carregar corretamente

  Scenario: Navegar para a página de Meus Pedidos
    Given que o usuário está autenticado na página inicial do LocalEats
    When ele clica no link "Meus Pedidos"
    Then a página de "Meus Pedidos" deve carregar corretamente

  Scenario: Retornar para a página de Explorar
    Given que o usuário está autenticado na página inicial do LocalEats
    And ele navegou até a página de "Meus Favoritos"
    When ele clica no link "Explorar"
    Then a página de "Explorar" deve carregar corretamente
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
projeto/
│
├── features/
│   └── navegacao_paginas.feature
│
├── tests/
│   └── test_navegacao_paginas.py
│
├── evidencias/
│
└── README.md
```

---

## Arquivo

```text
tests/test_navegacao_paginas.py
```

## Código

```python
import re

from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect

scenarios('../features/navegacao_paginas.feature')

URL_LOGIN = "https://local-eats-unisenac.vercel.app/static/login.html"

# Mapeia o nome do link exibido na tela para um trecho esperado da URL.
PAGINAS = {
    "Explorar": {
        "url_contem": "index.html",
    },
    "Meus Favoritos": {
        "url_contem": "profile.html",
    },
    "Meus Pedidos": {
        "url_contem": "orders.html",
    },
}


@given('que o usuário está autenticado na página inicial do LocalEats')
def acessar_pagina_autenticado(page):
    page.goto(URL_LOGIN)
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("novo@teste.com")
    page.get_by_role("textbox", name="Sua senha secreta").click()
    page.get_by_role("textbox", name="Sua senha secreta").fill("teste")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    # Confirma que a navegação principal já está visível antes de seguir
    page.get_by_role("link", name="Explorar").wait_for()


@given(parsers.parse('ele navegou até a página de "{pagina}"'))
def navegar_previamente(page, pagina):
    page.get_by_role("link", name=pagina, exact=True).click()
    url_esperada = PAGINAS[pagina]["url_contem"]
    expect(page).to_have_url(re.compile(url_esperada), timeout=10000)


@when(parsers.parse('ele clica no link "{pagina}"'))
def clicar_no_link(page, pagina):
    page.get_by_role("link", name=pagina, exact=True).click()


@then(parsers.parse('a página de "{pagina}" deve carregar corretamente'))
def validar_pagina_carregada(page, pagina):
    url_esperada = PAGINAS[pagina]["url_contem"]
    # Aguarda a URL mudar para a página esperada
    expect(page).to_have_url(re.compile(url_esperada), timeout=10000)
    # Confirma que a navegação principal continua visível (indica que a
    # página carregou sem travar/quebrar) e que existe pelo menos um
    # título/heading na tela, sinal de que o conteúdo da página renderizou
    expect(page.get_by_role("link", name="Explorar")).to_be_visible()
    expect(page.get_by_role("heading").first).to_be_visible()
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest -v tests/test_navegacao_paginas.py
```

---

## Resultado

```text
===================================================== test session starts =====================================================
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Admin\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Admin\Documents\ADS\Qualidade de Software\qualidade-software
plugins: anyio-4.9.0, base-url-2.1.0, bdd-8.1.0, playwright-0.8.0
collected 3 items

tests/test_navegacao_paginas.py::test_navegar_para_a_página_de_meus_favoritos PASSED                                     [ 33%]
tests/test_navegacao_paginas.py::test_navegar_para_a_página_de_meus_pedidos PASSED                                       [ 66%]
tests/test_navegacao_paginas.py::test_retornar_para_a_página_de_explorar PASSED                                          [100%]

====================================================== 3 passed in 9.74s ======================================================
```

**Total de cenários:** 3
**Passaram:** 3
**Falharam:** 0


---

# 🔹 5. Evidências

## Print da execução

```text
evidencias/
  execucao-testes.png
```

## Print da aplicação

```text
evidencias/
  navegacao-meus-favoritos.png
  navegacao-meus-pedidos.png
```

---

# 🔹 6. Análise crítica

## O cenário escrito ficou compreensível?

Sim. A estrutura Given-When-Then deixa claro que o comportamento esperado é simples: clicar em um link do menu deve levar à página correta, carregada corretamente.

## O teste automatizado ficou legível?

Sim. O uso de um dicionário (`PAGINAS`) para mapear nomes de página a trechos de URL deixou os steps reutilizáveis e evitou repetir lógica para cada página testada.

## O BDD ajudou a entender o comportamento?

Sim. Ficou fácil comunicar, em linguagem simples, que a navegação deve ser confiável — algo que qualquer pessoa da equipe entende sem precisar ler código.

## Quais dificuldades surgiram?

- **Troca de fluxo durante a atividade:** tive dificuldade para validar o fluxo escolhido inicialmente (busca de restaurantes) — não estava conseguindo fazer com que os 3 testes passassem, mesmo após diversas tentativas de ajuste (esperas assíncronas, digitação simulada, condições de espera mais robustas). Pelo nível de dificuldade encontrado, resolvi mudar de fluxo para um já testado e mais estável (navegação entre páginas).

## Os seletores foram frágeis?

Pouco frágeis. Usar `get_by_role("link", name=..., exact=True)` depende da semântica de acessibilidade (papel de link + texto acessível), que tende a mudar bem menos do que classes CSS ou estrutura de HTML.

## O teste ficou dependente da interface?

Minimamente. Como as validações usam papel semântico (`link`, `heading`) e trecho de URL, mudanças visuais (cores, layout, posição dos elementos) não devem quebrar o teste. Uma mudança nos nomes exibidos nos links, porém, exigiria atualização dos testes.

## O cenário representa realmente uma regra de negócio?

Sim. Garantir que a navegação entre as áreas principais do sistema funcione é uma regra de negócio essencial — sem isso, o usuário não consegue acessar suas funcionalidades básicas (ver favoritos, acompanhar pedidos, explorar restaurantes).

## O que tornaria o teste mais robusto?

- Validar também algum conteúdo específico de cada página (por exemplo, um heading com o texto exato de cada seção), assim que esse detalhe estiver disponível
- Adicionar verificação de que a página anterior realmente foi "trocada" (por exemplo, checando que um elemento exclusivo da página anterior não está mais visível)
- Testar também a navegação via URL direta (digitar a URL, não só clicar no menu) e o botão de voltar do navegador

---

# 🔹 7. Reflexão no contexto do LocalEats

## BDD melhora a comunicação entre equipe?

Sim. Mesmo neste fluxo simples, o cenário em Gherkin comunica exatamente o que se espera do sistema, sem exigir que quem lê conheça a implementação da navegação.

## Todo teste deve ser escrito em BDD?

Não. BDD faz mais sentido para fluxos que representam decisões de negócio relevantes. Testes muito técnicos ou de baixo nível não precisam necessariamente desse formato.

## Quando vale a pena usar BDD?

Quando o comportamento esperado precisa ser compreendido e validado por pessoas técnicas e não técnicas, e quando o fluxo representa algo importante para a experiência do usuário — como é o caso da navegação principal do sistema.

## O comportamento ficou mais claro?

Sim. Ficou explícito que "carregar corretamente" significa, neste contexto, a URL certa, o menu continuar acessível e algum conteúdo (heading) estar presente — uma definição que poderia ter ficado implícita e ambígua sem o cenário escrito antes da automação.

## Como isso ajuda no projeto do grupo?

Além de validar continuamente que a navegação básica do LocalEats não quebra, essa atividade também documentou um processo real de tomada de decisão em QA: identificar quando um fluxo está instável demais para ser automatizado no prazo disponível, reportar o problema encontrado (bug da busca) e redirecionar o esforço para um fluxo que agrega valor com mais previsibilidade.

---

# 📦 Repositório GitHub

```text
https://github.com/m4theusrohrig/qualidade-software
```

---

# ✅ Conclusão

A atividade permitiu compreender:

- escrita de cenários BDD utilizando Gherkin
- estruturação de comportamentos em Given-When-Then
- automação orientada a comportamento com pytest-bdd e Playwright, incluindo autenticação prévia via login
- uso de seletores baseados em papel semântico (`role`) para maior resiliência a mudanças visuais
- como o BDD pode revelar divergências entre requisito esperado e implementação real (bug real encontrado na busca por texto)
- a importância de saber redirecionar esforço de teste quando um fluxo se mostra instável, priorizando entregar valor dentro do prazo