# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrante
- Matheus Röhrig - 071900826

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Visualização de cardápios

**Descrição da funcionalidade:**  
A funcionalidade permite que o usuário visualize o cardápio do restaurante selecionado.

**O que o usuário espera:**  
O usuário espera ver rapidamente todas as opções do restaurante escolhido, com informações claras para decidir o que pedir, e ser avisado caso algo impeça essa visualização.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1:  
**Entrada:** Usuário seleciona um restaurante com cardápio cadastrado e acessa a funcionalidade de visualização de cardápio.  
**Comportamento esperado:** O sistema exibe, em tempo aceitável, todos os itens ativos do restaurante selecionado, organizados por categoria (entradas, pratos principais, bebidas, etc.), com nome, preço, imagem e status de disponibilidade visíveis para cada item.

- Cenário 2:
**Entrada:** Usuário acessa o cardápio de um restaurante que não possui nenhum item cadastrado.  
**Comportamento esperado:** O sistema exibe uma mensagem informativa (ex: "Este restaurante ainda não cadastrou um cardápio"), sem deixar a tela em branco ou travada.

- Cenário 3:
**Entrada:** Usuário acessa o cardápio em uma situação de falha de conexão ou erro no servidor.  
**Comportamento esperado:** O sistema exibe uma mensagem de erro clara (ex: "Não foi possível carregar o cardápio, tente novamente") e oferece uma opção de tentar novamente, sem travar ou fechar o app.

- Cenário 4:  
**Entrada:** Usuário acessa o cardápio de um restaurante que possui itens marcados como indisponíveis/esgotados no momento.  
**Comportamento esperado:** Os itens indisponíveis são exibidos de forma visualmente distinta (ex: esmaecidos, com etiqueta "esgotado") e não podem ser selecionados/adicionados ao pedido.
---

### 🔹 Possíveis erros identificados

- Cardápio não carrega e a tela permanece em branco, sem mensagem de erro ou feedback ao usuário.
- Itens sem imagem cadastrada quebram o layout da tela (espaço vazio, sobreposição de elementos).
- Itens sem preço definido são exibidos sem nenhuma indicação ("R$ --" ou similar), confundindo o usuário.
- Itens esgotados aparecem como disponíveis e permitem que o usuário tente adicioná-los ao pedido.
- Cardápio de um restaurante aparece misturado ou trocado com o de outro restaurante (erro de contexto/sessão).
- Demora excessiva no carregamento sem nenhum indicador visual (loading/skeleton), dando impressão de app travado.
- Categorias duplicadas ou itens repetidos na listagem.
- Ao voltar para a tela anterior e reabrir o cardápio, a ordem ou os dados dos itens mudam de forma inconsistente.  

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
<!-- Descreva a lógica interna da funcionalidade -->
```
Quando o usuário acessa a tela de cardápio, o frontend identifica o restaurante previamente selecionado (armazenado via parâmetro de rota ou estado global) e dispara uma requisição à API informando o `id` desse restaurante. Enquanto espera a resposta, a interface exibe um indicador de carregamento.

No backend, a rota responsável recebe esse `id` e primeiro valida se ele é válido. Caso não seja, retorna um erro tratado informando que o restaurante não foi encontrado. Se o `id` for válido, o sistema consulta o banco de dados buscando apenas os itens de cardápio vinculados àquele restaurante específico — essa filtragem é o ponto mais sensível da implementação, já que qualquer falha nela faria itens de outros restaurantes aparecerem misturados.

Os dados retornados (nome, preço, imagem, categoria e disponibilidade de cada item) chegam ao frontend em formato JSON. O frontend organiza esses itens por categoria e os renderiza na tela, tratando itens indisponíveis de forma visualmente diferenciada e bloqueando sua seleção.

Se a requisição falhar — por problema de rede, erro no servidor ou restaurante sem itens cadastrados — o sistema deveria capturar essa falha e exibir uma mensagem adequada ao usuário, em vez de deixar a tela travada ou em branco.

### 🔹 Situações a serem testadas

- Situação 1: A consulta ao banco retorna exclusivamente os itens vinculados ao `restaurante_id` informado, sem mistura de dados de outros restaurantes.
- Situação 2: O sistema recebe um `id` de restaurante inválido ou inexistente e responde com erro tratado, sem cair em erro genérico (500) ou retorno vazio silencioso.
- Situação 3: O campo de disponibilidade de cada item reflete corretamente o estado real no banco, e o frontend respeita esse valor ao renderizar (bloqueando seleção de itens esgotados).

### 🔹 Possíveis erros identificados

- Filtro de restaurante ausente ou incorreto na consulta, retornando itens de restaurantes diferentes misturados.
- Falta de validação do `id` recebido, permitindo que entradas inválidas cheguem até a consulta ao banco.
- Ausência de tratamento de falha na chamada da API pelo frontend, resultando em tela branca silenciosa em caso de erro de rede.

## ⚖️ 4. Comparação entre as abordagens

Qual a principal diferença entre testar sem ver o código e com acesso ao código?

A principal diferença está no ponto de partida da análise. No teste caixa-preta, o foco é exclusivamente no comportamento observável pelo usuário: dado uma entrada, qual é a saída esperada, sem nenhuma suposição sobre como o sistema processa isso internamente. Já no teste caixa-branca, o conhecimento da estrutura interna permite mirar diretamente nos pontos onde a implementação é mais frágil ou propensa a falhas.

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
Ajuda a encontrar problemas de experiência e usabilidade que o usuário final realmente vivenciaria: mensagens de erro ausentes ou confusas, telas que travam ou ficam em branco, informações faltando na interface, comportamento inconsistente entre acessos, e falhas em fluxos alternativos.

Caixa-branca:
Ajuda a encontrar problemas estruturais e de implementação que não seriam visíveis apenas usando o app: falhas de isolamento de dados entre restaurantes, ausência de validação de parâmetros, tratamento de erro mal implementado no código, queries lentas ou sem índice, inconsistência entre dados do banco e o que é exibido, e riscos de concorrência.

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

O teste caixa-preta, pois o projeto ainda está em definição e o foco agora é garantir que o comportamento esperado pelo usuário esteja claro, antes de validar detalhes de implementação.

Apenas uma abordagem seria suficiente? Por quê?

Não. Caixa-preta garante que a funcionalidade atenda ao usuário, mas não revela a causa de falhas internas. Caixa-branca garante que o código é sólido, mas não garante boa experiência. As duas juntas cobrem o que falta uma à outra.

## 🚀 Conclusão

Aprendi que testes caixa-preta e caixa-branca respondem perguntas diferentes e complementares: uma valida se a funcionalidade atende ao usuário, a outra valida se a implementação é sólida. Também ficou claro que critérios de aceite bem definidos são essenciais para saber o que testar.