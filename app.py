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

	import streamlit as st
	import textwrap
	from PIL import Image
		
	# Carrega a imagem da pasta local
	image = Image.open("dio.jpeg")
		
	# Exibe a imagem no topo da página
	st.image(image, use_column_width=True)
	
	# Título e subtítulo
	st.title("Banco DIO")
	st.subheader("Bem-vindo novamente ao Banco DIO!")
	
	# Função para inicializar as variáveis de estado
	def inicializa_estado():
	    if 'saldo' not in st.session_state:
	        st.session_state.saldo = 0
	    if 'limite' not in st.session_state:
	        st.session_state.limite = 500
	    if 'extrato' not in st.session_state:
	        st.session_state.extrato = ""
	    if 'numero_saques' not in st.session_state:
	        st.session_state.numero_saques = 0
	    if 'usuarios' not in st.session_state:
	        st.session_state.usuarios = []
	    if 'contas' not in st.session_state:
	        st.session_state.contas = []
	    if 'LIMITE_SAQUES' not in st.session_state:
	        st.session_state.LIMITE_SAQUES = 3
	    if 'AGENCIA' not in st.session_state:
	        st.session_state.AGENCIA = '0001'
	    if 'novo_usuario' not in st.session_state:
	        st.session_state.novo_usuario = {'cpf': '', 'nome': '', 'data_nascimento': '', 'endereco': ''}
	    if 'nova_conta' not in st.session_state:
	        st.session_state.nova_conta = {'cpf': ''}
	
	# Função para exibir o menu de opções
	def menu():
	    return st.radio("Selecione a opção desejada:", ["Depositar", "Sacar", "Extrato", "Nova conta", "Listar contas", "Novo usuário", "Sair"])
	
	# Função para depositar
	def depositar(saldo, valor, extrato):
	    if valor > 0:
	        saldo += valor
	        extrato += f'Depósito:\tR$ {valor:.2f}\n'
	        st.success('Depósito realizado com sucesso!')
	    else:
	        st.error('A operação falhou, o valor informado é inválido.')
	    return saldo, extrato
	
	# Função para sacar
	def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
	    excedeu_saldo = valor > saldo
	    excedeu_limite = valor > limite
	    excedeu_saques = numero_saques >= limite_saques
	
	    if excedeu_saldo:
	        st.error('A operação falhou! Não há saldo suficiente.')
	    elif excedeu_limite:
	        st.error('A operação falhou! O valor do saque supera o limite.')
	    elif excedeu_saques:
	        st.error('A operação falhou! Número máximo de saques excedido.')
	    elif valor > 0:
	        saldo -= valor
	        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
	        numero_saques += 1
	        st.success('Saque realizado com sucesso!')
	    else:
	        st.error('A operação falhou. O valor informado é inválido.')
	    
	    return saldo, extrato
	
	# Função para exibir o extrato
	def exibir_extrato(saldo, extrato):
	    st.write('========== EXTRATO ==========')
	    if not extrato:
	        st.write('Não foram realizadas movimentações.')
	    else:
	        st.text(extrato)
	    st.write(f'Saldo:\t\tR$ {saldo:.2f}')
	    st.write('=============================')
	
	# Função para criar usuário
	def criar_usuario(usuarios):
	    cpf = st.text_input('Informe o CPF (apenas números):', value=st.session_state.novo_usuario['cpf'])
	    st.session_state.novo_usuario['cpf'] = cpf
	    
	    usuario_existente = filtrar_usuario(cpf, usuarios)
	    
	    if usuario_existente:
	        st.error('Já existe um usuário cadastrado com este CPF!')
	    else:
	        nome = st.text_input('Informe o nome completo:', value=st.session_state.novo_usuario['nome'])
	        st.session_state.novo_usuario['nome'] = nome
	        
	        data_nascimento = st.text_input('Informe a data de nascimento (dd-mm-aaaa):', value=st.session_state.novo_usuario['data_nascimento'])
	        st.session_state.novo_usuario['data_nascimento'] = data_nascimento
	        
	        endereco = st.text_input('Informe o endereço (logradouro - nro - bairro - cidade - estado/sigla):', value=st.session_state.novo_usuario['endereco'])
	        st.session_state.novo_usuario['endereco'] = endereco
	        
	        if st.button('Cadastrar usuário'):
	            usuarios.append({
	                'nome': nome,
	                'data_nascimento': data_nascimento,
	                'cpf': cpf,
	                'endereco': endereco
	            })
	            st.success('Usuário cadastrado com sucesso!')
	            st.session_state.novo_usuario = {'cpf': '', 'nome': '', 'data_nascimento': '', 'endereco': ''}
	
	# Função para filtrar usuário
	def filtrar_usuario(cpf, usuarios):
	    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
	    return usuarios_filtrados[0] if usuarios_filtrados else None
	
	# Função para criar conta
	def criar_conta(agencia, numero_conta, usuarios, contas):
	    cpf = st.text_input('Informe o CPF do usuário para criar a conta:', value=st.session_state.nova_conta['cpf'])
	    st.session_state.nova_conta['cpf'] = cpf
	
	    if cpf and st.button('Criar conta'):
	        usuario = filtrar_usuario(cpf, usuarios)
	        if usuario:
	            contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
	            st.success('Conta cadastrada com sucesso!')
	        else:
	            st.error('Usuário não encontrado.')
	
	# Função para listar contas
	def listar_contas(contas):
	    if not contas:
	        st.write('Nenhuma conta cadastrada.')
	    else:
	        for conta in contas:
	            linha = f'''\
	                Agência:\t{conta['agencia']}
	                C/C:\t\t{conta['numero_conta']}
	                Titular:\t{conta['usuario']['nome']}'''
	            st.write('=' * 40)
	            st.write(textwrap.dedent(linha))
	
	# Função principal
	def main():
	    inicializa_estado()
	
	    opcao = menu()
	
	    if opcao == "Depositar":
	        valor = st.number_input('Informe o valor do depósito R$: ', min_value=0.0, step=0.01)
	        if st.button('Confirmar Depósito'):
	            st.session_state.saldo, st.session_state.extrato = depositar(st.session_state.saldo, valor, st.session_state.extrato)
	
	    elif opcao == "Sacar":
	        valor = st.number_input('Informe o valor do saque R$: ', min_value=0.0, step=0.01)
	        if st.button('Confirmar Saque'):
	            st.session_state.saldo, st.session_state.extrato = sacar(
	                saldo=st.session_state.saldo,
	                valor=valor,
	                extrato=st.session_state.extrato,
	                limite=st.session_state.limite,
	                numero_saques=st.session_state.numero_saques,
	                limite_saques=st.session_state.LIMITE_SAQUES
	            )
	
	    elif opcao == "Extrato":
	        exibir_extrato(st.session_state.saldo, st.session_state.extrato)
	
	    elif opcao == "Novo usuário":
	        criar_usuario(st.session_state.usuarios)
	
	    elif opcao == "Nova conta":
	        numero_conta = len(st.session_state.contas) + 1
	        criar_conta(st.session_state.AGENCIA, numero_conta, st.session_state.usuarios, st.session_state.contas)
	
	    elif opcao == "Listar contas":
	        listar_contas(st.session_state.contas)
	
	    elif opcao == "Sair":
	        st.write("Obrigado por usar o Banco DIO!")
	
	if __name__ == '__main__':
	    main()
	


	
