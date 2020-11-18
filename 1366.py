#1366		Jogo de Varetas
variedade = int(input())

while variedade!=0:
  possibilidade = 0
  for i in range(variedade):
    c, q = map(int,input().split())
    possibilidade += (q//2)
  print(possibilidade//2)

  variedade = int(input())