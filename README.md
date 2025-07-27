SysFilmes: Sistema de Gerenciamento e Avaliação de Filmes

1\. Visão Geral

O SysFilmes é um sistema de console interativo, desenvolvido em Python, projetado para o gerenciamento de uma coleção de filmes. A aplicação permite ao usuário cadastrar, consultar e avaliar filmes, além de oferecer funcionalidades para carregar e persistir dados a partir de arquivos no formato CSV.

O sistema foi estruturado de forma modular, com funções específicas para cada uma das suas responsabilidades, garantindo clareza e manutenibilidade do código.

2\. Funcionalidades

O menu principal oferece as seguintes operações:

1\. Cadastrar Filme: Adiciona um novo filme à coleção, solicitando título, ano de lançamento e gênero.

2\. Avaliar Filme: Permite ao usuário atribuir uma nota (de 1 a 5 estrelas) a um filme previamente cadastrado. O sistema calcula e atualiza a média de avaliações.

3\. Consultar Filme por Título: Realiza uma busca por um filme específico e exibe seus detalhes.

4\. Listar Filmes por Gênero: Exibe todos os filmes pertencentes a um gênero informado pelo usuário.

5\. Listar Filmes por Estrelas: Lista os filmes que possuem uma avaliação média igual ou superior à nota informada.

6\. Listar Todos os Filmes: Apresenta a lista completa de todos os filmes cadastrados no sistema.

7\. Carregar Filmes de Arquivo: Importa uma lista de filmes a partir de um arquivo filmes.csv.

8\. Carregar Avaliações de Arquivo: Importa e aplica avaliações a partir de um arquivo avaliacoes.csv.

9\. Sair do Sistema: Encerra a aplicação.

3\. Como Utilizar

Pré-requisitos

Python 3.x

Um terminal ou console que suporte a biblioteca IPython (para a função clear\_output). Se executado em um ambiente que não a possua, a funcionalidade de limpar a tela pode não ocorrer como esperado.

Execução

Salve o código em um arquivo com a extensão .py (ex: cinema.py).

Execute o arquivo através de um terminal que tenha o Python instalado:

python cinema.py





Navegue pelas opções do menu digitando o número correspondente e pressionando Enter.

4\. Estrutura de Dados

A principal estrutura de dados do sistema é uma lista de dicionários. Cada filme é representado por um dicionário Python com as seguintes chaves:

Título (str): O título do filme.

Ano (int): O ano de lançamento.

Gênero (str): O gênero principal do filme.

Estrelas (float): A média de estrelas calculada a partir das avaliações. Inicializada com 0.0.

Avaliações (int): O número total de avaliações recebidas. Inicializado com 0.

5\. Persistência de Dados

O sistema utiliza arquivos no formato CSV para carregar e salvar informações, garantindo que os dados não sejam perdidos ao encerrar a aplicação.

filmes.csv

Formato: Título,Ano,Gênero

Utilização: Usado para carregar a lista inicial de filmes e para salvar novos filmes cadastrados durante a execução.

avaliacoes.csv

Formato: Título,Estrelas

Utilização: Usado para carregar avaliações em lote. O sistema localiza o filme pelo título e atualiza sua média de estrelas e o contador de avaliações. As avaliações feitas durante a sessão também são salvas neste arquivo.



