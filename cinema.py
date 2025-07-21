#fazer leitura de csvs avaliacoes e filmes para poder ser usada na tabela

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
  #nessa função os dados add aqui serao add nas suas respectivas tabelas de avaliacoes como filmes
  filme = {}
  filme["Título"] = input("titulo: ").strip()
  filme["Ano"] = int(input("ano: ").strip())
  filme["Gênero"] = input("genero: ").strip()
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
  #fazer um print que mostre as colunas da tabela filmes, sendo as colunas titulo ano e genero
  print(f"Título: {filme['titulo']}")
  print(f"Ano: {filme['ano']}")
  print(f"Gênero: {filme['genero']}")
  print(f"Estrelas: {filme['estrelas']}")
  print(f"Número de avaliações: {filme['avaliacoes']}")
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
  #ler a tabela filmes, especificamente coluna genero
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

    else:
      print("Nenhum filme encontrado com esse gênero.")

  print("[**Tecle enter para voltar ao Menu Principal**]")
  input()

def lista_estrelas(min_estrelas, filmes):
  """
  Exibe os filmes com estrelas maiores ou iguais ao valor informado.
#na tabela avaliações tem duas colunas filme e avaliação entao aqui usaria somente avaliação
#talvez colocar um sistema que mostra as estrelas sem ser em numero

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