import ply.lex as lex
from ply import yacc
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog



#========================================================================================================================================================================
#                                                               Análise Léxica
#========================================================================================================================================================================
reserved = {
   'CASUS': 'CASUS',
   'ALITER': 'ALITER',
   'DUM': 'DUM',
   'TO': 'TO',
   'LEGERE': 'LEGERE',
   'SCRIBE': 'SCRIBE',
   'IN' : 'IN',
   'TRACTUS' : 'TRACTUS',
}

tokens = [
    'TOTUM',
    'BIP',
    'VERBUM',
    'INT',
    'DECIMALE',
    'VARIAVEL',
    'OPERADOR_SOMA',
    'OPERADOR_SUBTRACAO',
    'OPERADOR_MULTIPLICACAO',
    'OPERADOR_DIVISAO',
    'VIRGULA',
    'OPERADOR_ATRIBUICAO',
    'OPERADOR_MAIS_IGUAL',
    'OPERADOR_IGUAL',
    'OPERADOR_MENOR',
    'OPERADOR_MAIOR',
    'OPERADOR_MENOR_IGUAL',
    'OPERADOR_MAIOR_IGUAL',
    'PONTO_VIRGULA', 
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'ABRE_CHAVES',
    'FECHA_CHAVES',
] + list(reserved.values())  # Concatenando com as palavras reservadas para verificação


t_DUM = r'DUM'
t_CASUS = r'CASUS'
t_ALITER = r'ALITER'
t_TO = r'TO'
t_LEGERE = r'LEGERE'
t_SCRIBE = r'SCRIBE'

t_IN = r'IN'
t_TRACTUS = r'TRACTUS'

t_OPERADOR_SOMA = r'\+'
t_OPERADOR_SUBTRACAO = r'-'
t_OPERADOR_MULTIPLICACAO = r'\*'
t_OPERADOR_DIVISAO = r'/'

t_PONTO_VIRGULA = r'\;'
t_VIRGULA = r'\,'

t_OPERADOR_ATRIBUICAO = r'\='
t_OPERADOR_MAIS_IGUAL = r'\+\='
t_OPERADOR_IGUAL = r'\=\='
t_OPERADOR_MENOR = r'\<'
t_OPERADOR_MAIOR = r'\>'
t_OPERADOR_MENOR_IGUAL = r'\<\='
t_OPERADOR_MAIOR_IGUAL = r'\>\='

t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_ABRE_CHAVES = r'\{'
t_FECHA_CHAVES = r'\}'

t_ignore = ' \t'  



def t_VERBUM(t):
    r'("[^"]*")'
    return t

