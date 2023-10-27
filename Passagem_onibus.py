def venderPassagem (matriz):
  passagens = []
  idades = []
  continuar = 's'
  while continuar == 's':
    idade = int(input('Qual a sua idade? '))
    fileira = int(input('Qual fileira voce deseja se sentar? 1, 2 ou 3?')) -1
    assento = int (input('Qual assento voce deseja se sentar? 1 a 16?')) -1
    idades.append(idade)
    if matriz [fileira][assento] == '0':
      matriz[fileira][assento] = 'X'
    else:
      print('Assento ocupado. Tente novamente.')
    if idade > 0 and idade <= 12:
          if fileira == 1:
              passagem = 100
          elif fileira != 1:
            passagem = 150
    if idade >=13 and idade <=18:
          if fileira == 1:
            passagem = 200
          elif fileira != 1:
            passagem = 260
    if idade >=19:
          if fileira == 1:
            passagem = 300
          elif fileira !=1:
            passagem = 370
    passagens.append(passagem)
    continuar = input('Deseja continuar? s/n')


  return matriz, idades, passagens

def livresocup (matriz):
  contlivres = 0
  contocupados = 0
  for l in range (len(matriz)):
    for c in range (len(matriz[l])):
      if matriz[l][c] == '0':
        contlivres +=1
      else:
        contocupados +=1

  print("Assento livres >>", contlivres)
  print("Assentos ocupados>>", contocupados)

def faixaetaria (idades):
  soma = 0
  for i in idades:
    soma = soma + i

  return soma / len(idades)

def totalArrecadado (passagens):
  somavalor = 0
  for i in passagens:
    somavalor += i
  return somavalor


def maioridade(idades):
    maior = 0
    for i in range(len(idades)):
      if idades[i] > maior:
        maior = i
    return maior

def principal ():
  mat = [['0']*16 for i in range(3)]
  matr, l_idades, passa = venderPassagem(mat)
  livresocup(matr)
  totalA = totalArrecadado(passa)
  maior = maioridade(l_idades)
  media1 = faixaetaria(l_idades)
  print(f'A faixa etária média dos passageiros é: {media1}')
  print(f'O total arrecadado na viagem foi de:{totalA}')
  print(f'O passageiro mais velho no embarque tem {l_idades[maior]}')

principal()