# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Busca de restaurantes
- Login e cadastro de usuários
- Visualização de cardápios
- Sistema de avaliações
- Favoritos
- Recomendações personalizadas

---

## 2. Níveis de Teste

### Funcionalidade: Busca de restaurantes

- verificar o funcionamento dos filtros de busca (culinária, localização e faixa de preço)
- validar a comunicação entre o sistema de busca e o banco de dados
- confirmar que a pesquisa completa retorna restaurantes compatíveis com os critérios definidos
- Aceitação: garantir que o usuário consiga localizar restaurantes de acordo com os critérios informados

### Funcionalidade: Login e cadastro de usuários
- Unitário:  verificar a validação de campos obrigatórios, formato de e-mail e critérios de senha
- Integração: validar a comunicação entre o sistema de autenticação e o banco de dados de usuários
- Sistema:  confirmar o fluxo completo de cadastro e login, incluindo o tratamento de credenciais inválidas
- Aceitação: garantir que o usuário consiga se cadastrar e acessar o sistema de forma rápida e sem erros

### Funcionalidade: Visualização de cardápios
- Unitário: verificar a exibição correta dos dados de cada item do cardápio (nome, descrição, preço e categoria)
- Integração: validar a comunicação entre o módulo de cardápios e o banco de dados do restaurante
- Sistema:  confirmar que o cardápio completo é carregado corretamente ao acessar a página do restaurante
- Aceitação: garantir que o usuário consiga visualizar o cardápio com clareza e sem informações incorretas ou ausentes

### Funcionalidade: Sistema de avaliações
- Unitário: verificar a validação da nota atribuída e dos campos do comentário (limite de caracteres, campos obrigatórios)
- Integração: validar a comunicação entre o módulo de avaliações e o banco de dados, garantindo o correto armazenamento das notas e comentários
- Sistema: confirmar que a avaliação enviada pelo usuário é processada e exibida corretamente no perfil do restaurante
- Aceitação: garantir que o usuário consiga avaliar um restaurante e visualizar sua avaliação refletida de forma adequada na plataforma

### Funcionalidade: Favoritos
- Unitário: verificar a lógica de adicionar e remover um restaurante da lista de favoritos
- Integração:  validar a comunicação entre o módulo de favoritos e o banco de dados, garantindo o correto armazenamento das preferências do usuário
- Sistema: confirmar que a lista de favoritos é atualizada e exibida corretamente após as ações do usuário
- Aceitação: garantir que o usuário consiga marcar, remover e acessar seus restaurantes favoritos sem dificuldades

### Funcionalidade: Recomendações personalizadas
- Unitário:  verificar a lógica do algoritmo que gera as sugestões com base nas preferências e no histórico do usuário
- Integração: validar a comunicação entre o módulo de recomendações e as fontes de dados (histórico de pedidos, avaliações e favoritos)
- Sistema: confirmar que as recomendações são geradas e exibidas corretamente ao usuário em diferentes cenários de uso
- Aceitação: garantir que o usuário receba sugestões relevantes e alinhadas aos seus interesses e hábitos na plataforma

---

## 3. Prioridades e Riscos

Alta prioridade:
- Busca de restaurantes → Trata-se da funcionalidade central da plataforma. Resultados incorretos comprometem diretamente o propósito do sistema.

- Login e cadastro → Sem um mecanismo de autenticação adequado, o usuário fica impossibilitado de acessar recursos personalizados.

- Avaliações → A perda de avaliações compromete a confiabilidade da plataforma e abala a confiança dos usuários.

Média prioridade:
- Visualização de cardápios → Tem papel relevante na tomada de decisão dos usuários, mas sua falha não impede totalmente o uso do sistema.

- Recomendações personalizadas → Agregam valor à experiência do usuário, porém não são indispensáveis para o funcionamento básico da plataforma.

Baixa prioridade: 
- Favoritos → Contribui para uma experiência mais agradável, mas sua indisponibilidade não compromete o uso das demais funcionalidades.

---

## 4. Pirâmide de Testes

- Maior foco: Testes unitários → Os testes unitários devem concentrar a maior parte da estratégia de testes, já que são rápidos, de baixo custo e permitem identificar falhas ainda nas etapas iniciais do desenvolvimento.
- Médio foco: Testes de integração → Devem garantir que a comunicação entre componentes essenciais — como banco de dados, autenticação e mecanismos de busca — ocorra de forma correta.
- Menor foco: Testes de sistema e aceitação → Por serem mais custosos e demandarem mais tempo, devem ser reservados para validar os fluxos completos do sistema e a experiência real do usuário.

Justificativa:

A adoção da pirâmide de testes possibilita a identificação de defeitos de forma mais eficiente e econômica, reduzindo os custos de correção e elevando a confiabilidade geral do sistema.

---

## 5. Testes em Produção

- Uso de testes em produção pode ser feito de maneira controlada e limitada.

- Aplicar em:
* Monitoramento de desempenho nos horários de maior movimento
* Testes com variações de funcionalidades para parte dos usuários antes do lançamento completo
* Identificação de erros específicos de certos dispositivos ou navegadores
* Verificação contínua da disponibilidade das funcionalidades críticas

Justificativa:
A adoção de testes em produção nessas situações permite identificar problemas que só se manifestam em condições reais de uso, como picos de acesso, diversidade de dispositivos e comportamento real dos usuários. Essa abordagem complementa os testes realizados em etapas anteriores, contribuindo para maior estabilidade e confiabilidade do sistema sem comprometer a experiência do usuário.