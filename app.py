import streamlit as st
import pdfplumber as pdf
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import joblib


# -------------------------------------------------------------------------------------------------
# GUIA LATERAL

st.set_page_config(page_title = 'My Projects', layout = 'centered', initial_sidebar_state = 'auto')

st.sidebar.write('''
### Projetos de Data Analysis, Data Science, códigos e outros. 
''')

st.sidebar.markdown('---')

paginas = ['Inicio','Nuvem de Palavras','Modelo - Liberação de Crédito','Sistema Bancário DIO']
pagina = st.sidebar.radio('Selecione um projeto:', paginas)

st.sidebar.markdown('---')

#links importantes

st.sidebar.write('''
             
Acesse:\n
- [Portfolio](https://www.datascienceportfol.io/joaovictor)\n
- [GitHub](https://github.com/joaovictordds)\n
- [LinkedIn](https://linkedin.com/in/joaovictordds)\n            

''')

st.sidebar.markdown('---')

# --------------------------------------------------------------------------------------------------
# PROJETOS

if pagina == 'Inicio':
     
    # Título da página
    st.title("Bem-vindo!")

    # Cabeçalho
    st.subheader("Explorando o mundo dos dados")

    # Imagem
    st.image("da.png",  use_column_width=True)

    # Texto
    st.write(             
            '**Este é um blog pessoal dedicado à análise de dados, data science e data analytics onde você encontrará modelos de ML, projetos, análise de dados entre outros conteúdos.**\n'
            '- [Análise](https://medium.com/@joaovictordds/an%C3%A1lise-de-dados-do-banco-xyz-02eb55e8d7b9) do comportamento do banco XYZ e de seus clientes.\n'
            '- [Here](https://medium.com/@joaovictordds/data-analysis-of-xyz-bank-f9d6da27e0cc) the same analysis of the XYZ Bank in english.\n'
            '- Análise dos dados dos últimos balanços de [Petrobras](https://medium.com/@joaovictordds/an%C3%A1lise-explorat%C3%B3ria-de-petrobr%C3%A1s-utilizando-python-628f69ab5011)\n'     
            '- [Exploratory analysis](https://medium.com/@joaovictordds/exploratory-analysis-of-petrobras-with-python-a00de6496e36) of the numbers of the Petrobras company.\n'
            '- [Market place](https://medium.com/@joaovictordds/delivery-center-c4b8a66df76b) Delivery Center em português.\n'
            '- [Delivery Center](https://medium.com/@joaovictordds/delivery-center-84651776d1f1) analysis in english.\n'
            "- In [français](https://medium.com/@joaovictordds/delivery-center-4173b14b2518), analyse des données de l'entreprise Delivery Center."

            )
        
    


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

 
if pagina == 'Modelo - Liberação de Crédito':

    modelo = joblib.load('modeloclas.pkl')  
    subpag = ['Liberação de crédito'] #'Sugestão de quantia' 
    pag = st.sidebar.selectbox('Selecione o modelo:', subpag)
    st.image("credit.png",  use_column_width=True)
    st.write(' Uma fintech disponibilizou seus dados para análise da situação da companhia e para elaboração de um modelo para aprovar futuros empréstimos.')
    st.write('[Acesse](https://medium.com/@joaovictordds/german-bank-eda-ml-parte-2-3-7c499a59c664) a anáise dos dados da empresa')
	
    if pag == 'Liberação de crédito':
        
        st.title('Liberação de crédito')
        st.markdown('---')
        # Imagem
    	
     
      

    # INPUT DE VARIAVEIS

        saldocon = ['sem conta','negativo','positivo']
        cont = st.selectbox('Situação da conta', saldocon)

        #st.write('Quantidade de parcelas')
        dur = st.number_input('Qtde. Parcelas', 1, 120)

        #st.write('Histórico do cliente:')
        his = ['pagamento em dia','já atrasou pagamentos']
        histori = st.selectbox('Histórico do cliente', his) 

        #st.write('Valor em conta:')
        quant = st.number_input('Quantia solicitada', 1, 1000000)

        his = ['ate 1000','>1000','nao']
        poupan = st.selectbox('Saldo atual na instituição', his)

        empr = ['1-4 anos','> 7 anos','4-7 anos','desempregado']
        empreg = st.selectbox('Tempo de emprego', empr)
		
        #Novos dados
        duracao = dur
        quantia = quant
        conta = cont
        historico = histori
        poupança = poupan
        emprego = empreg

        # Dados
        tdados = {'conta': [conta],
                'historico': [historico],
                'poupança': [poupança],
                'emprego': [emprego],
                'duração': duracao,
                'quantia': quantia}

        # Criar DataFrame
        dtf = pd.DataFrame(tdados)
        

        
        st.markdown('---')
        
        if st.button('Executar modelo'):
            
            novos_dados = modelo.predict(dtf)
            saida = []
            
            if novos_dados == 0:
                saida = 'Não aprovar novo crédito'
                
            else :
                saida = 'Aprovar'
                
            st.subheader(saida)
        
        st.markdown('---')
        

