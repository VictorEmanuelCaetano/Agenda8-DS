# 📋 Pesquisa de Satisfação

Sistema de coleta de opiniões de clientes via terminal, desenvolvido em Python. Registra respostas de até 50 pessoas e exibe um resumo das avaliações ao final.

---

## 🚀 Como usar

1. **Clone ou baixe** o arquivo do script.
2. **Execute** com Python 3.10 ou superior:

```bash
python pesquisa.py
```

3. Responda às perguntas para cada participante:
   - Nome
   - Idade
   - Avaliação do atendimento: `RUIM`, `BOM` ou `EXCELENTE`

4. Ao final das 50 rodadas (ou quando encerrado), o programa exibe o **resumo das opiniões**.

---

## 📦 Requisitos

- Python **3.10+** (necessário para usar `match/case`)

---

## 🖥️ Exemplo de execução

```
Qual é o seu nome? Maria
Qual é o sua idade? 34
Como voce avalia nosso atendimento? RUIM, BOM, EXCELENTE: excelente

Qual é o seu nome? João
Qual é o sua idade? 22
Como voce avalia nosso atendimento? RUIM, BOM, EXCELENTE: bom

...

Quantidade de opiniões no total: 2
Excelente: 1
Bom: 1
Ruim: 0
```

---

## ⚠️ Observações

- O programa aceita as opiniões em **qualquer combinação de maiúsculas/minúsculas** (ex: `Bom`, `BOM`, `bom`).
- Respostas inválidas exibem uma mensagem de erro e **pulam para o próximo participante**, sem contar na contagem.
- As variáveis `qtdRuim`, `qtdBom` e `qtdExelente` precisam ser **inicializadas antes do loop** para o código funcionar corretamente:

```python
qtdRuim = 0
qtdBom = 0
qtdExelente = 0
```
