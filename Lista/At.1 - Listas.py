suspeitos = input()
lista_suspeitos = suspeitos.split(",")
comandos = [
    "Não encontrei nada no primeiro suspeito",
    "Não encontrei nada no primeiro suspeito",
    "O último da lista está limpo",
    "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita",
    "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição: 1"
]

while True:
  if len(lista_suspeitos) == 1:
    print(f"Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!")
    break
  
  comando = input()

  if comando == "Não encontrei nada no primeiro suspeito":
    lista_suspeitos.pop(0)

  elif comando == "O último da lista está limpo":
    lista_suspeitos.pop(-1)

  elif comando == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita":
    meio = (len(lista_suspeitos)) // 2  # Correção para pegar o índice do meio
    lista_suspeitos.pop(meio)

  elif comando == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:":
    posicao = int(input())
    lista_suspeitos.pop(posicao)

  elif comando == "Acho que temos mais uma opção a ser analisada…":
    novo_suspeito = input()
    lista_suspeitos.append(novo_suspeito)

  else:
    print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")
