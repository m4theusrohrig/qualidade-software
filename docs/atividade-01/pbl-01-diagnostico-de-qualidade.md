# PBL 1 – Diagnóstico Inicial da Qualidade do LocalEats

## Integrante

* Matheus Röhrig Corrêa - 071900826

---

# 1. Cenário

O LocalEats é uma plataforma disponível para web e dispositivos móveis que tem como objetivo aproximar moradores e visitantes de restaurantes independentes da cidade. Por meio do sistema, os usuários podem pesquisar estabelecimentos, consultar cardápios, adicionar restaurantes aos favoritos, receber sugestões personalizadas e compartilhar suas avaliações e experiências.

Após a disponibilização da primeira versão da plataforma, vários usuários relataram problemas durante a utilização, apontando possíveis deficiências relacionadas aos atributos de qualidade do software.

---

# 2. Problemas Identificados e Atributos de Qualidade Afetados

| Problema identificado                             | Atributo de qualidade afetado (ISO/IEC 25010) | Justificativa técnica                                                                            | Impacto para usuário/negócio                                                  |
| ------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Sistema lento em horários de pico                 | Eficiência de Desempenho                      | A aplicação não consegue manter um desempenho adequado quando há grande volume de acessos simultâneos.              | A demora nas respostas pode levar à perda de usuários e reduzir o engajamento na plataforma.              |
| Telas confusas e pouco intuitivas                 | Usabilidade                                   | O design e a organização das informações dificultam a interação e a localização de recursos pelos usuários.         | A experiência de uso torna-se menos agradável, aumentando a chance de desistência do serviço.                         |
| Buscas retornam resultados incorretos             | Adequação Funcional                           | O mecanismo de pesquisa apresenta falhas ao interpretar os critérios informados, gerando resultados inadequados.    | Os usuários podem não encontrar os restaurantes desejados, comprometendo a utilidade da plataforma.                          |
| Falhas em determinados modelos de smartphone      | Compatibilidade                               | Existem problemas de funcionamento em alguns dispositivos devido a diferenças de hardware, software ou configuração.| Parte do público fica impossibilitada de utilizar todos os recursos disponíveis.           |
| Dificuldade para concluir ações simples           | Usabilidade                                   | Os processos de navegação e execução de tarefas exigem etapas desnecessárias ou pouco claras.                       | Usuários podem abandonar ações importantes, reduzindo a efetividade da aplicação.       |
| Avaliações desaparecem após atualização da página | Confiabilidade                                | O sistema apresenta falhas na persistência ou recuperação de dados após determinadas operações.                     | A credibilidade da plataforma é afetada, além do risco de perda de conteúdo gerado pelos usuários. |
| Inconsistências entre versão web e mobile         | Compatibilidade e Adequação Funcional         | As funcionalidades não apresentam o mesmo comportamento ou resultados em diferentes plataformas.                    | Os usuários enfrentam experiências divergentes, aumentando a insatisfação e o número de reclamações.             |

---

# 3. Avaliação Geral da Qualidade

A análise dos problemas identificados demonstra que a aplicação necessita de melhorias para atender adequadamente aos requisitos de qualidade esperados.

Os principais atributos comprometidos são:

* Eficiência de Desempenho
* Usabilidade
* Adequação Funcional
* Confiabilidade
* Compatibilidade

A permanência dessas falhas pode gerar insatisfação dos usuários, além de afetar negativamente a credibilidade da plataforma no mercado.

---

# 4. Priorização dos Problemas

## Alta Prioridade

1. Retorno de resultados incorretos nas pesquisas
2. Perda de avaliações após atualização da página
3. Baixo desempenho em períodos de alta demanda

### Justificativa

Essas falhas possuem impacto direto nas funcionalidades essenciais da plataforma, comprometendo a precisão das informações fornecidas, a integridade dos dados armazenados e a satisfação dos usuários. Por afetarem aspectos críticos do sistema, sua correção deve ser tratada como prioridade.

## Média Prioridade

1. Problemas de funcionamento em determinados modelos de smartphones
2. Diferenças de comportamento entre as versões web e mobile
3. Dificuldades na execução de tarefas básicas pelos usuários

### Justificativa

Embora não inviabilizem completamente o uso da plataforma, esses problemas comprometem a acessibilidade, a uniformidade da experiência e a eficiência da interação em diferentes ambientes de utilização, afetando uma parcela significativa dos usuários.

## Baixa Prioridade

1. Interface com elementos pouco claros ou intuitivos

### Justificativa

Apesar de influenciarem a experiência de navegação e a facilidade de uso, essas questões geralmente não impedem a execução das principais funcionalidades do sistema, podendo ser tratadas após a resolução dos problemas mais críticos.

---

# 5. Conclusão

A avaliação realizada evidencia que o LocalEats apresenta não conformidades relacionadas a diferentes atributos de qualidade estabelecidos pela norma ISO/IEC 25010. Os aspectos mais críticos estão associados à adequação funcional, à confiabilidade e à eficiência de desempenho, uma vez que exercem influência direta sobre a capacidade do sistema de atender adequadamente às expectativas e necessidades dos usuários.

Dessa forma, recomenda-se concentrar os esforços iniciais na correção das falhas relacionadas aos resultados de busca, à preservação das avaliações dos usuários e ao desempenho da aplicação em momentos de alta utilização. A mitigação desses problemas contribuirá para aumentar a confiabilidade, a estabilidade e a qualidade geral da plataforma antes da implementação de novas funcionalidades ou da ampliação de sua base de usuários.