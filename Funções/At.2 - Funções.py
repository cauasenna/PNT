def verifica_parenteses(sentenca, contador=0):
    # Caso base: Se a string está vazia
    if not sentenca:
        return contador
    # Incrementa se o primeiro caractere for '('
    if sentenca[0] == '(':
        return verifica_parenteses(sentenca[1:], contador + 1)
    # Decrementa se o primeiro caractere for ')'
    elif sentenca[0] == ')':
        return verifica_parenteses(sentenca[1:], contador - 1)
    # Continua verificando se o caractere não é parêntese
    else:
        return verifica_parenteses(sentenca[1:], contador)

def processa_sentencas(sentencas):
    resultados = []
    for sentenca in sentencas:
        resultado = verifica_parenteses(sentenca)
        if resultado == 0:
            resultados.append("Essa sentença está com os parênteses balanceados, HOORAY!")
        elif resultado > 0:
            resultados.append("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
        else:
            resultados.append("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
    return resultados

# Entrada de dados
n = int(input())
sentencas = [input() for i in range(n)]

# Processamento e saída
resultados = processa_sentencas(sentencas)
for resultado in resultados:
    print(resultado)
