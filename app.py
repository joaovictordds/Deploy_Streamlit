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

	
	from datetime import datetime
	from abc import ABC, abstractmethod
	from PIL import Image
		
	# Código
	class Cliente:
	    def __init__(self, endereco):
	        self.endereco = endereco
	        self.contas = []
	
	    def realizar_transacao(self, conta, transacao):
	        transacao.registrar(conta)
	
	    def adicionar_conta(self, conta):
	        self.contas.append(conta)
	
	
	class PessoaFisica(Cliente):
	    def __init__(self, nome, data_nascimento, cpf, endereco):
	        super().__init__(endereco)
	        self.nome = nome
	        self.data_nascimento = data_nascimento
	        self.cpf = cpf
	
	
	class Conta:
	    def __init__(self, numero, cliente):
	        self._saldo = 0
	        self._numero = numero
	        self._agencia = "0001"
	        self._cliente = cliente
	        self._historico = Historico()
	
	    @classmethod
	    def nova_conta(cls, cliente, numero):
	        return cls(numero, cliente)
	
	    @property
	    def saldo(self):
	        return self._saldo
	
	    @property
	    def numero(self):
	        return self._numero
	
	    @property
	    def agencia(self):
	        return self._agencia
	
	    @property
	    def cliente(self):
	        return self._cliente
	
	    @property
	    def historico(self):
	        return self._historico
	
	    def sacar(self, valor):
	        saldo = self.saldo
	        excedeu_saldo = valor > saldo
	
	        if excedeu_saldo:
	            st.error("Operação falhou! Você não tem saldo suficiente.")
	
	        elif valor > 0:
	            self._saldo -= valor
	            st.success("Saque realizado com sucesso!")
	            return True
	
	        else:
	            st.error("Operação falhou! O valor informado é inválido.")
	
	        return False
	
	    def depositar(self, valor):
	        if valor > 0:
	            self._saldo += valor
	            st.success("Depósito realizado com sucesso!")
	        else:
	            st.error("Operação falhou! O valor informado é inválido.")
	            return False
	
	        return True
	
	
	class ContaCorrente(Conta):
	    def __init__(self, numero, cliente, limite=500, limite_saques=3):
	        super().__init__(numero, cliente)
	        self._limite = limite
	        self._limite_saques = limite_saques
	
	    def sacar(self, valor):
	        numero_saques = len(
	            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
	        )
	
	        excedeu_limite = valor > self._limite
	        excedeu_saques = numero_saques >= self._limite_saques
	
	        if excedeu_limite:
	            st.error("Operação falhou! O valor do saque excede o limite.")
	
	        elif excedeu_saques:
	            st.error("Operação falhou! Número máximo de saques excedido.")
	
	        else:
	            return super().sacar(valor)
	
	        return False
	
	    def __str__(self):
	        return f"""\
	            Agência:\t{self.agencia}
	            C/C:\t\t{self.numero}
	            Titular:\t{self.cliente.nome}
	        """
	
	
	class Historico:
	    def __init__(self):
	        self._transacoes = []
	
	    @property
	    def transacoes(self):
	        return self._transacoes
	
	    def adicionar_transacao(self, transacao):
	        self._transacoes.append(
	            {
	                "tipo": transacao.__class__.__name__,
	                "valor": transacao.valor,
	                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
	            }
	        )
	
	
	class Transacao(ABC):
	    @property
	    @abstractmethod
	    def valor(self):
	        pass
	
	    @abstractmethod
	    def registrar(self, conta):
	        pass
	
	
	class Saque(Transacao):
	    def __init__(self, valor):
	        self._valor = valor
	
	    @property
	    def valor(self):
	        return self._valor
	
	    def registrar(self, conta):
	        sucesso_transacao = conta.sacar(self.valor)
	
	        if sucesso_transacao:
	            conta.historico.adicionar_transacao(self)
	
	
	class Deposito(Transacao):
	    def __init__(self, valor):
	        self._valor = valor
	
	    @property
	    def valor(self):
	        return self._valor
	
	    def registrar(self, conta):
	        sucesso_transacao = conta.depositar(self.valor)
	
	        if sucesso_transacao:
	            conta.historico.adicionar_transacao(self)
	
	
	# Streamlit App
	def main():
	    if 'clientes' not in st.session_state:
	        st.session_state.clientes = []
	    if 'contas' not in st.session_state:
	        st.session_state.contas = []
	
	    
	
	    menu = ['Inicio',"Depósito", "Saque", "Extrato", "Nova Conta", "Listar Contas", "Novo Usuário", "Sair"]
	
	    escolha = st.selectbox("Escolha uma opção", menu)
	
	    if escolha == 'Inicio':
	        print('')
	        st.subheader('Bem-vindo novamente ao Banco DIO')
	        st.write(' ')
	        st.write("Navegue pela barra acima para selecionar a opção desejada.")
	        st.image('dio.jpeg', use_column_width=True)
	    
	    if escolha == "Sair":
	        print('')
	        st.write("Obrigado pela visita. Até a próxima!")
	        print('')
	        st.image('dio.jpeg', use_column_width=True)
	        return
	
	    if escolha == "Depósito":
	        cpf = st.text_input("Informe o CPF do cliente", key="cpf_dep")
	        valor = st.number_input("Informe o valor do depósito", min_value=0.0, step=0.01, key="valor_dep")
	        if st.button("Realizar Depósito"):
	            cliente = next((c for c in st.session_state.clientes if c.cpf == cpf), None)
	            if cliente:
	                conta = next((c for c in cliente.contas), None)
	                if conta:
	                    transacao = Deposito(valor)
	                    cliente.realizar_transacao(conta, transacao)
	                else:
	                    st.error("Cliente não possui conta!")
	            else:
	                st.error("Cliente não encontrado!")
	
	    elif escolha == "Saque":
	        cpf = st.text_input("Informe o CPF do cliente", key="cpf_saq")
	        valor = st.number_input("Informe o valor do saque", min_value=0.0, step=0.01, key="valor_saq")
	        if st.button("Realizar Saque"):
	            cliente = next((c for c in st.session_state.clientes if c.cpf == cpf), None)
	            if cliente:
	                conta = next((c for c in cliente.contas), None)
	                if conta:
	                    transacao = Saque(valor)
	                    cliente.realizar_transacao(conta, transacao)
	                else:
	                    st.error("Cliente não possui conta!")
	            else:
	                st.error("Cliente não encontrado!")
	
	    elif escolha == "Extrato":
	        cpf = st.text_input("Informe o CPF do cliente", key="cpf_ext")
	        if st.button("Exibir Extrato"):
	            cliente = next((c for c in st.session_state.clientes if c.cpf == cpf), None)
	            if cliente:
	                conta = next((c for c in cliente.contas), None)
	                if conta:
	                    st.write("=== EXTRATO ===")
	                    for transacao in conta.historico.transacoes:
	                        st.write(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")
	                    st.write(f"Saldo: R$ {conta.saldo:.2f}")
	                else:
	                    st.error("Cliente não possui conta!")
	            else:
	                st.error("Cliente não encontrado!")
	
	    elif escolha == "Nova Conta":
	        cpf = st.text_input("Informe o CPF do cliente para nova conta", key="cpf_nc")
	        if st.button("Criar Nova Conta"):
	            cliente = next((c for c in st.session_state.clientes if c.cpf == cpf), None)
	            if cliente:
	                numero_conta = len(st.session_state.contas) + 1
	                conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
	                st.session_state.contas.append(conta)
	                cliente.contas.append(conta)
	                st.success("Conta criada com sucesso!")
	            else:
	                st.error("Cliente não encontrado!")
	
	    elif escolha == "Listar Contas":
	        st.write("=== CONTAS ===")
	        for conta in st.session_state.contas:
	            st.write(f"Agência: {conta.agencia}")
	            st.write(f"C/C: {conta.numero}")
	            st.write(f"Titular: {conta.cliente.nome}")
	            st.write("=" * 30)
	
	    elif escolha == "Novo Usuário":
	        cpf = st.text_input("Informe o CPF do novo cliente", key="cpf_nu")
	        nome = st.text_input("Informe o nome completo", key="nome_nu")
	        data_nascimento = st.text_input("Informe a data de nascimento (dd-mm-aaaa)", key="data_nasc_nu")
	        endereco = st.text_input("Informe o endereço", key="endereco_nu")
	        if st.button("Criar Novo Usuário"):
	            if not next((c for c in st.session_state.clientes if c.cpf == cpf), None):
	                cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
	                st.session_state.clientes.append(cliente)
	                st.success("Cliente criado com sucesso!")
	            else:
	                st.error("Já existe cliente com esse CPF!")
	
	if __name__ == "__main__":
	    main()


	
