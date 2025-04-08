# Repita os passos manuais usando codigo
from selenium import webdriver #selenium / webdriver to access the website 
from selenium.webdriver.common.by import By #selenium / webdriver to find the elements via XPATH 
import os # OS to help separating files per line
from time import sleep #time and sleep so the automation has enough time to run

# 1 - Entrar no site https://www.kabum.com.br/
url = input("Por favor, insira o link da página Kabum desejada: ")

print('Abrindo página e coletando as informações e criando arquivo csv')
driver = webdriver.Chrome()
driver.get(url) #'https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia'
print("Aguardando carregamento da página (10 segundos)...")
sleep(10)

# Scroll down to ensure all products load
print("Executando scroll para garantir carregamento dos produtos...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)

# 2 - Anotar o nome do primeiro produto (repetir) XPATH >> //tag[@atributo='valor']
produtos = driver.find_elements(By.XPATH, "//span[@height='54']")

# 3 - Anotar o preço do primeiro produto (repetir) XPATH >> //tag[@atributo='valor']
precos = driver.find_elements(By.XPATH, "//span[@class='sc-57f0fd6e-2 hjJfoh priceCard']")

# 4 - Guardar informações em arquivo de texto (csv)
for produto, preco in zip(produtos, precos):
    with open('preços_original.csv','a',encoding='utf-8') as arquivo:
        if arquivo.tell() == 0:
            arquivo.write('Produto,Preço\n')
        arquivo.write(f'{produto.text},{preco.text}{os.linesep}')

print(f'Total de produtos coletados: {len(produtos)}')

driver.quit()
