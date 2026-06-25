# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrante:  
- Matheus Röhrig - 071900826

---

# 1. Plano de Testes

## 1.1 Objetivo
Validar as principais funcionalidades do LocalEats — cadastro/login, busca de restaurantes, visualização de cardápio, realização de pedido e avaliação — garantindo que atendam aos requisitos funcionais esperados e apresentem comportamento consistente diante de cenários comuns e de borda.

---

## 1.2 Escopo

### O que será testado
- Login/Cadastro de usuário
- Busca de restaurantes
- Visualização de cardápio
- Realização de pedido
- Avaliação do restaurante

### O que NÃO será testado
- Integração com gateways de pagamento reais
- Envio de notificações push
- Painel administrativo do restaurante (gestão de cardápio pelo lojista)
- Testes de carga/performance em escala (apenas avaliação qualitativa de tempo de resposta)

---

## 1.3 Funcionalidades selecionadas

- Login/Cadastro
- Busca de restaurantes
- Visualização de cardápio
- Pedido
- Avaliação

---

## 1.4 Estratégia de Testes

- Tipos de teste:
  - (x) Funcional
  - (x) Usabilidade
  - (x) Outros: Testes exploratórios

- Abordagem:
  > Testes manuais baseados em cenários previamente definidos (caminho feliz + condições de borda), complementados por testes exploratórios para identificar problemas não cobertos pelos casos formais (ex.: duplo clique, conexões instáveis).

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome           | Responsabilidade                                    |
|----------------|-----------------------------------------------------|
| Matheus Röhrig | Elaboração dos casos de teste e critérios de aceite |
| Matheus Röhrig | Execução dos testes e registro de evidências        |
| Matheus Röhrig | Consolidação dos resultados e do relatório final    |
| Matheus Röhrig | Revisão da cobertura e da qualidade dos casos       |

---

# 2. Casos de Teste

## CT-01 – [Título do teste]

**Pré-condição:**  
Usuário possui conta cadastrada e ativa no LocalEats.

**Passos:**  
1. Acessar a tela de login.
2. Informar e-mail e senha válidos.
3. Clicar em "Entrar".  

**Dados de entrada (se aplicável):**  
E-mail: usuario@teste.com / Senha: Teste@123

**Resultado esperado:**  
Usuário autenticado e redirecionado à tela inicial, com seu nome exibido no cabeçalho.

---

## CT-02 – [Título do teste]

**Pré-condição:**  
Usuário autenticado; existe ao menos um restaurante cadastrado com nome acentuado (ex.: "Pizzaria Itália").

**Passos:**  
1. Acessar a barra de busca na tela inicial.
2. Digitar parte do nome do restaurante, sem acentuação.
3. Confirmar a busca.

**Dados de entrada (se aplicável):**  
Termo de busca: "pizzaria italia"

**Resultado esperado:**  
Lista de restaurantes contendo "Pizzaria Itália" é exibida, mesmo sem o usuário ter digitado a acentuação correta.

---

## CT-03 – [Título do teste]

**Pré-condição:**  
Restaurante selecionado possui cardápio cadastrado com itens, categorias, preços e fotos.

**Passos:**  
1. Selecionar um restaurante na lista de resultados.
2. Acessar a aba "Cardápio".
3. Navegar pelas categorias disponíveis.

**Dados de entrada (se aplicável):**  
Conexão simulada: 3G (rede lenta)

**Resultado esperado:**  
Cardápio carregado em até 3 segundos, exibindo nome, descrição, preço e foto de cada item, organizados por categoria.

---

## CT-04 – [Título do teste]

**Pré-condição:**  
Usuário autenticado, cardápio aberto, item disponível em estoque.

**Passos:**  
1. Selecionar um item do cardápio.
2. Clicar em "Adicionar ao carrinho".
3. Acessar o carrinho e clicar em "Finalizar pedido".
4. Confirmar endereço de entrega e forma de pagamento.
 

**Dados de entrada (se aplicável):**  
Item: Pizza Calabresa / Quantidade: 1 / Pagamento: cartão de crédito

**Resultado esperado:**  
Pedido confirmado uma única vez, com número de protocolo gerado e status "Em preparo".

