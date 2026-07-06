# Aula 15 - Modelos de Maturidade

## 👥 Integrantes
- Matheus Rohrig - 071900826

## 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não | Evidência / Justificativa |
|---|---|---|---|---|
| Os requisitos são documentados? | | X | | As atividades do PBL registram objetivos e fluxos esperados das funcionalidades, mas não há um documento formal de requisitos (ex.: histórias de usuário completas) do LocalEats em si. |
| Existe controle de mudanças? | | X | | O Git registra alterações por meio dos commits, mas não há um fluxo formal de abertura, análise e aprovação de mudanças. |
| Há atividades de teste definidas? | X | | | O processo já contempla testes manuais, automatizados, TDD e BDD, aplicados de forma consistente nas atividades anteriores (Aulas 6, 9, 10 e 12). |
| Os defeitos são registrados? | | X | | Defeitos aparecem nas evidências de execução dos testes e nas reflexões das atividades, mas não são registrados de forma padronizada em Issues. |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | | Como o trabalho é individual, o processo mapeado na Aula 14 é seguido de forma consistente em todas as entregas. |
| As tarefas são planejadas e acompanhadas regularmente? | | X | | O cronograma das aulas do PBL guia o planejamento, mas não há um quadro visual ou backlog formal de acompanhamento. |
| Existe padronização para implementação de funcionalidades? | | X | | Há um fluxo semelhante repetido entre atividades (análise, critérios de aceite, testes, correção), mas ainda falta um checklist único documentado. |
| Os testes são executados antes da entrega das funcionalidades? | X | | | O fluxo mapeado na Aula 14 prevê explicitamente a etapa de testes antes da revisão final e entrega. |
| Há revisão de código ou validação por outro integrante da equipe? | | | X | Por se tratar de trabalho individual, não existe revisão por pares; a validação é feita apenas pelo próprio autor. |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | X | | O GitHub é usado para versionamento e organização das entregas, mas ainda não há uso estruturado de GitHub Projects ou Issues. |
| Os artefatos do projeto são organizados e versionados? | X | | | Documentos, testes e evidências ficam organizados em pastas específicas e versionados no repositório do curso. |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | X | | Os testes se relacionam com as funcionalidades trabalhadas (cardápio, taxa de entrega, navegação), mas não há uma matriz formal ligando requisito, teste e entrega. |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | X | | As reflexões escritas ao final de cada atividade do PBL funcionam como uma retrospectiva informal, mas não é uma prática estruturada e recorrente. |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X | Não há métricas contínuas como cobertura de testes, número de defeitos em aberto ou tempo médio de correção. |

### Classificação do Processo

**Nível: Gerenciado**

O processo apresenta práticas básicas de planejamento e execução — testes definidos, versionamento organizado e um fluxo repetível entre atividades —, o que o afasta de um nível puramente **Inicial** (ad hoc). No entanto, ainda faltam elementos que caracterizam um processo **Definido**, como padronização documentada (checklist único), controle formal de mudanças e rastreabilidade estruturada entre requisitos e testes. Práticas de revisão por pares e retrospectivas formais também são inexistentes ou informais, e não há indicadores quantitativos de qualidade, o que descarta os níveis **Quantitativamente Gerenciado** e **Em Otimização**. Por isso, o processo se encontra no estágio **Gerenciado**: organizado o suficiente para produzir resultados consistentes, mas ainda dependente de disciplina individual em vez de práticas institucionalizadas.

## 2. Identificação de Lacunas

| Lacuna | Impacto |
|---|---|
| Falta de métricas de qualidade (cobertura de testes, defeitos em aberto) | Dificulta acompanhar objetivamente a evolução da qualidade do projeto ao longo do tempo. |
| Ausência de revisão por pares | Aumenta o risco de erros ou vieses não percebidos passarem despercebidos antes da entrega. |
| Falta de rastreabilidade formal entre requisitos e testes | Dificulta garantir que todas as funcionalidades relevantes do LocalEats estejam de fato cobertas por testes. |
| Ausência de controle formal de mudanças | Gera risco de perda de contexto sobre por que uma decisão técnica foi tomada ou alterada. |

## 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Implementar métricas simples (nº de testes, taxa de aprovação, defeitos por entrega) | Maior visibilidade objetiva sobre a evolução da qualidade do processo. |
| Criar uma matriz de rastreabilidade requisito → teste → entrega | Garante cobertura mais clara das funcionalidades do LocalEats e facilita auditoria. |
| Adotar um checklist de "Definição de Pronto" (Definition of Done) para cada funcionalidade | Padroniza os critérios de aceite e reduz variação entre entregas. |
| Utilizar GitHub Issues/Projects para registrar defeitos e planejar tarefas | Melhora a gestão do backlog e o registro histórico de problemas encontrados. |

## 4. Conclusão

A avaliação realizada mostra que o processo de desenvolvimento do LocalEats possui práticas que contribuem para a organização e a qualidade das entregas, como o uso de versionamento e a execução de testes antes da finalização das funcionalidades. Por outro lado, ainda existem oportunidades de melhoria relacionadas à padronização do processo, ao controle de mudanças, à rastreabilidade e ao uso de métricas de qualidade. Dessa forma, a classificação no nível Gerenciado é adequada, pois o processo apresenta consistência, mas ainda pode evoluir com a adoção de práticas mais estruturadas e documentadas.