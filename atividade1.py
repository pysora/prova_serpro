import csv

colunas = ['Nome', 'Sobrenome', 'Lotação', 'Email', 'Cargo', 'Tarefa']

arq_saida = "C:/teste/resultado/prova_modificada.csv"

def validar_email(email):
  if not email.endswith('@email.com') or email.count('@') !=1 :
    return False
  else:
    return True

with open('C:/teste/prova.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader, None)

  lotacao_contagem = {}
  linhas_validas = []
  
  for linha in reader:
      nome, sobrenome, lotacao, email, cargo, tarefa = linha
        
      if validar_email(email) == False:
        continue
    
      if cargo == 'Estagiaria':
        continue
  
      if tarefa == 'Não':
        continue
  
      lotacao_contagem[lotacao] = lotacao_contagem.get(lotacao, 0)+1
      linhas_validas.append(linha)

for lotacao, contagem in lotacao_contagem.items():
  print(f"Lotação {lotacao}: {contagem} pessoas")

with open(arq_saida, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')
  writer.writerow(colunas)
  writer.writerows(linhas_validas)
