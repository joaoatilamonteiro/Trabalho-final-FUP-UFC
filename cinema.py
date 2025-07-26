
from IPython.display import clear_output
filmes = []

def mostra_menu(total):
    """
    Mostra o menu principal do sistema SysFilmes.

    Argumentos:
    total (int): Número total de filmes cadastrados.

    Retorna:
    int: Opção digitada pelo usuário.
    """
    while True:
        clear_output()
        print("*********** SysFilmes ***********")
        print(f"******* Existem: {total} filmes *******")
        print("*********************************")
        print("1. Cadastrar Filme")
        print("2. Avaliar Filme")
        print("3. Consultar Filme por Título")
        print("4. Listar Filmes por Gênero")
        print("5. Listar Filmes por Estrelas")
        print("6. Listar Todos os Filmes")
        print("7. Carregar Filmes de Arquivo")
        print("8. Carregar Avaliações de Arquivo")
        print("9. Sair do Sistema")
        try:
            opcao = int(input("Digite a opção desejada: "))
            if 1 <= opcao <= 9:
                return opcao
            else:
                print("Opção inválida. Tecle enter para repetir!")
                input()
        except ValueError:
            print("Entrada inválida. Tecle enter para repetir!")
            input()

def cria_filme():
  """
  Pede ao usuário as informações de um novo filme e retorna em um dicionário com os dados.

  Retorno:
  dict: Dicionário com os dados do filme (título, ano, gênero, estrelas e avaliações).
  """
  clear_output()
  print("""*********** SysFilmes ***********
******* Cadastrando Filme *******
*********************************
""")
  filme = {}
  filme["Título"] = input("Título: ").strip()
  filme["Ano"] = int(input("Ano: ").strip())
  filme["Gênero"] = input("Gênero: ").strip()
  filme["Estrelas"] = 0.0
  filme["Avaliações"] = 0
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
  clear_output()
  print("""*********** SysFilmes ***********
******** Listando Filmes ********
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
  clear_output()
  print("""*********** SysFilmes ***********
      *** Listando Filmes por Gênero **
      *********************************""")
  encontrado = False

  for filme in filmes:
    if filme['Gênero'].lower() == genero.lower():
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
  clear_output()
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

def busca_titulo(titulo, filmes):
  """
  Procura um filme pelo título e retorna o dicionário do filme ou None.
  """
  for filme in filmes:
    if filme["Título"].lower() == titulo.lower():
      return filme
  return None

def consulta_titulo(filmes):
 """
 Consulta um filme pelo título e mostra suas informações.
 """
 clear_output()
 print("""*********** SysFilmes ***********
 *** Consulta Filmes por Título **
 *********************************""")
 titulo = input("Digite o título do filme desejado: ").strip()

 filme = busca_titulo(titulo, filmes)

 if filme:
  print()
  mostra_filme(filme)
 else:
  print("Filme não encontrado!")

 input("[**Tecle enter para voltar ao Menu Principal**]")

def avalia_filme(filmes):
  """
  Permite ao usuário avaliar um filme existente na lista de filmes.
  Atualiza as estrelas e o número de avaliações do filme.

  Argumentos:
   filmes(list): A lista de dicionários de filmes cadastrados.
  """
  clear_output()
  print("""*********** SysFilmes ***********
  ********* Avaliar Filme *********
  *********************************""")
  titulo = input("Digite o título do filme que deseja avaliar: ").strip()
  filme_achado = busca_titulo(titulo, filmes)

  while True:
    try:
      estrelas = float(input("Quantas estrelas você atribui a esse filme? (1 a 5)"))
      if 1 <= estrelas <= 5:
       break
      else:
       print("Número inválida. Por favor, digite um valor entre 1 e 5.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número para a nota.")

  avaliacoes_atuais = filme_achado["Avaliações"]
  estrelas_atuais = filme_achado["Estrelas"]

  if avaliacoes_atuais == 0:
    filme_achado["Estrelas"] = estrelas
  else:
    nova_soma_estrelas = (estrelas_atuais * avaliacoes_atuais) + estrelas
    filme_achado["Estrelas"] = nova_soma_estrelas / (avaliacoes_atuais + 1)

  filme_achado["Avaliações"] = avaliacoes_atuais + 1

  print(f"\nFilme '{filme_achado['Título']}' avaliado com sucesso!")
  input("[**Tecle enter para voltar ao Menu Principal**]")

def carrega_filmes(filmes):
  """
  Carrega filmes de um CSV no formato:
  Título,Ano,Gênero
  - Ignora o cabeçalho com readline()
  - Inicializa Estrelas=0.0 e Avaliações=0
  """
  clear_output()
  print("""*********** SysFilmes ***********
  ** Carregando Filmes do Arquivo *
  *********************************""")
  nome_arquivo = input("Digite o nome do arquivo: ").strip()

  total_lidas = total_carregados = total_ignorados = 0
  arquivo = None

  try:
    arquivo = open(nome_arquivo)
    arquivo.readline()
    for linha in arquivo:
      linha = linha.strip()
      if not linha:
        continue
      partes = linha.split(',')
      if len(partes) < 3:
        total_ignorados += 1
        continue

      total_lidas += 1
      titulo = partes[0].strip()
      ano_txt = partes[1].strip()
      genero = partes[2].strip()

      try:
        ano = int(ano_txt)
      except ValueError:
        total_ignorados += 1
        continue

      filme = {"Título": titulo,"Ano": ano,"Gênero": genero,"Estrelas": 0.0,"Avaliações": 0}

      filmes.append(filme)
      total_carregados += 1

    print(f"\nFilmes lidos: {total_lidas}")
    print(f"Filmes carregados: {total_carregados}")
    print(f"Filmes ignorados: {total_ignorados}")
    print("Filmes carregados com sucesso!")
    print("\n[**Tecle enter para voltar ao Menu Principal**]")
    input()

  except FileNotFoundError:
    print("Arquivo não encontrado. Tecle enter para voltar.")
    input()
  finally:
    if arquivo is not None:
      arquivo.close()

def carrega_avaliacoes(filmes):
   """
   Lê um arquivo CSV (Título, Estrelas) e atualiza
   a média de estrelas e o número de avaliações dos filmes.
   """
   clear_output()
   print("""*********** SysFilmes ***********
   *** Carregando Avaliações CSV ***
   *********************************""")
   nome_arquivo = input("Digite o nome do arquivo: ").strip()

   total_lidas = total_aplicadas = total_ignoradas = 0
   arquivo = None

   try:
     arquivo = open(nome_arquivo)
     arquivo.readline()
     for linha in arquivo:
        linha = linha.strip()
        if not linha:
          continue
        partes = linha.split(',')
        if len(partes) < 2:
          total_ignoradas += 1
          continue
        total_lidas += 1
        titulo_avaliado = partes[0].strip()
        estrelas_str = partes[1].strip().replace(',', '.')

        try:
          estrelas = float(estrelas_str)
        except ValueError:
          total_ignoradas += 1
          continue

        if not (0 <= estrelas <= 5):
          total_ignoradas += 1
          continue

        filme_achado = busca_titulo(titulo_avaliado, filmes)
        if filme_achado == None:
          total_ignoradas += 1
          continue

        numero_avaliacoes = filme_achado["Avaliações"]
        filme_achado["Estrelas"] = round((filme_achado["Estrelas"] * numero_avaliacoes + estrelas) / (numero_avaliacoes + 1),1)
        filme_achado["Avaliações"] = numero_avaliacoes + 1
        total_aplicadas += 1
     print(f"\nAvaliações lidas: {total_lidas}")
     print(f"Avaliações aplicadas: {total_aplicadas}")
     print(f"Avaliações ignoradas: {total_ignoradas}")
     print("Avaliações carregadas com sucesso!")
     print("\n[**Tecle enter para voltar ao Menu Principal**]")
     input()
   except FileNotFoundError:
     print("Arquivo não encontrado. Tecle enter para voltar.")
     input()
   finally:
     if arquivo is not None:
      arquivo.close()

def atualiza_filmes(filmes):
  """
  Atualiza o arquivo filmes.csv com os filmes cadastrados.
  """
  try:
    arquivo = open("filmes.csv", "w")  # 'w' sobrescreve
    arquivo.write("Título,Ano,Gênero\n")  # cabeçalho
    for filme in filmes:
      linha = f"{filme['Título']},{filme['Ano']},{filme['Gênero']}\n"
      arquivo.write(linha)
    arquivo.close()
  except Exception as erro:
    print(f"Erro ao atualizar filmes: {erro}")

def atualiza_avaliacoes(filmes):
  """
  Atualiza o arquivo avaliacoes.csv com as avaliações atuais.
  """
  try:
    arquivo = open("avaliacoes.csv", "w")  # 'w' sobrescreve
    arquivo.write("Título,Estrelas\n")  # cabeçalho
    for filme in filmes:
      if filme['Avaliações'] > 0:
        linha = f"{filme['Título']},{round(filme['Estrelas'], 1)}\n"
        arquivo.write(linha)
    arquivo.close()
  except Exception as erro:
    print(f"Erro ao atualizar avaliações: {erro}")

opcao = 0
while opcao != 9:
  opcao = mostra_menu(len(filmes))
  if opcao == 1:
    novo_filme = cria_filme()
    filmes.append(novo_filme)
    atualiza_filmes(filmes)
  elif opcao == 2:
    avalia_filme(filmes)
    atualiza_avaliacoes(filmes)
  elif opcao == 7:
    carrega_filmes(filmes)
  elif opcao == 8:
    carrega_avaliacoes(filmes)
  elif opcao == 3:
    consulta_titulo(filmes)
  elif opcao == 4:
    genero = input("Digite o gênero desejado:").strip()
    lista_genero(genero, filmes)
  elif opcao == 5:
    estrelas = float(input("Digite o número de estrelas desejado:"))
    lista_estrelas(estrelas, filmes)
  elif opcao == 6:
    lista_todos(filmes)
  elif opcao == 9:
    clear_output()
    print("[**Bye, você saiu do SysFilmes!**]")
    break
