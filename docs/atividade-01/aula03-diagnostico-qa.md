# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software
> Aula 3 – Papéis, Responsabilidades e Práticas de QA
> Integrante: Matheus Röhrig Corrêa – 071900826

---

# 1. Diagnóstico da Situação Atual

## 1.1 Papéis atuais identificados

Considerando o cenário descrito, é provável que os seguintes papéis estejam atualmente presentes na startup:

* Desenvolvedor
* Analista de Sistemas
* Gerente de Produto (Product Owner)

---

## 1.2 Quem é responsável pela qualidade hoje?

No momento, a responsabilidade pela qualidade parece estar diluída de maneira informal entre os próprios desenvolvedores, sem a existência de um profissional ou processo dedicado à validação das funcionalidades antes da entrega. Essa lacuna favorece o surgimento de defeitos no ambiente de produção.

---

## 1.3 Problemas identificados

* Funcionalidades chegam à produção com defeitos
* Falhas ocorrem durante a finalização de pedidos
* Restaurantes recebem pedidos duplicados
* Não há clareza na definição das responsabilidades relacionadas à qualidade
* Faltam processos formais de teste e validação

---

## 1.4 Impactos desses problemas

Esses problemas impactam diretamente a experiência dos usuários e a credibilidade da plataforma. Como consequência, clientes podem abandonar o uso do sistema, restaurantes podem perder a confiança no serviço, e a empresa fica exposta a prejuízos financeiros e danos à sua reputação.

---

## 1.5 A qualidade é responsabilidade de quem?

A responsabilidade pela qualidade deve ser compartilhada por toda a equipe. Embora exista o papel de QA para coordenar e dar suporte às atividades relacionadas à qualidade, desenvolvedores, analistas, gestores e demais profissionais também devem se envolver na prevenção de defeitos e na melhoria contínua do produto.

---

# 2. Papéis da Equipe Propostos

## 2.1 Lista de papéis

* Desenvolvedor
* Analista de Qualidade (QA)
* Analista de Sistemas
* DevOps
* Product Owner

---

## 2.2 Descrição dos papéis

Aqui está a tabela com as colunas reescritas:

| Papel                      | Responsabilidades principais                                  | Relação com a qualidade                                                  |
| -------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Desenvolvedor              | Desenvolver funcionalidades e solucionar defeitos identificados | Escrever código confiável e executar testes preliminares antes da entrega  |
| Analista de Qualidade (QA) | Planejar, executar e monitorar os testes do sistema              | Assegurar a qualidade do produto antes do lançamento                       |
| Analista de Sistemas       | Coletar requisitos e documentar as regras de negócio             | Assegurar a clareza e a correção dos requisitos levantados                 |
| DevOps                     | Administrar a infraestrutura e os processos de implantação      | Assegurar estabilidade, disponibilidade e monitoramento contínuo do sistema |
| Product Owner              | Definir prioridades das funcionalidades e validar as entregas   | Assegurar que o produto esteja alinhado às necessidades do negócio         |

---

# 3. Práticas de QA Sugeridas

## 3.1 Lista de práticas

* Testes manuais das funcionalidades principais
* Registro e acompanhamento de bugs
* Revisão de requisitos antes do desenvolvimento
* Revisão de funcionalidades antes da entrega
* Testes exploratórios periódicos

---

## 3.2 Explicação das práticas

### Prática 1

**Descrição:**
Executar testes manuais nas funcionalidades críticas para detectar falhas antes da publicação.

### Prática 2

**Descrição:**
Utilizar uma ferramenta de gerenciamento de defeitos para registrar, priorizar e corrigir os bugs identificados.

### Prática 3

**Descrição:**
Analisar os requisitos antes do desenvolvimento para evitar ambiguidades e interpretações equivocadas.

### Prática 4

**Descrição:**
Analisar os requisitos antes do desenvolvimento para evitar ambiguidades e interpretações equivocadas.

### Prática 5

**Descrição:**
Realizar testes exploratórios periodicamente para identificar problemas não contemplados nos cenários planejados.

---

# 4. Anúncios de Contratação

## 4.1 Vaga 1 – Analista de Qualidade de Software (QA)

### Descrição da vaga

A Local Eats está em busca de um Analista de Qualidade de Software (QA) responsável por assegurar a qualidade das funcionalidades desenvolvidas pela equipe. O profissional atuará junto a desenvolvedores e analistas, identificando riscos, validando entregas e contribuindo para a evolução contínua do produto.

### Responsabilidades

* Planejar e conduzir os testes de software
* Identificar, registrar e monitorar defeitos até sua resolução
* Auxiliar na definição dos critérios de qualidade do produto
* Conduzir testes exploratórios e funcionais
* Atuar junto à equipe de desenvolvimento na prevenção de falhas

### Requisitos obrigatórios

* Noções básicas sobre testes de software
* Habilidade para documentar defeitos de forma clara
* Noções básicas sobre desenvolvimento de sistemas
* Boa capacidade de comunicação e colaboração em equipe

### Requisitos desejáveis

*Vivência com aplicações web
* Familiaridade com ferramentas de gestão de defeitos
* Conhecimentos introdutórios em automação de testes
* Familiaridade com Git e controle de versionamento

### Certificações desejáveis

* ISTQB CTFL (Certified Tester Foundation Level)

---

## 4.2 Vaga 2 – Desenvolvedor Full Stack

### Descrição da vaga

A Local Eats procura um Desenvolvedor Full Stack para contribuir com o desenvolvimento e a manutenção de sua plataforma web e mobile. O profissional ficará encarregado de implementar novas funcionalidades, corrigir defeitos e apoiar as práticas de qualidade adotadas pela equipe.

### Responsabilidades

* Implementar novas funcionalidades no sistema
* Solucionar defeitos apontados pela equipe de QA
* Participar das revisões de código realizadas pela equipe
* Executar testes preliminares antes da entrega das funcionalidades
* Contribuir para a melhoria contínua da plataforma

### Requisitos obrigatórios

* Conhecimento em desenvolvimento web
* Conhecimento de banco de dados
* Lógica de programação
* Conhecimento em controle de versão com Git

### Requisitos desejáveis

* Vivência com APIs REST
* Conhecimentos em desenvolvimento para dispositivos móveis
* Familiaridade com testes automatizados
* Experiência com metodologias ágeis de desenvolvimento

### Certificações desejáveis

* Cursos voltados ao Desenvolvimento Web Full Stack
* Certificações relacionadas às tecnologias adotadas pela empresa

---

# 5. Conclusão da Equipe

A atividade possibilitou compreender a relevância de definir claramente os papéis, as responsabilidades e os processos voltados à qualidade de software. Constatou-se que a falta de uma estrutura organizada de QA favorece o surgimento de defeitos e de problemas operacionais.

Entre as principais melhorias propostas, destacam-se a criação de um papel específico de QA, a implementação de práticas de teste e acompanhamento de defeitos, além da distribuição da responsabilidade pela qualidade entre todos os integrantes da equipe.