def t_BIP(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_TOTUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIAVEL(t):
    r'[a-z][a-z_0-9]*'
    return t

def t_INT(t):
    r'INT'
    return t

def t_DECIMALE(t):
    r'DECIMALE'
    return t

# Define uma regra para que seja possível rastrear o números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)


#========================================================================================================================================================================
#                                                               Análise Sintática
#========================================================================================================================================================================

# Análise Sintática

def p_declaracoes_single(p):
    '''
    declaracoes : declaracao
    '''

def p_declaracoes_mult(p):
    '''
    declaracoes :  declaracao bloco
                |  bloco
    '''

def p_bloco(p):
    '''
    bloco : ABRE_CHAVES declaracoes FECHA_CHAVES
          | ABRE_CHAVES declaracao bloco FECHA_CHAVES
          | ABRE_CHAVES impressao FECHA_CHAVES
          | ABRE_CHAVES escrita impressao FECHA_CHAVES
          | ABRE_CHAVES escrita escrita impressao FECHA_CHAVES
          | ABRE_CHAVES escrita escrita expr impressao FECHA_CHAVES
          | ABRE_CHAVES impressao param_cond PONTO_VIRGULA FECHA_CHAVES
          | ABRE_CHAVES param_cond PONTO_VIRGULA impressao FECHA_CHAVES
          | ABRE_CHAVES impressao expr FECHA_CHAVES
          
    '''

def p_declaracao_DUM(p):
    '''
    declaracao : DUM param_cond bloco
               | declaracao DUM param_cond bloco
    '''

def p_declaracao_TO(p):
    '''
    declaracao : TO VARIAVEL IN TRACTUS ABRE_PARENTESES TOTUM VIRGULA TOTUM FECHA_PARENTESES bloco
               | TO VARIAVEL IN TRACTUS ABRE_PARENTESES BIP VIRGULA BIP FECHA_PARENTESES bloco
    '''

def p_declaracao_atribuicaoValorVariavel(p):
    '''
    declaracao : VARIAVEL OPERADOR_ATRIBUICAO expr PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO VERBUM PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO TOTUM PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO TOTUM PONTO_VIRGULA VARIAVEL OPERADOR_ATRIBUICAO TOTUM PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO BIP PONTO_VIRGULA
            | VARIAVEL OPERADOR_ATRIBUICAO funcao PONTO_VIRGULA
            | param VARIAVEL OPERADOR_ATRIBUICAO TOTUM PONTO_VIRGULA
            | VARIAVEL OPERADOR_MAIS_IGUAL TOTUM
            | VARIAVEL OPERADOR_MAIS_IGUAL BIP
            | VARIAVEL OPERADOR_MAIS_IGUAL VARIAVEL
    '''

def p_declaracao_condicionais(p):
    '''
    declaracao : CASUS param_cond bloco
               | declaracao CASUS param_cond bloco
               | declaracao CASUS param_cond bloco senao
               | CASUS param_cond bloco senao
    '''

def p_declaracao_funcao_invocada(p):
    '''
    declaracao : funcao PONTO_VIRGULA
               | impressao
               | escrita
    '''

def p_declaracao_definir_funcao(p):
    '''
    declaracao : funcao ABRE_CHAVES declaracoes FECHA_CHAVES
    '''

def p_parametro_condicional(p):
    '''
    param_cond :  VARIAVEL OPERADOR_MENOR TOTUM
                | VARIAVEL OPERADOR_MENOR BIP
                | VARIAVEL OPERADOR_MENOR VARIAVEL
                | VARIAVEL OPERADOR_MAIOR TOTUM
                | VARIAVEL OPERADOR_MAIOR BIP
                | VARIAVEL OPERADOR_MAIOR VARIAVEL
                | VARIAVEL OPERADOR_MAIS_IGUAL TOTUM
                | VARIAVEL OPERADOR_MAIS_IGUAL BIP
                | VARIAVEL OPERADOR_MAIS_IGUAL VARIAVEL
                | VARIAVEL OPERADOR_IGUAL TOTUM
                | VARIAVEL OPERADOR_IGUAL BIP
                | VARIAVEL OPERADOR_IGUAL VARIAVEL
                | VARIAVEL OPERADOR_MAIOR_IGUAL TOTUM
                | VARIAVEL OPERADOR_MAIOR_IGUAL BIP
                | VARIAVEL OPERADOR_MAIOR_IGUAL VARIAVEL
                | VARIAVEL OPERADOR_MENOR_IGUAL TOTUM
                | VARIAVEL OPERADOR_MENOR_IGUAL BIP
                | VARIAVEL OPERADOR_MENOR_IGUAL VARIAVEL

    '''

def p_impressao(p):
    '''impressao : LEGERE expr PONTO_VIRGULA
                 | LEGERE expr ABRE_PARENTESES VERBUM VIRGULA VARIAVEL FECHA_PARENTESES PONTO_VIRGULA
                 | LEGERE ABRE_PARENTESES VERBUM FECHA_PARENTESES PONTO_VIRGULA
                 | LEGERE ABRE_PARENTESES  VERBUM VIRGULA VARIAVEL FECHA_PARENTESES PONTO_VIRGULA
    '''

def p_escrita(p):
    '''escrita : VARIAVEL OPERADOR_ATRIBUICAO SCRIBE ABRE_PARENTESES expr FECHA_PARENTESES PONTO_VIRGULA
               | VARIAVEL OPERADOR_ATRIBUICAO param ABRE_PARENTESES SCRIBE ABRE_PARENTESES VERBUM FECHA_PARENTESES FECHA_PARENTESES PONTO_VIRGULA
               | VARIAVEL OPERADOR_ATRIBUICAO SCRIBE ABRE_PARENTESES VERBUM FECHA_PARENTESES PONTO_VIRGULA 
               | VARIAVEL OPERADOR_ATRIBUICAO SCRIBE ABRE_PARENTESES VERBUM VARIAVEL FECHA_PARENTESES PONTO_VIRGULA 
    '''


def p_expressao_variavel(p):
    '''
    expr :  VARIAVEL PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_SOMA TOTUM PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_SOMA VARIAVEL PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_SUBTRACAO TOTUM PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_SUBTRACAO VARIAVEL PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_MULTIPLICACAO TOTUM PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_MULTIPLICACAO VARIAVEL PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_DIVISAO TOTUM PONTO_VIRGULA
         |  VARIAVEL OPERADOR_ATRIBUICAO VARIAVEL OPERADOR_DIVISAO VARIAVEL PONTO_VIRGULA

    '''


def p_expressao_operacao(p):
    '''
    expr : expr OPERADOR_SOMA expr
        |  expr OPERADOR_SUBTRACAO expr
        |  expr OPERADOR_MULTIPLICACAO expr
        |  expr OPERADOR_DIVISAO expr
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''


def p_parametro(p):
    '''
    param : TOTUM
        | INT
        | DECIMALE
        | BIP
        | VERBUM
        | VARIAVEL
    '''

def p_regra_funcao(p):
    '''
    funcao :  ABRE_PARENTESES param_vazio FECHA_PARENTESES
        |  ABRE_PARENTESES param FECHA_PARENTESES
    '''

def p_senao_se(p):
    '''
    senao : ALITER bloco
    '''

# Define a precedência e associação dos operadores matemáticos
precedence = (
    ('left', 'OPERADOR_SOMA', 'OPERADOR_SUBTRACAO'),
    ('left', 'OPERADOR_MULTIPLICACAO', 'OPERADOR_DIVISAO'),
)

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    if p:
        print("ERRO SINTÁTICO: ", p)
    else:
        print("ERRO SINTÁTICO: erro de sintaxe desconhecido")

parser = yacc.yacc()

erros = 0

# função padrão para adicionar as classificações dos tokens para ser impressa pelo compilador
def add_lista_saida(t, notificacao):
    saidas.append(( t.type, t.value, notificacao))

saidas = []


root = tk.Tk()  # cria a janela



#========================================================================================================================================================================
#                                                               Interface Transpilador
#========================================================================================================================================================================

class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        root.mainloop()

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, tk.END)
        for i in self.saida.get_children():
            self.saida.delete(i)
        saidas.clear()
        erroslexicos.clear()
        errossintaticos.clear()
        global erros
        erros = 0
        self.frame_1.update()
        self.frame_2.update()
        self.frame_3.update()
        root.update()

    def tela(self):
        self.root.title("Transpilador Latinus")
        self.root.configure(background="#282a36")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):
        # Label Código Fonte
        self.lb_codigo = tk.Label(
            text="Código Fonte", 
            bg="#282a36", 
            fg="#f8f8f2", 
            font=('Arial', 12, 'bold')
        )
        self.lb_codigo.place(relx=0.001, rely=0.02, relwidth=0.2, relheight=0.05)

        # Frame Código Fonte
        self.frame_1 = tk.Frame(
            self.root, 
            bd=4, 
            bg="#44475a", 
            highlightbackground="#6272a4", 
            highlightthickness=3
        )
        self.frame_1.place(relx=0.02, rely=0.07, relwidth=0.46, relheight=0.55)

        # Campo para inserir o Código Fonte
        self.codigo_fonte_entry = tk.Text(
            self.frame_1, 
            bg="#ffffff",  
            fg="#f8f8f2",  
            insertbackground="#f8f8f2",  
            font=('Arial', 12, 'bold')  
        )
        self.codigo_fonte_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)


        # Frame Código Python
        self.frame_3 = tk.Frame(
            self.root, 
            bd=4,  
            bg="#44475a", 
            highlightbackground="#6272a4", 
            highlightthickness=3
        )
        self.frame_3.place(relx=0.52, rely=0.07, relwidth=0.46, relheight=0.55)

        # Label Código Python
        self.lb_codigo_python = tk.Label(
            text="Código Python", 
            bg="#282a36", 
            fg="#f8f8f2", 
            font=('Arial', 12, 'bold')
        )
        self.lb_codigo_python.place(relx=0.51, rely=0.02, relwidth=0.2, relheight=0.05)

        # Código Python Entry
        self.codigo_python_entry = tk.Text(
            self.frame_3,
            bg="#ffffff", 
            fg="#44475a", 
            insertbackground="#f8f8f2", 
            font=('Courier', 10)
        )
        self.codigo_python_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        # Label Análise Léxica e Sintática
        self.lb_analise = tk.Label(
            text="Análise Léxica e Sintática", 
            bg="#282a36", 
            fg="#f8f8f2", 
            font=('Arial', 12, 'bold')
        )
        self.lb_analise.place(relx=0.05, rely=0.63, relwidth=0.3, relheight=0.05)

        # Frame do Analisador Léxico e Sintático
        self.frame_2 = tk.Frame(
            self.root, 
            bd=4, 
            bg="#44475a", 
            highlightbackground="#6272a4", 
            highlightthickness=3
        )
        self.frame_2.place(relx=0.02, rely=0.70, relwidth=0.96, relheight=0.20)


    def analisador(self):
        columns = ('token', 'lexema', 'notificacao')
        self.saida = ttk.Treeview(self.frame_2, height=5, columns=columns, show='headings')
        self.saida.heading("token", text='Token')
        self.saida.heading("lexema", text='Lexema')
        self.saida.heading("notificacao", text='Notificacao')

        # Adicionar barra de rolagem vertical
        scrollbar = ttk.Scrollbar(self.frame_2, orient='vertical', command=self.saida.yview)
        scrollbar.place(relx=0.975, rely=0, relheight=0.96)
        self.saida.configure(yscrollcommand=scrollbar.set)

        data = self.codigo_entry.get(1.0, "end-1c")
        lexer = lex.lex()
        lexer.input(data)

        print("Análise Léxica:")
        # Tokenizar a entrada para passar para o analisador léxico
        for tok in lexer:
            print("Token:", tok.type)
            print("Valor:", tok.value)
            global erros
            if tok.type == "TOTUM":
                max = (len(str(tok.value)))
                if max > 15:
                    erros += 1
                    add_lista_saida(tok, f"entrada maior que a suportada")
                else:
                    add_lista_saida(tok, f" ")
            elif tok.type == "CASUS" or tok.type == "ALITER" or tok.type == "DUM" or tok.type == "TO" or tok.type == "LEGERE" or tok.type == "IN" or tok.type == "TRACTUS" or tok.type == "SCRIBE":
                max = len(tok.value)
                if max < 20:
                    if tok.value in reserved:
                        tok.type = reserved[tok.value]
                        add_lista_saida(tok, f"palavra reservada")
                    else:
                        add_lista_saida(tok, f" ")
            else:
                add_lista_saida(tok, f" ")

        for tok in erroslexicos:
            add_lista_saida(tok, f"Caracter Inválido na linguagem")

        tamerroslex = len(erroslexicos)
        if tamerroslex == 0 and erros == 0:
            self.saida.insert('', tk.END, values="Análise Léxica Concluída sem Erros")
            parser.parse(data)
            tamerrosin = len(errossintaticos)
            if tamerrosin == 0:
                self.saida.insert('', tk.END, values="Análise Sintática Concluída sem Erros")
            else:
                self.saida.insert('', tk.END, values="Erro Sintático")
        else:
            self.saida.insert('', tk.END, values="Erro Léxico")

        for retorno in saidas:
            self.saida.insert('', tk.END, values=retorno)

        self.saida.place(relx=0.001, rely=0.01, relwidth=0.97, relheight=0.95)

    def transpilar_codigo(self):
        # Obtém o código-fonte do widget de entrada
        codigo_fonte = self.codigo_entry.get(1.0, tk.END)

        # Verifica se há erros léxicos ou sintáticos antes de transpilar
        if not erroslexicos and not errossintaticos:
            # Se não houver erros, transpila o código
            codigo_transpilado = self.gerar_python(codigo_fonte)
            self.exibir_codigo_python(codigo_transpilado)
        else:
            # Se houver erros, mostra uma mensagem ao usuário 
            messagebox.showerror("Erro", "Existem erros léxicos ou sintáticos no código. Corrija-os antes de transpilar.")

    def gerar_python(self, codigo_fonte):
        # Remover o ponto e vírgula no final da linha e espaços em branco subsequentes
        codigo_fonte = codigo_fonte.replace(';', '').rstrip()

        # Substituir TO por for
        codigo_fonte = codigo_fonte.replace('TO', 'for')

        codigo_fonte = codigo_fonte.replace('ALITER', 'else')

        # Substituir SCRIBE por input
        codigo_fonte = codigo_fonte.replace('SCRIBE', 'input')

        # Substituir CASUS por if e ALITER por else
        codigo_fonte = codigo_fonte.replace('CASUS', 'if')

        # Substituir LEGERE por print
        codigo_fonte = codigo_fonte.replace('LEGERE', 'print')

        # Substituir chaves por indentação
        codigo_fonte = codigo_fonte.replace('{', '').replace('}', '')

        # Remover ':' após a linha 'x = 11'
        codigo_fonte = codigo_fonte.replace('x = 11\n:', 'x = 11\n')

        # Substituir acentos
        codigo_fonte = codigo_fonte.replace('eh', 'é')

        # Corrigir formatação da VERBUM dentro da função LEGERE
        in_verbum = False
        temp = ''
        word = ''
        for char in codigo_fonte:
            if char == '"':
                in_verbum = not in_verbum
            if not in_verbum:
                if char.isalpha():
                    word += char
                else:
                    if word == 'TRACTUS':
                        temp += 'range'
                    elif word == 'IN':
                        temp += 'in'
                    elif word == 'INT':
                        temp += 'int'
                    elif word == 'DECIMALE':
                        temp += 'float'
                    else:
                        temp += word
                    word = ''
                    temp += char
            else:
                temp += char
        codigo_fonte = temp

        # transpilar a estrutura DUM
        codigo_fonte = codigo_fonte.replace('DUM', 'while')

        # Transpilar atribuição de valor a uma variável
        codigo_fonte = codigo_fonte.replace('OPERADOR_ATRIBUICAO', '=')

        # Corrigir indentação
        linhas = codigo_fonte.split('\n')
        for i in range(len(linhas)):
            linha = linhas[i].strip()
            if linha.startswith(('if', 'else', 'while', 'for')):
                # Adicionar ':' se ainda não estiver presente
                if not linha.endswith(':'):
                    linhas[i] = linha + ':'
            # Corrigir indentação do bloco else
            elif linha.startswith('else'):
                if i > 0 and linhas[i-1].strip().endswith(':'):
                    linhas[i] = ' ' + linha
                else:
                    if i+1 < len(linhas) and not linhas[i+1].strip().startswith('print'):
                        linhas[i+1] = '    ' + linhas[i+1]
                        linhas[i] = ' ' + linha

        codigo_fonte = '\n'.join(linhas)

        return codigo_fonte

    
    
    def exibir_codigo_python(self, codigo_transpilado):
        # Limpar a área de visualização do código Python
        self.codigo_python_entry.delete(1.0, tk.END)
        # Exibir o código Python transpilado na área de visualização
        self.codigo_python_entry.insert(tk.END, codigo_transpilado)

    def botoes(self):
        # botao limpar
        self.bt_limpar = tk.Button(text="Limpar", bd=2, bg="#FF6347", font=('', 11), command=self.limpa_telaentrada)
        self.bt_limpar.place(relx=0.74, rely=0.92, relwidth=0.1, relheight=0.05)

        self.bt_transpilar = tk.Button(text="Transpile", bd=2, bg="#87CEEB", font=('', 11),
                                       command=lambda: [self.analisador(), self.transpilar_codigo()])
        self.bt_transpilar.place(relx=0.63, rely=0.92, relwidth=0.1, relheight=0.05)

        self.codigo_entry = tk.Text(self.frame_1)
        self.codigo_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_1, orient='vertical', command=self.codigo_entry.yview)
        self.scroll_bar.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar


app = App()