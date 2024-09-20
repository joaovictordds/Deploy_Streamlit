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
    #st.subheader("Explorando o mundo dos dados")

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
	from abc import ABC, abstractmethod
	from datetime import datetime
	
	# Função de inicialização dos dados no session_state
	def inicializar_dados():
	    if 'clientes' not in st.session_state:
	        st.session_state['clientes'] = []
	    if 'contas' not in st.session_state:
	        st.session_state['contas'] = []
	    if 'menu' not in st.session_state:
	        st.session_state['menu'] = None
	
	# Função de boas-vindas
	def boas_vindas():
	    st.title("Bem-vindo ao Banco DIO")
	    st.image('dio.jpeg', use_column_width=True)
	    if st.button("Acessar o menu"):
	        st.session_state['menu'] = 'menu'
	
	# Função para exibir o menu
	def menu():
	    st.title("Menu")
	    escolha = st.selectbox(
	        "Escolha uma opção:",
	        ["Depositar", "Sacar", "Extrato", "Nova conta", "Listar contas", "Novo usuário", "Sair"]
	    )
	
	    if escolha == "Depositar":
	        depositar()
	    elif escolha == "Sacar":
	        sacar()
	    elif escolha == "Extrato":
	        exibir_extrato()
	    elif escolha == "Novo usuário":
	        criar_cliente()
	    elif escolha == "Nova conta":
	        criar_conta()
	    elif escolha == "Listar contas":
	        listar_contas()
	    elif escolha == "Sair":
	        st.write("Obrigado pela visita. Até a próxima!")
	        st.image('dio.jpeg', use_column_width=True)
	        st.session_state['menu'] = None  # Voltar à tela inicial de boas-vindas
	
	# Classe Cliente e suas derivadas
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
	
	# Classe Conta e suas derivadas
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
	            st.write("\n|==> Não há saldo suficiente em conta...")
	
	        elif valor > 0:
	            self._saldo -= valor
	            st.write("\n=== Saque realizado com sucesso! ===")
	            return True
	
	        else:
	            st.write("\n|==> O valor informado é inválido...")
	
	        return False
	
	    def depositar(self, valor):
	        if valor > 0:
	            self._saldo += valor
	            st.write("\n=== Depósito realizado com sucesso! ===")
	        else:
	            st.write("\n|==> O valor informado é inválido...")
	            return False
	
	        return True
	
	class ContaCorrente(Conta):
	    def __init__(self, numero, cliente, limite=500, limite_saques=3):
	        super().__init__(numero, cliente)
	        self._limite = limite
	        self._limite_saques = limite_saques
	
	    def sacar(self, valor):
	        numero_saques = sum(1 for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__)
	
	        excedeu_limite = valor > self._limite
	        excedeu_saques = numero_saques >= self._limite_saques
	
	        if excedeu_limite:
	            st.write("\n|==> O valor do saque excede o limite...")
	
	        elif excedeu_saques:
	            st.write("\n|==> Número máximo de saques excedido...")
	
	        else:
	            return super().sacar(valor)
	
	        return False
	
	    def __str__(self):
	        return f"""
	        Agência: {self.agencia}
	        C/C: {self.numero}
	        Titular: {self.cliente.nome}
	        """
	
	# Classe Historico e Transações
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
	
	# Funções do sistema bancário
	def filtrar_cliente(cpf, clientes):
	    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)
	
	def recuperar_conta_cliente(cliente):
	    if not cliente.contas:
	        st.write("\n |==> Cliente não possui conta!")
	        return None
	
	    if len(cliente.contas) == 1:
	        return cliente.contas[0]
	
	    escolha = st.selectbox("Escolha a conta", [f"Conta: {conta.numero}" for conta in cliente.contas])
	    return cliente.contas[int(escolha.split(":")[1].strip()) - 1]
	
	def realizar_transacao(cpf, clientes, transacao):
	    cliente = filtrar_cliente(cpf, clientes)
	    if not cliente:
	        st.write("\n |==> Cliente não encontrado!")
	        return
	
	    conta = recuperar_conta_cliente(cliente)
	    if not conta:
	        return
	
	    cliente.realizar_transacao(conta, transacao)
	
	def depositar():
	    cpf = st.text_input("Informe o CPF:")
	    valor = st.number_input("Informe o valor do depósito:", min_value=0.01)
	    if st.button("Confirmar Depósito"):
	        transacao = Deposito(valor)
	        realizar_transacao(cpf, st.session_state['clientes'], transacao)
	
	def sacar():
	    cpf = st.text_input("Informe o CPF:")
	    valor = st.number_input("Informe o valor do saque:", min_value=0.01)
	    if st.button("Confirmar Saque"):
	        transacao = Saque(valor)
	        realizar_transacao(cpf, st.session_state['clientes'], transacao)
	
	def exibir_extrato():
	    cpf = st.text_input("Informe o CPF:")
	    cliente = filtrar_cliente(cpf, st.session_state['clientes'])
	
	    if cliente:
	        conta = recuperar_conta_cliente(cliente)
	        if conta:
	            st.write("=== Extrato ===")
	            for transacao in conta.historico.transacoes:
	                st.write(f"{transacao['tipo']} em {transacao['data']} ---> R$ {transacao['valor']:.2f}")
	            st.write(f"Saldo: R$ {conta.saldo:.2f}")
	    else:
	        st.write("\n |==> Cliente não encontrado!")
	
	def criar_cliente():
	    cpf = st.text_input("Informe o CPF:")
	    nome = st.text_input("Informe o nome:")
	    data_nascimento = st.text_input("Informe a data de nascimento:")
	    endereco = st.text_input("Informe o endereço:")
	    
	    if st.button("Criar Cliente"):
	        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
	        st.session_state['clientes'].append(cliente)
	        st.write("\n=== Cliente criado com sucesso! ===")
	
	def criar_conta():
	    cpf = st.text_input("Informe o CPF do cliente:")
	    cliente = filtrar_cliente(cpf, st.session_state['clientes'])
	
	    if cliente:
	        numero_conta = len(st.session_state['contas']) + 1
	        conta = ContaCorrente.nova_conta(cliente, numero_conta)
	        st.session_state['contas'].append(conta)
	        cliente.adicionar_conta(conta)
	        st.write("\n=== Conta criada com sucesso! ===")
	    else:
	        st.write("\n |==> Cliente não encontrado!")
	
	def listar_contas():
	    for conta in st.session_state['contas']:
	        st.write(str(conta))
	
	# Função principal
	def main():
	    inicializar_dados()
	    
	    if st.session_state['menu'] is None:
	        boas_vindas()
	    else:
	        menu()
	
	if __name__ == "__main__":
	    main()


	
