#fazer leitura de csvs avaliacoes e filmes para poder ser usada na tabela
import pandas as pad
import os


sequencias = []


avaliacoes = r"avaliacoes.csv"
colunas_avaliacoes = ['Título', 'Estrelas', 'Número avaliações']
filmes = r"filmes.csv"
lista_colunas = ['Título', 'Ano', 'Gênero']

def mostra_menu(total):
  print("""
  ***Qual opção deseja escolher?***
  1 - cadastrar filme
  2 - Avaliar filme
  3 - Consultar Filme por Título
  4 - Listar Filmes por Gênero
  5 - Listar filmes por estrela
  6 - Listar todos os filmes
  7 - Sair""")


def carrega_arquivos(caminho, coluna_padrao):
  dataframe = pad.read_csv(caminho, sep = ",")
  print(f"arquivo {caminho} carregado")
  return dataframe

def cadastrar_filme(filmes_carregados, avaliacoes_carregadas):  # Agora recebe o DataFrame corretamente

  print("""*********** SysFilmes ***********
  ******* Cadastrando Filme *******
  *********************************
  """)

  novo_filme, novo_filme_estrela = {}, {}
  for coluna in lista_colunas:
    valor_digitado = input(f"{coluna}: ").strip()

    if coluna == "Ano":
      novo_filme[coluna] = int(valor_digitado)
    else:
      novo_filme[coluna] = valor_digitado


  novo_filme_estrela['Título'] = novo_filme.get("Título")
  novo_filme_estrela['Estrelas'] = 0.0
  novo_filme_estrela['Número avaliações'] = 0

  filmes_add = pad.concat([filmes_carregados, pad.DataFrame([novo_filme])], ignore_index=True)
  filmes_add.to_csv(filmes, sep=",", index=False)

  filmes_add_estrela = pad.concat([avaliacoes_carregadas, pad.DataFrame([novo_filme_estrela])], ignore_index=True)
  filmes_add_estrela.to_csv(avaliacoes, sep=",", index=False)


  print("\nFilme cadastrado com sucesso!")
  print("\n[**Tecle enter para continuar**]")
  input()


def avaliar_filme(filmes):
  pass

def lista_estrelas(num, filmes):
  #solicita número mínimo de estrelas
  #lista os filmes com as estrelas maior ou igual ao valor dado
  pass

def lista_todos(filmes):
  #mostra todos os filmes com suas respectivas informações
  pass

opcao = -1
while True:

  mostra_menu(opcao)
  opcao = int(input('Digite a opção: '))
  if opcao == 1:
    df_filmes = carrega_arquivos(filmes, lista_colunas)
    df_avaliacoes_atuais = carrega_arquivos(avaliacoes, colunas_avaliacoes)
    cadastrar_filme(df_filmes,df_avaliacoes_atuais)

  elif opcao == 2:
    pass

  elif opcao == 3:
    pass

  elif opcao == 4:
    pass

  elif opcao == 5:
    pass

  elif opcao == 6:
    pass
  elif opcao == 7:
    print("Encerrado o programa...")
    break





