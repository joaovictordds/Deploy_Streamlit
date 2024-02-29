import streamlit as st
import pdfplumber as pdf
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --------------------------------------------------------------------------------------------------
# GUIA LATERAL

st.set_page_config(page_title = 'My Projects', layout = 'centered', initial_sidebar_state = 'auto')

st.sidebar.write('''
### My projects of Data Analysis, Data Science, Code and Others 
''')

st.sidebar.markdown('---')

paginas = ['Nuvem de Palavras']
pagina = st.sidebar.radio('Select one job:', paginas)

st.sidebar.markdown('---')

# --------------------------------------------------------------------------------------------------
# PROJETOS

if pagina == 'Nuvem de Palavras':

	nltk.download('stopwords')
	nltk.download('punkt')
	
	st.write('''

	### NUVEM DE PALAVRAS
		  
	''')	

	#st.image('contratado.jpg')
	
	st.write('''
	Crie uma nuvem de palavras a partir de um arquivo no formato pdf.

	##### COMO FUNCIONA?

	- Faça o upload do arquivo pdf.
	- Clique no botão 'GERAR NUVEM'
	
	''')	

	#st.image('thats-all.gif')
    
	uploaded_file = st.file_uploader("Somente arquivos de uma página, no formato PDF:", type=["pdf"])

	if st.button(label = '-> GERAR NUVEM <-', help = 'É só clicar ali'):

		cv = pdf.open(uploaded_file)
		pagina1 = cv.pages[0] # pagina 0 é a primeira
		texto = pagina1.extract_text()

		lista_de_palavras = nltk.tokenize.word_tokenize(texto) # coloca cada palavra em uma linha

		# Padronizando as palavras em lowercase (apenas letras minúsculas)
		lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras] #deixando tudo minusculo

		#Criando uma lista que contém pontuação que desejamos remover
		pontuacao = ['(', ')', ';', ':', '[', ']', ',', "'", '.', '-', '•']

		#Criando uma lista de stop words "a", "de", "um"que não tem valor como palavra
		stop_words = nltk.corpus.stopwords.words('portuguese')

		#criando uma lista de palavra sem stopword e pontuacoes
		keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]

		# concatenar as palavras
		textocv = " ".join(s for s in keywords)

		wordcloud = WordCloud(background_color = '#0f54c9', max_font_size = 150, width = 1280, height = 720, colormap= 'Blues').generate(textocv) 

		# mostrar a imagem final
		fig, ax = plt.subplots(figsize=(50, 20))
		ax.imshow(wordcloud)
		ax.set_axis_off()
		plt.imshow(wordcloud)
		wordcloud.to_file("wordcloud.png")
		st.image('wordcloud.png')



