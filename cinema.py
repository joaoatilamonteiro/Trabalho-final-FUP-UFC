#fazer leitura de csvs avaliacoes e filmes para poder ser usada na tabela
import pandas as pad
import os


sequencias = []


avaliacoes = r"avaliacoes.csv"
filmes = "filmes.csv"

def mostra_menu(total):
  print("""
  ***Qual opção deseja escolher?***\n
  1 - cadastrar filme
  2 - Avaliar filme
  3 - Consultar Filme por Título
  4 - Listar Filmes por Gênero
  5 - Listar filmes por estrela
  6 - Listar todos os filmes
  7 - Sair""")


def carregar_filmes():
  filmes_carregados = pad.read_csv(filmes, sep = ",")
  #lista_colunas = filmes_carregados.columns.tolist()
  return filmes_carregados

def carregar_avaliacoes():
  avaliacoes_carregadas = pad.read_csv(avaliacoes, sep = ",")
  #media = (avaliacoes_carregadas.groupby("Título")["Estrelas"].mean().round(2))

def cadastrar_filme(filmes_carregados):  # Agora recebe o DataFrame corretamente

  print("""*********** SysFilmes ***********
  ******* Cadastrando Filme *******
  *********************************
  """)

  lista_colunas = ['Título', 'Ano', 'Gênero']

  novo_filme = {}
  for coluna in lista_colunas:
    valor_digitado = input(f"{coluna}: ").strip()
    if coluna == "Ano":
      novo_filme[coluna] = int(valor_digitado)
    else:
      novo_filme[coluna] = valor_digitado

  novo_filme['estrelas'] = 0.0
  novo_filme['numero_avaliacoes'] = 0
  filmes_add = pad.concat([filmes_carregados, pad.DataFrame([novo_filme])], ignore_index=True)
  filmes_add.to_csv("filmes.csv", sep=",", index=False)
  print("\nFilme cadastrado com sucesso!")
  print("\n[**Tecle enter para continuar**]")
  input()

opcao = -1
while True:

  mostra_menu(opcao)
  opcao = int(input('\n'))
  if opcao == 1:
    df_filmes = carregar_filmes()
    cadastrar_filme(df_filmes)
  if opcao == 7:
    break





