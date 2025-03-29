def criarJogadores(*extras): 
    # Inicializa variáveis de validação
    posicaoValida = False
    nomeValido = False
    jogador = input()
    infoJogador = jogador.split("-")
    
    # Verifica se a entrada tem 3 partes: {jogador}-{posição}-{peso}
    if len(infoJogador) == 3:
        # Se a posição for 'reserva'
        if infoJogador[1] == 'reserva': 
            # Permite até 3 jogadores na posição 'reserva'
            if jogadoresPosicao.count('reserva') < 3: 
                jogadoresNome.append(infoJogador[0])
                jogadoresPosicao.append(infoJogador[1])
                jogadoresPeso.append(int(infoJogador[2]))  
            else:  # Exibe mensagem se o limite de reservas for atingido
                return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
        else: 
            # Valida posição e nome do jogador
            if infoJogador[1] in POSICOES and infoJogador[1] not in jogadoresPosicao: 
                posicaoValida = True
            if infoJogador[0] not in jogadoresNome: 
                nomeValido = True
            # Adiciona o jogador se os dados forem válidos
            if posicaoValida and nomeValido: 
                jogadoresNome.append(infoJogador[0])
                jogadoresPosicao.append(infoJogador[1])
                jogadoresPeso.append(int(infoJogador[2]))
            else: 
                return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    # Se o input for apenas o nome do jogador {jogador}
    elif len(infoJogador) == 1:
        # Permite até 3 reservas automaticamente
        if jogadoresPosicao.count('reserva') < 3:
            jogadoresNome.append(infoJogador[0])
            jogadoresPosicao.append('reserva')
            jogadoresPeso.append(3)
        else: 
            return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    else:  # Exibe mensagem para entradas inválidas
        return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    
    # Se houver argumentos adicionais, exibe mensagem confirmando o jogador
    if extras: 
        return print(f'Ele veste a camisa, é com garra, é com amor. {infoJogador[0]} representando como {jogadoresPosicao[-1]}.')

def convocarTime():
    # Exibe mensagem se não houver jogadores
    if not jogadoresNome: 
        return print("Não é possível, Arnaldo!")        
    # Exibe os jogadores adicionados
    for i in range(len(jogadoresNome)): 
        print(f"{jogadoresNome[i]}-{jogadoresPosicao[i]}")  
    return

def avaliarTime(*extras):
    # Calcula a pontuação total do time
    pontuacao = sum(jogadoresPeso)
    
    # Se a função for chamada com argumento adicional, retorna a pontuação
    if extras: 
        return pontuacao
    else: 
        # Avalia o time com base na pontuação
        if pontuacao < 25:
            print(f"A zaga tá batendo cabeça, o meio de campo tá perdido, sem criatividade. E o ataque? Isolado, sem receber uma bola decente! Assim não dá!. No máximo, o {time} é uns {pontuacao} na escala!")
        elif pontuacao >= 25 and pontuacao < 45:
            print(f"Esse time tem qualidade, tem talento, mas tá faltando encaixar o jogo! O {time}... é uns... {pontuacao} ali na escala.")
        elif pontuacao >= 45:
            print(f"O elenco é fortíssimo: tem goleiro experiente, zaga sólida, meio-campo técnico, e um ataque rápido e criativo. O {time} TÁ MUITO ACIMA: {pontuacao} PRA MAIS, PRA MAIS, NA ESCALA!")
        return

def estimarPartida():
    # Inicializa variável de vitória
    vitoria = False
    pontuacaoPartida = avaliarTime(1)
    timeAdversario = input()
    fator = input()
    nomeAdversario, dificuldade = timeAdversario.split("-")
    
    # Ajusta pontuação com base em fatores adicionais
    if fator != "A verdade é que a situação tá complicada... A favor desse time, não tem nada!":
        fatoresTime = fator.split(",")
        pontuacaoPartida += len(fatoresTime)
        
    # Ajusta pontuação com base no nome do adversário
    if "1" in nomeAdversario:
        pontuacaoPartida += 2
    elif "3" in nomeAdversario:
        pontuacaoPartida -= 2
    
    # Determina vitória com base na dificuldade do adversário
    if dificuldade == "fácil":
        if pontuacaoPartida >= 25:
            vitoria = True
    elif dificuldade == "normal":
        if pontuacaoPartida >= 35:
            vitoria = True
    elif dificuldade == "difícil":
        if pontuacaoPartida >= 45:
            vitoria = True
    
    # Exibe mensagem de vitória ou derrota
    if vitoria: 
        print(f'O apito final confirma a vitória! QUE ESPETÁCULO DO {time}. No fim, não teve como pro {nomeAdversario}! Isso é futebol, meus amigos!')
        return vitoria
    else: 
        return print(f"Que tristeza, amigo! O time lutou, mas não conseguiu segurar o resultado. A torcida do {time}, que esteve em peso, agora vai embora cabisbaixa, dando espaço pro avanço do {nomeAdversario}.")

# Variáveis e listas principais
NOMES = ["emerson.novaera", "erick.daselva", "valdelas", "marcella.linda123", "tamys.silva_br", "levi.ackerman", "mec.programadora", "alex_do_gerah"]
POSICOES = ["goleiro", "pivô", "fixo", "ala esquerdo", "ala direito"]
jogadoresNome, jogadoresPosicao, jogadoresPeso = [], [], []

usuario = input()

# Verifica se o usuário é válido
if usuario in NOMES: 
    pass
else: 
    print("Desse jeito, vai complicar, meu amigo! Usuário da comissão não encontrado.")
    quit()

time = input()
qtdJogadores = int(input())

# Adiciona jogadores se a quantidade for válida
if qtdJogadores <= 8: 
    for i in range(qtdJogadores):
        criarJogadores()
elif qtdJogadores == 0: 
    print("Não é possível, Arnaldo!")    
else: 
    pass

convocarTime()

# Loop principal para comandos do usuário
while True:
    acao = input()
    if acao == "Quero agradecer de coração a você que nos acompanhou!":
        break
    elif acao == "Olha só, amigo! Vamos pra mais da escalação do time:":
        criarJogadores(1)
    elif acao == "Olha o elenco ai, amigos da rede Porto!":
        convocarTime()
    elif acao == "Arnaldo, e o que eu posso dizer desse time?":
        avaliarTime()
    elif acao == "Vai rolar a bola! É emoção que não acaba mais, amigo! Haja coração! E aí, Arnaldo, me diz uma coisa: o que tem a favor desse time?":
        estimarPartida()
    else:
        print("COMANDO NÃO RECONHECIDO.")
