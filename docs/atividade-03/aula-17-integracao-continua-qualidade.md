# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes
- Matheus Rohrig - 071900826

---

## 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| Nome do repositório | localeats-ci |
| Link do repositório | https://github.com/m4theusrohrig/localeats-ci |

### Estrutura de Diretórios

```text
localeats-ci/
├── tests/
│   └── test_delivery_fee.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── delivery_fee.py
├── pytest.ini
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| Título da Issue | Implementar cálculo da taxa de entrega com regra de frete grátis |
| Objetivo da funcionalidade | Calcular a taxa de entrega do pedido com base na distância percorrida, aplicando frete grátis para pedidos a partir de R$ 100,00 |
| Link da Issue | https://github.com/m4theusrohrig/localeats-ci/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|---|---|
| Tipo de teste | Unitário (TDD) |
| Objetivo do teste | Verificar se a taxa de entrega é calculada corretamente conforme a distância, o valor do pedido e as regras de frete grátis e validação de entradas |
| Link para o arquivo do teste | https://github.com/m4theusrohrig/localeats-ci/blob/main/tests/test_delivery_fee.py |

```python
import pytest
from delivery_fee import calculate_delivery_fee


def test_calculate_delivery_fee_basic():
    """3 km de distância: 5.0 + (1.5 * 3) = 9.5"""
    assert calculate_delivery_fee(distance_km=3, order_total=40.0) == 9.5


def test_calculate_delivery_fee_zero_distance():
    """Distância zero: cobra apenas a taxa base"""
    assert calculate_delivery_fee(distance_km=0, order_total=20.0) == 5.0


def test_calculate_delivery_fee_free_shipping():
    """Pedido acima de R$ 100 tem frete grátis, independente da distância"""
    assert calculate_delivery_fee(distance_km=10, order_total=150.0) == 0.0


def test_calculate_delivery_fee_free_shipping_boundary():
    """Pedido exatamente em R$ 100 também tem frete grátis"""
    assert calculate_delivery_fee(distance_km=5, order_total=100.0) == 0.0


def test_calculate_delivery_fee_negative_distance_raises_error():
    with pytest.raises(ValueError):
        calculate_delivery_fee(distance_km=-1, order_total=30.0)


def test_calculate_delivery_fee_negative_order_total_raises_error():
    with pytest.raises(ValueError):
        calculate_delivery_fee(distance_km=2, order_total=-10.0)
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | `push` e `pull_request` na branch `main` |
| Link para o arquivo do workflow | https://github.com/m4theusrohrig/localeats-ci/blob/main/.github/workflows/quality.yml |
| Link de uma execução do workflow | https://github.com/m4theusrohrig/localeats-ci/actions/runs/28882880157 |

```yaml
name: Quality Check

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Executar testes automatizados
        run: pytest -v
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|---|---|
| Quantidade de testes executados | 6 |
| Quantidade de testes aprovados | 6 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso ✅ |

---

## 6. Registro de Defeito

| Item | Descrição |
|---|---|
| Título do defeito | Frete grátis não aplicado corretamente no valor-limite do pedido |
| Severidade | Média |
| Link da Issue | https://github.com/m4theusrohrig/localeats-ci/issues/2 |

O defeito foi simulado alterando a condição de frete grátis de `order_total >= VALOR_FRETE_GRATIS` para `order_total > VALOR_FRETE_GRATIS`, fazendo com que um pedido de exatamente R$ 100,00 não recebesse frete grátis. O problema foi identificado automaticamente pela falha do teste `test_calculate_delivery_fee_free_shipping_boundary` durante a execução do pipeline no GitHub Actions. Após reverter a condição para `>=`, os 6 testes voltaram a passar e o pipeline retornou ao status de sucesso.