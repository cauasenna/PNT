# Recebe o nome de quem está enviando a lista (Bonna ou João)
nome = input()

# Exibe a mensagem inicial com base em quem enviou a lista
if nome == "Bonna":
    print("Os filmes sugeridos por Bonna são:")
elif nome == "João":
    print("Os filmes sugeridos por João são:")

# Recebe a quantidade de filmes na lista
quantidade = int(input())

# Recebe a lista de filmes e notas
lista_filmes = [input() for _ in range(quantidade)]

# Convertendo os filmes e notas para uma lista de tuplas (filme, nota)
filmes = [(filme.split(" - ")[0], float(filme.split(" - ")[1])) for filme in lista_filmes]

# Implementando bubble sort diretamente no código para ordenar a lista de filmes em ordem decrescente
n = len(filmes)
for i in range(n):
    for j in range(0, n - i - 1):
        # Comparação dos valores para trocar, caso a nota do próximo seja maior
        if filmes[j][1] < filmes[j + 1][1]:
            filmes[j], filmes[j + 1] = filmes[j + 1], filmes[j]

# Exibindo a lista ordenada
for filme, nota in filmes:
    print(f"{filme} - {nota:.1f}")
