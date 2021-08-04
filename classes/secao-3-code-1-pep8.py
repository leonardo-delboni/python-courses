# PEP - Python Enhanced Proposal
# Propostas de Melhoria e Padronização da Linguagem Python

# PEP 8 -> Boas Práticas na codagem em Python
# A ideia da PEP 8 é a escrita de Python de forma visualmente agradável.

# [1] Utilize Camel Case para nomes de Classes
# NOMES DE CLASSES EM MAIÚSCULO E SEM HÍFENS!!!
# Ex: 
"""


class Calculadora
    pass


class CalculadoraCientifica
    pass


"""

# [2] FUNÇÕES ou VARIÁVEIS -> NOMES EM MINÚSCULO E COM UNDERLINE!!!
# Ex:

"""

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

"""

# [3] UTILIZE 4 ESPAÇOS PARA IDENTAÇÃO!!! CONFERIR ANTES DE USAR O TAB!!!

"""
if 'a' in 'banana':
    print('tem')

"""

# [4] SEPARAR FUNÇÕES E DEFINIÇÕES DE CLASSE COM DUAS LINHAS EM BRANCO!
#     MÉTODOS DENTRO DE CLASSE DEVEM SER SEPARADOS COM 1 ÚNICA LINHA EM BRANCO

"""


class Calculadora
    pass


class CalculadoraCientifica
    pass


"""

# [5] UM ÚNICO IMPORT POR LINHA!
"""
import sys
import os
"""

# OBSERVE QUE PODE SE UTILIZAR DESSA MANEIRA:

"""
from types import StringType, ListType
"""

# CASO SEJAM MUITOS IMPORTS DE UM MESMO PACOTE:
"""
from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)
"""
# [6] IMPORTS DEVEM SER COLOCADOS NO TOPO/INÍCIO DO PROGRAMA, LOGO APÓS OS COMENTÁRIOS OU DOCSTRINGS
#     E ANTES DE TODAS AS CONSTANTES E VARIÁVEIS GLOBAIS

# [7] A UTILIZAÇÃO DE ESPAÇOS DEVE SER CONFORME OS EXEMPLOS ABAIXO:
"""
funcao(algo[1], {outro: 2})
algo(1)
dict['chave'] = lista[indice]
"""

# [8] NÃO ALINHE VARIÁVEIS PELO SINAL DE ATRIBUIÇÃO!
"""
x = 1
y = 14
var_curta = 952
variavel_longa = 154232
"""

# [9] CONCLUIR SEMPRE COM UMA LINHA EM BRANCO!
# Easter Egg próprio do Python
import this