if pagina == 'Sistema Bancário DIO':

	from PIL import Image
	# Carrega a imagem da pasta local
	image = Image.open("dio.jpeg")
	
	# Exibe a imagem no topo da página
	st.image(image, use_column_width=True)
	
	# Função para inicializar as variáveis de estado, garantindo que persistam entre interações
	def inicializa_estado():
	    if 'saldo' not in st.session_state:
	        st.session_state.saldo = 0
	    if 'limite' not in st.session_state:
	        st.session_state.limite = 500
	    if 'extrato' not in st.session_state:
	        st.session_state.extrato = ""
	    if 'numero_saques' not in st.session_state:
	        st.session_state.numero_saques = 0
	    if 'LIMITE_SAQUES' not in st.session_state:
	        st.session_state.LIMITE_SAQUES = 3
	
	# Chama a função para garantir que o estado esteja inicializado
	inicializa_estado()
	
	# Título e subtítulo
	st.title("Banco DIO")
	st.subheader("Bem-vindo novamente ao Banco DIO!")
	
	# Menu de opções com botões
	st.write("Selecione a opção desejada:")
	opcao = st.radio("", ["Extrato", "Depositar", "Sacar", "Sair"])
	
	# Opção de Depósito
	if opcao == "Depositar":
	    valor_deposito = st.number_input("Informe o valor do depósito:", min_value=0.0, step=0.01)
	    if st.button("Confirmar Depósito"):
	        if valor_deposito > 0:
	            st.session_state.saldo += valor_deposito
	            st.session_state.extrato += f"Depósito: + R$ {valor_deposito:.2f}\n"
	            st.success(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
	        else:
	            st.error("Operação falhou! O valor informado é inválido.")
	
	# Opção de Saque
	elif opcao == "Sacar":
	    valor_saque = st.number_input("Informe o valor do saque:", min_value=0.0, step=0.01)
	    if st.button("Confirmar Saque"):
	        excedeu_saldo = valor_saque > st.session_state.saldo
	        excedeu_limite = valor_saque > st.session_state.limite
	        excedeu_saques = st.session_state.numero_saques >= st.session_state.LIMITE_SAQUES
	
	        if excedeu_saldo:
	            st.error("Operação falhou! Você não tem saldo suficiente.")
	        elif excedeu_limite:
	            st.error("Operação falhou! O valor do saque excede o limite.")
	        elif excedeu_saques:
	            st.error("Operação falhou! Número máximo de saques excedido.")
	        elif valor_saque > 0:
	            st.session_state.saldo -= valor_saque
	            st.session_state.extrato += f"Saque: - R$ {valor_saque:.2f}\n"
	            st.session_state.numero_saques += 1
	            st.success(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
	        else:
	            st.error("Operação falhou! O valor informado é inválido.")
	
	# Opção de Extrato
	elif opcao == "Extrato":
	    st.write("\n================ EXTRATO ================")
	    if not st.session_state.extrato:
	        st.write("Não foram realizadas movimentações.")
	    else:
	        st.text(st.session_state.extrato)
	    st.write(f"\nSaldo: R$ {st.session_state.saldo:.2f}")
	    st.write("==========================================")
	
	# Opção de Sair
	elif opcao == "Sair":
	    st.write('Obrigado pela preferência!!!')


	
