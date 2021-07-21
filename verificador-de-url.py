import requests

while True:
  sites=str(input("""Insira as URLs dos sites que deseja verificar o status, separadas por vírgula

  """)).lower().strip().replace(' ','')

  formatar_urls=sites.replace(',',' ')
  urls=formatar_urls.split()
  

  for url in urls:
    try:
      if 'http://' not in url:
        requisicao=requests.get('http://'+url)
      else:
        requisição=requests.get(url)
        
      if requisicao.status_code==200:
        print(f'O site {url} está online ')
    except:
      print(f'O site {url} não existe ou está fora do ar')
  
  
  pergunta=str(input('gostaria de continuar?[S/N]: ')).strip().upper()[0]
  
  if pergunta in 'N':
    break
  while pergunta not in 'S':
    pergunta=str(input('ERRO, digite S para continuar e N para encerrar: ')).strip().upper()[0]

print('Obrigado, tamo junto, tenha um excelente dia e volte sempre!')



