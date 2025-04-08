# Automação de Coleta de Preços - Kabum
Este projeto utiliza **Python** e **Selenium** para automatizar o processo de coleta de informações de produtos (nome e preço) em uma página do site [Kabum](https://www.kabum.com.br/). As informações coletadas são armazenadas em um arquivo CSV, facilitando a análise e comparação de preços, por exemplo, em momentos de promoções.

# Funcionalidades
Acessa a página Kabum especificada pelo usuário.

Realiza o carregamento completo da página via "scroll".

Coleta os nomes e preços dos produtos disponíveis.

Salva os dados coletados em um arquivo CSV para uso posterior.

## Pré-requisitos
Python 3.8+

Google Chrome instalado

ChromeDriver compatível com a versão do Google Chrome

Instalar dependências Python:

``bash
pip install selenium

# Como usar
Clone este repositório: 

``bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
Execute o script no terminal:

``bash
python nome_do_arquivo.py

Insira o link da página desejada no site Kabum quando solicitado.

O arquivo preços_original.csv será gerado com os dados coletados.
