# Libs de web scrapping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Lib para realizar tokenize e importação das stopwords 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

# Lib string e realizando importações de pontuações (caracteres especiais)
from string import punctuation

# Lib para manipular dados
import pandas as pd

# Libs para realizar PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Lib para criação de gráficos
import matplotlib.pyplot as plt

# Lib para criação do WordCloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator





def pega_links():
	'''Função responsável por raspar os links da página do wikipedia'''

	lista_links = []
	
	url = "https://pt.wikipedia.org/wiki/Lista_de_dias_do_ano"
	option = Options()
	option.headless = True
	
	driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
	driver.get(url)
	
	# "Raspa" os links associados aos elementos que contem os meses na tabela da página do wikipedia
	for num in range(3,15):
		string = '//*[@id="collapsibleTable0"]/tbody/tr['+ str(num)+']/th/a'
		lista_links.append(driver.find_element_by_xpath(string).get_attribute('href'))
	
	# "Raspa" os links associados aos elementos que contem os dias dos meses na tabela da página do wikipedia
	for linha in range(3,15):
		for coluna in range(1,29):
			string = '//*[@id="collapsibleTable0"]/tbody/tr['+str(linha)+']/td/div/ul/li['+str(coluna)+']/a'
	
			lista_links.append(driver.find_element_by_xpath(string).get_attribute('href'))

	
	
	# Retorna uma lista de 51 posições
	return lista_links[:51]

def carrega_textos(link,texto):
	'''Função responsável por acessar o link, raspar o texto da página do wikipedia e concatenar com uma string'''

	paragrafo = ""
	option = Options()
	option.headless = True

	driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
	driver.get(link)

	# Após acessar o link que é passado, ele pega o texto contido na tag p , onde fica as informações da página.
	p = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/p')

	# Ele concatena os textos do paragrafo em uma unica váriavel
	for i in p:
		paragrafo = paragrafo+i.text+"\n"
	
	# E junta com o texto dos paragrafos com a variavel texto onde está o texto dos outros links
	texto = texto+paragrafo+"\n"

	# Por fim, retorna a variavel paragrafo com todo o texto da página e a variavel texto (junção desse e dos outros textos)
	return paragrafo, texto

def gera_texto(link):
	'''Função responsável por gerar a junção de todos os textos das páginas presentes na lista dos dias do wikipedia'''

	texto = ""

	# Carrega os links das páginas nessa lista
	l_links = link

	lista_texto = []

	# Percorre os links da lista, acessando e juntando todos os textos em um só lugar
	for i in range(0, len(l_links)):
		para, texto = carrega_textos(l_links[i], texto)
		# Adiciona o texto da página na mesma posição que a do link. Será usado na outra função para contar as palavras que aparecem. 
		lista_texto.append(para)

	# Retorna a lista com os textos de cada link e uma variavel com a junção de todos os textos.
	return lista_texto, texto

def palavras_repetem(texto, lista_texto):
	'''Função responsável por limpar o texto gerado pela função gera_texto e ver quais são as palavras que se repetem. Retornando um dicionario com as palavras e suas ocorrencias'''
	
	# Carrega as stopwords do idioma PT-BR, adiciono caracteres especiais, algumas outras stopwords e numeros.
	all_stopwords = stopwords.words('portuguese')
	all_stopwords += punctuation 
	all_stopwords += ['','``','a','em','o','e'] 
	all_stopwords += [str(i) for i in range(0,1000)]

	# Realizo word_tokenize, que é pegar um texto e dividi-lo por palavras. ex: Ola amigo, tudo bem? | = ['ola', 'amigo',',', 'tudo','bem']
	text_tokens = word_tokenize(texto)

	# Crio uma nova listagem  onde verifico se as palavras não estão contidas na listagem das stopwords.
	texto_sw = [word for word in text_tokens if not word in all_stopwords]

	# Realizo  word_tokenize com os textos que estão na lista de textos.
	for i in range(0,len(lista_texto)):
		text_lista = lista_texto[i]
		text_lista = word_tokenize(text_lista)
		lista_texto[i] = [word.lower() for word in text_lista if not word.lower() in all_stopwords]

	palavras = {}

	# Preenchendo o dicionario de acordo com as palavras e atualizando a quantidade de ocorrencias delas na lista que foi feito o word__tokenize
	for palavra in texto_sw:

		palavra = palavra.lower()

		if palavra in palavras:
			palavras[palavra] += 1

		else:
			palavras[palavra] = 1

	# Realiza ordenação dos elementos do dicionario levando em conta os itens(N° de ocorrencia das palavras), ex: palavras = {"Palavra":"N° Ocorrencia"}
	palavras_sort = sorted(palavras.items(), key = lambda x: x[1], reverse=True)

	
	# Mostra para o usuario quais foram as 50 palavras que mais se repetiram
	for i in palavras_sort:
		print("Palavra: {} | Ocorrencia: {}".format(i[0], i[1]))
	
	# Retorna a lista de textos que foi feito word_tokenize e a lista com as 50 palavras
	return lista_texto, palavras_sort[:51]

