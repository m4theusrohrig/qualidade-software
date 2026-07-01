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