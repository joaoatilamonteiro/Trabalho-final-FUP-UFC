def cria_filme():
  """
  Pede ao usuário as informações de um novo filme e retorna em um dicionário com os dados.

  Retorno:
  dict: Dicionário com os dados do filme (título, ano, gênero, estrelas e avaliações).
  """
  print("""*********** SysFilmes ***********
******* Cadastrando Filme *******
*********************************
""")
  filme = {}
  filme["Título"] = input("Título: ").strip()
  filme["Ano"] = int(input("Ano: ").strip())
  filme["Gênero"] = input("Gênero: ").strip()
  filme["Estrelas"] = 0.0
  filme["numero de avaliações"] = 0
  print("\n[**Tecle enter para voltar ao Menu Principal**]")
  input()
  return filme

def mostra_filme(filme):
  """
  Exibe os detalhes de um filme.

  Parâmetros:
  filme (dict): Dicionário contendo as informações de um filme.
  """
  print(f"Título: {filme['Título']}")
  print(f"Ano: {filme['Ano']}")
  print(f"Gênero: {filme['Gênero']}")
  print(f"Estrelas: {filme['Estrelas']}")
  print(f"Número de avaliações: {filme['Avaliações']}")
  print("\n*********************************")
def lista_todos(filmes):
  """
  Exibe a lista completa de todos os filmes cadastrados.

  Parâmetros:
  filmes (list): Lista contendo os filmes cadastrados.
  """
  print("""*********** SysFilmes ***********
*** Listando Filmes ***
*********************************""")

  if filmes:
      for filme in filmes:
          mostra_filme(filme)
  else:
      print("Nenhum filme cadastrado.")

  print("[**Tecle enter para voltar ao Menu Principal**]")
  input()

def lista_genero(genero, filmes):
  """
  Exibe os filmes do gênero definido pelo usuário.

  Parâmetros:
  genero (str): Gênero a ser buscado.
  filmes (list): Lista de filmes cadastrados.
  """
  print("""*********** SysFilmes ***********
      *** Listando Filmes por Gênero **
      *********************************""")
  encontrado = False

  for filme in filmes:
    if filme["Gênero"].lower() == genero.lower():
      mostra_filme(filme)
      encontrado = True

    if not encontrado:
      print("Nenhum filme encontrado com esse gênero.")

  print("[**Tecle enter para voltar ao Menu Principal**]")
  input()

def lista_estrelas(min_estrelas, filmes):
  """
  Exibe os filmes com estrelas maiores ou iguais ao valor informado.

  Parâmetros:
  min_estrelas (float): Valor mínimo de estrelas.
  filmes (list): Lista de filmes cadastrados.
  """
  print("""*********** SysFilmes ***********
  ** Listando Filmes por Estrelas *
 *********************************""")
  encontrado = False
  for filme in filmes:
    if filme["Estrelas"] >= min_estrelas:
      mostra_filme(filme)
      encontrado = True

    if not encontrado:
      print("Nenhum filme com essa quantidade de estrelas ou mais.")

    print("[**Tecle enter para voltar ao Menu Principal**]")
    input()