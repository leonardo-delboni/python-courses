# SEÇÃO 3 - CÓDIGO 3 - RECEBENDO DADOS DO USUÁRIO
# RECEBENDO DADOS DO USUÁRIO

# input() -> Todo dado recebido via input é do tipo String!!!

# Em Python, String é tudo que estiver entre:
# Aspas simples -> Ex: 'Angelina Jolie'
# Aspas duplas -> Ex: "Angelina Jolie"
# Aspas simples triplas -> Ex: '''Angelina Jolie'''
# Aspas duplas triplas -> Ex: """Angelina Jolie"""

# Cast é a conversão de um tipo de dado para outro, exemplo:
# int(idade) -> cast

# EXEMPLO DE PROGRAMA ANTIGO (VERSÃO PYTHON 2.0)

""""
# Entrada de Dados
print("Qual seu nome? ")
nome = input() # Input de Nome
print("Seja bem-vindo(a), senhor(a) %s" % nome)

print("Qual a sua idade? ")
idade = input() # Input de Idade
# Processamento

# Saída de Dados
print(" O(a) senhor(a) %s tem %s anos de idade" % (nome, idade))
"""

# EXEMPLO NA VERSÃO ATUAL DO PYTHON (3.0)

# Entrada de Dados

print('Olá. Qual o seu nome? ')
nome = input() # Input de entrada

print('Seja bem-vindo(a) senhor(a) {0}. Qual a sua idade?'.format(nome))
idade = input() # Input de idade

# Processamento

# Saída de dados
ano_nascimento = 2021 - int(idade)
print('O(A) senhor(a) {0} nasceu em {1} e tem {2} anos de idade'.format(nome, ano_nascimento, idade))
