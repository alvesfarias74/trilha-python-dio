# trilha-python-dio - Sistema Bancário em Python #

Desafio para o Luizalabs - Back-end com Python - otimizar um sistema bancário simples desenvolvido em Python, com foco em modularização, organização e boas práticas de programação. Ele permite realizar operações bancárias como depósito, saque, visualização de extrato, cadastro de usuários e criação de contas correntes.

## 🧱 Estrutura do Projeto

O sistema foi estruturado com funções separadas para cada operação, facilitando a manutenção e expansão do código. As principais funcionalidades são:

- Depósito
- Saque
- Extrato
- Cadastro de usuário
- Criação de conta corrente
- Listagem de contas

## 🛠️ Funcionalidades e Regras

### 🔐 Cadastro de Usuário

- Cada usuário é identificado por CPF (apenas números).
- Dados armazenados: nome completo, data de nascimento, CPF e endereço.
- O endereço deve seguir o formato: `logradouro, nro - bairro - cidade/sigla estado`.
- Não é permitido cadastrar dois usuários com o mesmo CPF.

### 🏦 Criação de Conta Corrente

- Cada conta possui:
  - Agência fixa: `0001`
  - Número sequencial de conta
  - Usuário vinculado
- Um usuário pode ter várias contas, mas cada conta pertence a apenas um usuário.

### 💸 Depósito

- Recebe argumentos apenas por posição.
- Valida se o valor é positivo.
- Atualiza saldo e histórico de extrato.

### 🏧 Saque

- Recebe argumentos apenas por nome.
- Valida:
  - Se há saldo suficiente
  - Se o valor não excede o limite por saque
  - Se o número de saques não excede o limite diário
- Atualiza saldo, extrato e contador de saques.

### 📄 Extrato

- Exibe todas as movimentações realizadas.
- Recebe saldo por posição e extrato por nome.

## 📦 Organização do Código

As funções foram separadas conforme boas práticas:

- `depositar(saldo, valor, extrato, /)`
- `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
- `exibir_extrato(saldo, /, *, extrato)`
- `criar_usuario(usuarios)`
- `criar_conta(agencia, contas, usuarios)`
- `listar_contas(contas)`
- `encontrar_usuario(cpf, usuarios)`

## 📋 Menu Interativo

O sistema é executado em loop com um menu interativo que permite ao usuário escolher entre as operações disponíveis:
