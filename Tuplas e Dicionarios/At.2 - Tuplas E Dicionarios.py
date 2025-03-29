def verificar_lancamentos():
    # Entrada do número de pedras
    n = int(input())
    # Entrada das distâncias das pedras de Gohan
    gohan_distances = list(map(int, input().split()))
    # Entrada das distâncias das pedras de Piccolo
    piccolo_distances = list(map(int, input().split()))
    # Função para contar frequências utilizando dicionário
    def count_frequencies(distances):
        freq = {}
        for distance in distances:
            if distance in freq:
                freq[distance] += 1
            else:
                freq[distance] = 1
        return freq
    # Calculando as frequências para ambos
    gohan_freq = count_frequencies(gohan_distances)
    piccolo_freq = count_frequencies(piccolo_distances)
    # Comparando as frequências
    if gohan_freq == piccolo_freq:
        print("Dale Gohan!")
    else:
        print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")
# Executa a função principal renomeada
verificar_lancamentos()
