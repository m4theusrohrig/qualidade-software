# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes
- Matheus Röhrig - 071900826

---

## 📁 Estrutura do Projeto

.  
├── src/   
│   └── entrega.py  
└── tests/   
    └── test_entrega.py  

---

## 🔹 1. Funcionalidades escolhidas

### 👤 Funcionalidade: Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/entrega.py`  
**Arquivo de testes:** `/tests/test_entrega.py`

#### Descrição
Calcula o valor da taxa de entrega cobrada do cliente com base na distância (km) entre o restaurante e o endereço de entrega.

#### Regras de negócio
- Distância até 3km → taxa fixa de **R$ 5,00**
- Distância acima de 3km → taxa fixa + **1,50** por km excedente
- Distância negativa → deve lançar erro (entrada inválida)

---

## 🔹 2. Testes Unitários

Os testes unitários foram implementados no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Testes – Taxa de Entrega

#### Teste 1 – Distância até 3km

- Cenário: Taxa fixa  
- Dados de entrada: distancia_km = 2
- Resultado esperado: 5  

##### TDD
- Red: ImportError, função ainda não existia  
- Green: retorno fixo  
- Refactor: subistituído por constante TAXA_FIXA

##### Refatoração
- Inclusão da constante TAXA_FIXA no lugar do número 5

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Distância acima de 3km

- Cenário: Taxa proporcional
- Dados de entrada: distancia_km = 5 
- Resultado esperado: 8 (5 + 2km x 1,5) 

##### TDD
- Red: função retornava sempre 5, teste falhou (5 != 8)
- Green: implementada lógica condicional com cálculo do excedente 
- Refactor: extraída a função auxiliar _calcular_valor_excedente

##### Refatoração
- Lógica de cálculo do excedente isolada em função própria
-Constantes LIMITE_KM_TAXA_FIXA e VALOR_POR_KM_EXCEDENTE nomeadas

##### Execução
- Resultado: Passou  

---
#### Teste 3 – Distância acima de 3km

- Cenário: Entrada inválida
- Dados de entrada: distancia_km = -1
- Resultado esperado: ValueError("distância inválida")

##### TDD
- Red: nenhuma validação existia, teste falhou
- Green: validação if distancia_km < 0: raise ValueError(...) adicionada
- Refactor: validação extraída para a função _validar_distancia

##### Refatoração
- Validação de entrada separada da lógica de cálculo, melhorando legibilidade

##### Execução
- Resultado: Passou  

---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, pois é necessário pensar no comportamento esperado antes de pensar em como implementar.

---

### O TDD ajudou no desenvolvimento?
Sim, ajudou a estruturar melhor a lógica antes da implementação.

---

### Os testes aumentaram a confiança no código?
Sim, pois qualquer erro pode ser detectado rapidamente.

---

### O que melhorariam?
- Cobrir mais cenários  
- Melhor organização dos testes  

---

### Como isso ajuda no projeto?
Permite evoluir o sistema com mais segurança e qualidade.