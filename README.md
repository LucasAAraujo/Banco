# Banco Python

Este é um simples sistema bancário desenvolvido em Python, onde é possível realizar operações como criar contas, realizar saques, depósitos, transferências e listar todas as contas cadastradas.

## Funcionalidades

- **Criar Conta:** Registra um novo cliente e cria uma conta bancária associada a ele.
- **Efetuar Saque:** Permite ao usuário sacar valores da sua conta.
- **Efetuar Depósito:** Permite ao usuário depositar valores na sua conta.
- **Efetuar Transferência:** Permite ao usuário transferir valores entre contas.
- **Listar Contas:** Exibe todas as contas cadastradas no sistema.
- **Sair do Sistema:** Encerra o programa.

## Tecnologias Utilizadas

- **Python 3.x**
- **Estruturas de Dados (Listas)**
- **Programação Orientada a Objetos (POO)**

## Estrutura do Código

### Arquivos Principais:

- `main.py`: Contém o fluxo principal do programa, o menu de opções e a execução das operações bancárias.
- `models/cliente.py`: Define a classe `Cliente`, que armazena informações sobre os clientes, como nome, CPF, e data de nascimento.
- `models/conta.py`: Define a classe `Conta`, responsável pela manipulação das operações bancárias, como saque, depósito e transferência.
- `utils/helper.py`: Contém funções auxiliares para conversão de data e formatação de valores.
