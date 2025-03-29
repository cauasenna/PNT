rodadas = int(input())

win_sheldon = 0
win_raj = 0

for i in range (1,rodadas+1):
  escolha_sheldon1 = input()
  escolha_raj1 = input()
  if escolha_sheldon1 == "lagarto" and escolha_raj1 == "spock"\
  or escolha_sheldon1 == "spock" and escolha_raj1 == "tesoura"\
  or escolha_sheldon1 == "tesoura" and escolha_raj1 == "lagarto":
    win_sheldon += 1
    
  elif escolha_raj1 == "lagarto" and escolha_sheldon1 == "spock"\
  or escolha_raj1 == "spock" and escolha_sheldon1 == "tesoura"\
  or escolha_raj1 == "tesoura" and escolha_sheldon1 == "lagarto":
   win_raj += 1
   
  else:
    pass
  
if win_sheldon > win_raj:
  print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif win_raj > win_sheldon:
  print("ENGOLE ESSA, SHELDON!")
elif win_sheldon == win_raj:
  print("Oh não, precisamos de outra rodada.")
  