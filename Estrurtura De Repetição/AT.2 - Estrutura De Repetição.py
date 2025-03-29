PB = 0
PR = 0
p_1 = None
reacao_1 = None
while p_1 !="Fim do Show!":
  p_1 = input()
  if p_1 == "Fim do Show!":
    break
  reacao_1 = input()
  if reacao_1 == "BAZINGA!":
    PB +=1
  else:
    PR += 1
if PB > (PB + PR)*60/100:
  print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
elif PR > (PB + PR)*60/100:
  print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
else:
  print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")

  