---

## CT-05 – [Título do teste]

**Pré-condição:**  
Pedido do usuário com status "Entregue".

**Passos:**  
1. Acessar o histórico de pedidos.
2. Selecionar o pedido entregue.
3. Clicar em "Avaliar".
4. Atribuir nota (1 a 5 estrelas) e escrever um comentário.
5. Enviar a avaliação.

**Dados de entrada (se aplicável):**  
Nota: 5 estrelas / Comentário: "Entrega rápida, comida ainda quente."

**Resultado esperado:**  
Avaliação registrada e exibida no perfil do restaurante; opção de avaliar removida do pedido já avaliado.

---

# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou)  | Evidência (descrição ou print)                                                                                                                |
|--------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| CT-01  | Passou                     | Login concluído normalmente, nome do usuário exibido no cabeçalho.                                                                            |
| CT-02  | Falhou                     | Busca por "pizzaria italia" (sem acento) não retornou "Pizzaria Itália"; algoritmo de busca não normaliza acentuação.                         |
| CT-03  | Falhou                     | Em conexão 3G simulada, o carregamento do cardápio levou ~6s e algumas fotos exibiram placeholder quebrado.                                   |
| CT-04  | Passou (com ressalva)      | Pedido finalizado com sucesso; porém, ao clicar duas vezes rapidamente em "Finalizar pedido", foram gerados 2 pedidos idênticos no histórico. |
| CT-05  | Passou                     | Avaliação registrada corretamente e exibida no perfil do restaurante.                                                                         |

---

# 4. Análise dos Resultados

- Quantidade de testes executados: 5
- Quantidade de testes que passaram: 3 (CT-01, CT-04, CT-05)
- Quantidade de testes que falharam: 2 (CT-02, CT-03)

## Principais problemas encontrados
- Busca não normaliza acentuação, retornando falsos negativos para termos sem acento (CT-02).
- Carregamento do cardápio é lento e instável em redes ruins, com falha no carregamento de imagens (CT-03).
- Duplo clique no botão "Finalizar pedido" pode gerar pedidos duplicados — problema identificado durante a execução do CT-04, fora do roteiro original.

---

# 5. Reflexão

- O plano de testes ajudou a organizar melhor o processo? Por quê?

Sim. Definir previamente pré-condições, passos e resultados esperados deixou a execução mais objetiva e facilitou a comparação entre o comportamento esperado e o observado, tornando mais fácil apontar exatamente onde cada funcionalidade falhou.

- Algum problema só foi identificado durante a execução? Explique.

Sim. A possibilidade de pedido duplicado por duplo clique não estava prevista em nenhum caso de teste formal — ela surgiu de uma interação exploratória durante a execução do CT-04, reforçando a importância de complementar os casos escritos com testes exploratórios.

- O que o grupo melhoraria no processo de testes?

Incluir casos específicos para cenários de rede degradada (cardápio), testes de internacionalização/normalização de texto para a busca, e casos voltados a concorrência de cliques/requisições, já que esses pontos só foram percebidos de forma incidental.
---

## Conclusão

O comportamento das funcionalidades testadas foi considerado parcialmente aceitável. Login, pedido e avaliação atenderam aos requisitos esperados, mas busca e visualização de cardápio apresentaram falhas (acentuação e performance/carregamento de imagens) que precisam ser corrigidas antes de uma liberação para produção.
---

# 6. Conclusão Geral

- **Qualidade geral do sistema testado:** razoável — funcionalidades centrais (login, pedido, avaliação) funcionam de forma estável, mas há pontos de atenção relevantes em busca e desempenho de carregamento.
- **Principais pontos positivos:** fluxo de pedido completo e funcional, fluxo de avaliação simples e sem erros, autenticação estável.
- **Principais problemas identificados:** busca sem normalização de acentos, lentidão/falha no carregamento de imagens do cardápio em redes ruins, risco de duplicidade de pedidos por duplo clique.
- **Impressão geral do grupo sobre o processo de testes:** o processo estruturado ajudou a antecipar problemas que impactariam diretamente a experiência do usuário, e os testes exploratórios complementares foram essenciais para revelar falhas que os casos formais não cobririam.