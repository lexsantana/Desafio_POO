## Desafio POO – Sistema Bancário em Python (DIO)

*Este projeto implementa a solução do Desafio de Programação Orientada a Objetos (POO) da trilha Python da DIO.
O objetivo foi refatorar o sistema bancário, substituindo estruturas baseadas em dicionários por uma arquitetura composta por classes, seguindo boas práticas de POO e o modelo UML proposto.*

------------------------------------------------------------

### 🧩Objetivo do Desafio

- Criar classes para modelar:
  - Cliente
  - Pessoa Física
  - Conta
  - Conta Corrente
  - Historico
  - Transacao
  - Deposito
  - Saque
- Utilizar herança, encapsulamento e polimorfismo.
- Permitir operações bancárias:
  - Depósito  
  - Saque  
  - Extrato  
  - Criação de clientes  
  - Criação de contas  
  - Listagem de contas  

- Atualizar o menu para trabalhar diretamente com os objetos criados.

------------------------------------------------------------

### 🛠️ Tecnologias utilizadas
- Python 3.12
- POO (Programação Orientada a Objetos)
- pytest para testes automatizados
- Git & GitHub para versionamento

------------------------------------------------------------

### 📂 Estrutura do Projeto

Desafio_POO/

│

├── Resolucao_desafio_poo.py _-> Implementação completa do sistema bancário em POO_

├── .gitignore

├── README.md

│

└── tests/
        
            └── test_conta.py _-> Testes com pytest para validar as operações básicas_ 



------------------------------------------------------------

### 🏗️ Como a solução foi implementada

 - Cliente e PessoaFisica:
	 - Armazenam dados do usuário.
    - Podem possuir múltiplas contas.
    - Realizam transações através do método realizar_transacao.

- Conta e ContaCorrente:
	- Controlam saldo, saques e depósitos.
	- ContaCorrente adiciona limites e número máximo de saques.
	- Cada conta possui um objeto Historico.

- Transacao:
	- Classe abstrata para operações bancárias (Deposito e Saque).
	- Cada operação registra valor, tipo e timestamp.

- Historico:
	- Armazena todas as transações da conta.

------------------------------------------------------------

### 🚀 Como executar o projeto

    python Resolucao_desafio_poo.py

O menu será exibido no terminal.

------------------------------------------------------------

### 🧪 Rodar os testes

    pytest -q

Valida:
- Depósitos
- Saques
- Regras de saldo
- Registro de transações

------------------------------------------------------------

### 📘 Funcionalidades principais

- Criar clientes e contas
- Depositar e sacar com validações
- Extrato detalhado com timestamp
- Suporta múltiplas contas por cliente
- Histórico completo de transações

------------------------------------------------------------

### 📄 Licença
Uso livre para fins de estudo e aperfeiçoamento.