def conta_palavras(palavras, palavra):
	'''Função responsável por retornar o número de vezes que uma palavra se repete em um texto'''

	contador = 0
	for i in palavras:
		if i == palavra:
			contador +=1

	return contador

def nuvem_de_palavras(texto):
	'''Função responsável por criar a nuvem de palavras'''

	# Carrega as stopwords e adiciona outras palavras, simbolos e números para retirar
	all_stopwords = stopwords.words('portuguese')
	all_stopwords += punctuation 
	all_stopwords += ['','``','a','em','o','e'] 
	all_stopwords += [str(i) for i in range(0,1000)]

	# Criando a wordcloud
	wordcloud = WordCloud(stopwords=all_stopwords,
	                      background_color='black', width=1600,                            
	                      height=800).generate(texto)


	# Realizando a plotagem 
	fig, ax = plt.subplots(figsize=(16,8))            
	ax.imshow(wordcloud, interpolation='bilinear')       
	ax.set_axis_off()
	plt.imshow(wordcloud)
	plt.show()               
	
def analise_pca():
	'''Função responsável por realizar a criação do datafram e realizar a PCA'''

	lista_links = pega_links()

	lista_texto, texto = gera_texto(lista_links)

	nuvem_de_palavras(texto)

	lista_texto, list_words = palavras_repetem(texto, lista_texto)
	
	# Crio a lista com as colunas do dataframe, que é os links mais as palavras.
	colum = ["Links"]
	c = [item[0] for item in list_words]
	colum = colum + c


	# Criando data frame
	df = pd.DataFrame(columns = colum)


	# Preenche a coluna Links com os links das páginas do wikipedia
	for i in range(0, len(lista_links)):
		df.at[i, "Links"] = lista_links[i]


	# Percorro linha e coluna, verificando quantas vezes tal palavra se repetiu no texto do link, atualizando o valor no dataframe
	for i in range(0,len(lista_links)):
		for j in df.columns[1:]:
			
			num = conta_palavras(lista_texto[i], j)

			df.at[i,j] = num

	# Pego o nome das colunas começando depois da coluna "Links"
	features = [palavra for palavra in df.columns[1:]]

	x = df.loc[:, features].values

	y = df.loc[:, ['Links']].values

	x = StandardScaler().fit_transform(x)

	# Realizo PCA
	pca = PCA(n_components = 2)
	principalComponents = pca.fit_transform(x)

	principalDf = pd.DataFrame(data = principalComponents, columns = ['principal componente 1', 'principal componente 2'])

	# Concateno o dataframe resultante do PCA com a coluna dos "Links"
	finalDf = pd.concat([principalDf, df[['Links']]], axis=1)


	fig, ax = plt.subplots()
	ax.scatter(finalDf['principal componente 1'], finalDf['principal componente 2'])
	ax.grid()

	plt.title("Componentes - PCA")
	plt.xlabel("Componente Principal 1")
	plt.ylabel("Componente Principal 2")

	fig.tight_layout()
	plt.show()

	
	





	




# Executa a função que chama todas as outras para criar o dataframe e realiza o PCA. Além de criar o gráfico e a nuvem de palavras.
analise_pca()




