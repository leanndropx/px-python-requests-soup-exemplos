import requests
from bs4 import BeautifulSoup

print('Bem-vindo ao Negociador de Moedas')

                        # 1 - RECEBE DADOS

#pegou a URL
url = "https://www.iban.com/currency-codes"
print()


#tentou fazer a requisição HTTP, se conseguir, salva o hmtl dentro de requisição
try:
  requisicao=requests.get(url)
  if requisicao.status_code==200:
    print(f'Acessamos o site {url}')
    print('Escola pelo número da lista o país que deseja consultar o código de moeda')

except:
  print(f'O site {url} não está acessando')



                        # 2 - MANIPULA DADOS

#salvou o texto do html em uma variável
html_texto = requisicao.text


#organizou o texto
soup=BeautifulSoup(html_texto, 'html.parser')


#encontrou todas as tags 'tr', colocou em uma lista e deletou a Head da tabela
paises=soup.find_all('tr')
del paises[0]


#criou um dicionario e uma lista pra usar no loop de filtro das informações de pais e codigo da moeda
pais_codigo={}
lista_paises=[]

#executou o loop, filtrou Pais e Codigo e adicionou no dicionario e na lista
for pais in paises:
  for key,value in enumerate(pais):
    
    if key==1:
      pais_codigo['pais']=value.get_text()
      
    if key==5:
      pais_codigo['codigo']=value.get_text()
      
  lista_paises.append(pais_codigo.copy())




                # 3 - RETORNA DADOS

#exibiu o menu de paises com index
for numero in range (0, len(lista_paises)):
  print(f'{numero} - {lista_paises[numero]["pais"]}')


                
#input
print()

try:
    while True:
        escolha = int(input('gostaria de ver o código de qual pais?: '))

        #if escolha>len(lista_paises)
        while escolha>len(lista_paises):
            escolha=int(input('Não existe, escolha uma opção de número na lista'))
          
        print(f'O código da moeda do país {lista_paises[escolha]["pais"]} é {lista_paises[escolha]["codigo"]}')
          
        deseja_continuar = str(input('gostaria de ver mais países?: ')).upper()[0]
          
        if deseja_continuar in "N":
            break


except:
    print('Isto não é um número')




    



  




