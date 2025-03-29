def adicionar_pokemon():  # Função para adicionar Pokémon à Pokédex
    nome_pokemon = comando[1]  # Extrai o nome do Pokémon
    if nome_pokemon in pokedex_dic:  # Verifica se o Pokémon já está na Pokédex
        print("Pokémon já adicionado na Pokédex")
    else:  # Caso não esteja, adiciona o Pokémon e sua descrição
        descricao = input().strip()  # Lê a descrição do Pokémon
        pokedex_dic[nome_pokemon] = descricao  # Atualiza o dicionário
        print("Pokémon adicionado com sucesso")

def descrever_pokemon():  # Função para mostrar descrição de Pokémon na Pokédex
    nome_pokemon = comando[1]  # Extrai o nome do Pokémon
    if nome_pokemon in pokedex_dic:  # Verifica se o Pokémon está na Pokédex
        print(pokedex_dic[nome_pokemon])
    else:  # Caso não esteja, mostra uma mensagem de erro
        print("Ainda não há registro desse Pokémon")

pokedex_dic = {}  # Dicionário para armazenar os Pokémon e suas descrições

while True:
    try:
        entrada = input().strip()  # Lê o comando e remove espaços extras
        if not entrada:  # Ignora entradas vazias
            continue
        
        comando = entrada.split(maxsplit=1)  # Divide a entrada em comando e nome do Pokémon
        if len(comando) < 2:  # Verifica se a entrada tem duas partes
            continue  # Ignora comandos inválidos sem exibir mensagem

        acao = comando[0].upper()  # Padroniza o comando para maiúsculas
        if acao == "ADD":  # Se o comando for 'ADD', chama a função de adicionar
            adicionar_pokemon()
        elif acao == "DESC":  # Se o comando for 'DESC', chama a função de descrever
            descrever_pokemon()
    except EOFError:  # Trata o fim das entradas
        break
