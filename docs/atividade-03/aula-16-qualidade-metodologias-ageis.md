# Aula 16 – Qualidade em Metodologias Ágeis

## Integrantes
- Matheus Rohrig -071900826

---

# 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcial | Cada aula do PBL funciona como um ciclo curto, com escopo e entrega próprios, que constroem sobre o resultado da aula anterior. | Sim — poderia haver um planejamento explícito por ciclo, com objetivos e critérios de aceite definidos antes de iniciar cada entrega. |
| Priorização de funcionalidades | Parcial | O que será trabalhado em cada aula é definido pelo professor conforme o cronograma da disciplina, não por um backlog próprio. | Sim — poderia existir um backlog pessoal das funcionalidades do LocalEats, priorizado por risco ou importância. |
| Entregas incrementais | Sim | Cada aula gera um artefato incremental (mapeamento de processo, diagnóstico de maturidade, análise ágil), que se conecta ao anterior e evolui o entendimento do projeto. | Sim — as entregas poderiam ser fatiadas em incrementos ainda menores, com validação mais frequente. |
| Feedback frequente | Parcial | O feedback principal vem da rubrica de avaliação do professor a cada entrega. | Sim — poderia haver checkpoints intermediários de autoavaliação antes da entrega final, simulando um "review" mais frequente. |
| Trabalho colaborativo | Não | O trabalho é realizado de forma individual, sem outros integrantes no grupo. | Sim — ainda que individual, poderia simular papéis (ex.: revisar o próprio trabalho como se fosse outro integrante) para reduzir vieses. |
| Controle visual das atividades | Não | Não há quadro Kanban ou ferramenta visual; o acompanhamento é feito de forma implícita, seguindo a sequência das aulas. | Sim — um quadro simples (Trello, GitHub Projects) tornaria visível o status de cada entrega (a fazer, em andamento, concluído). |
| Melhoria contínua | Parcial | As reflexões escritas ao final de cada atividade (ex.: Aula 14 e 15) já apontam pontos de melhoria do processo. | Sim — poderia se tornar uma prática formal e recorrente, com ações de melhoria efetivamente aplicadas na atividade seguinte. |

### Conclusão

O processo atual já apresenta algumas características ágeis, especialmente entregas incrementais e uma forma inicial de melhoria contínua através das reflexões escritas em cada aula. Por outro lado, práticas centrais do trabalho ágil em equipe — como trabalho colaborativo, controle visual das atividades e priorização própria do backlog — praticamente não existem, principalmente por se tratar de um trabalho individual conduzido dentro de um cronograma acadêmico fixo. O maior ponto forte é a consistência: cada entrega segue um fluxo parecido e se apoia na anterior. A maior oportunidade de melhoria está em tornar esse fluxo mais explícito e visual, com planejamento e feedback antes da entrega final, e não apenas ao final do processo.

---

# 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|---|---|---|
| Utilizar um quadro Kanban (ex.: GitHub Projects) para acompanhar o status de cada entrega do PBL | Kanban | Maior visibilidade do andamento das atividades e do que ainda falta ser feito |
| Planejar cada entrega em um ciclo curto, com objetivo e critérios de aceite definidos antes de começar | Scrum | Foco mais claro em cada entrega e redução de retrabalho por escopo mal definido |
| Aplicar testes e integração contínua a cada pequena mudança, reforçando o hábito de TDD já usado no projeto | XP (Extreme Programming) | Maior qualidade contínua do código e detecção mais rápida de defeitos |
| Eliminar etapas ou documentações redundantes, mantendo apenas o que agrega valor real à entrega | Lean Software Development | Maior eficiência no processo, com menos desperdício de tempo e esforço |

---

# 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para desenvolvimento quando:

1. A funcionalidade e o enunciado da atividade estiverem claramente entendidos.
2. Os critérios de aceite da funcionalidade estiverem definidos previamente.
3. O comportamento esperado da funcionalidade já tiver sido explorado diretamente no LocalEats.
4. O ambiente de testes (pytest, pytest-bdd, Playwright) estiver configurado e funcional.
5. Não houver dependências pendentes (ex.: acesso ao sistema, bibliotecas instaladas) que impeçam o início do desenvolvimento.

---

# 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

1. Os critérios de aceitação definidos para a funcionalidade tiverem sido atendidos.
2. Os testes manuais e/ou automatizados relacionados tiverem sido executados com sucesso.
3. Eventuais defeitos identificados tiverem sido corrigidos e revalidados.
4. A documentação da entrega estiver atualizada e organizada.
5. O artefato final estiver commitado e versionado no repositório GitHub.