# Analise de Textos do Wikipedia
Script desenvolvido durante o processo seletivo para uma bolsa de iniciação cientifica do Instituto do Cérebro da UFRN. O script tem como objetivo acessar uma determinada lista do  wikipedia, acessar todos os links contidos nessa lista e trazer um compilado dos textos presentes em cada uma dessas páginas. Após isso, realizar tratamento dos dados e por fim, análise do que foi obtido.

## Bibliotecas Utilizadas:
  - [Selenium](https://pypi.org/project/selenium/)
  - [nltk](https://www.nltk.org/index.html)
  - [string](https://pypi.org/project/strings/)
  - [pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
  - [sklearn](https://scikit-learn.org/stable/user_guide.html)
  - [matplotlib](https://matplotlib.org)
  - [wordcloud](https://pypi.org/project/wordcloud/)

## Conteúdo:
  - ### [Notebook com os resultados obtidos pelo script](https://github.com/Raffae2679/analise_textos/blob/main/Resultados.ipynb)
  - ### [Script Analise_Textos](https://github.com/Raffae2679/analise_textos/blob/main/analise_texto.py)

## Enunciado da atividade:
O link a seguir é uma página da Wikipédia em português que mostra listas e subcategorias de
listas sobre diversos assuntos:

https://pt.wikipedia.org/wiki/Categoria:Listas

Escolha uma destas listas. Ela será válida se estiver contida no link acima, mesmo que de forma
recursiva através das subcategorias contidas no link. Pelo menos 50 itens da lista escolhida
precisam estar associados a uma página do Wikipédia que tenha conteúdo, formando assim, um
conjunto de pelo menos 50 páginas do Wikipédia. Caso a lista seja muito grande, pode-se
trabalhar com um subconjunto dessas páginas, usando qualquer critério para a seleção, desde
que o subconjunto possua pelo menos 50 páginas.

Para cada página, encontre um meio de carregar o texto da página, de modo que possa ser
analisado computacionalmente usando Python.

Combinando o texto de todas as páginas carregadas, descubra quais as 50 palavras que ocorrem
mais vezes. Você pode definir um conjunto de palavras a ser ignorado nessa contagem, de
acordo com critérios de sua escolha. Você também pode transformar palavras em outras,
seguindo um critério.

Sendo p o número de páginas carregadas, monte uma matriz com p linhas (uma para cada
página) e 50 colunas (uma para cada palavra). Os valores da matriz devem indicar a quantidade
de vezes que uma determinada palavra ocorre em uma determinada página.

Nessa matriz aplique uma PCA (Análise de Componentes Principais). Avalie os resultados da PCA
de modo a gerar 2 grupos de palavras. Gere gráficos para mostrar esses resultados. Interprete
os resultados de modo a tentar entender que conceitos distinguem os dois grupos de palavras.
Escreva uma conclusão que mostre como esses resultados ampliaram seu entendimento sobre
o assunto de que se trata a lista.


