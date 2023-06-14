import tkinter as tk

# cores
cor1 = '#3b3b3b'  # preto
cor2 = '#feffff'  # branco
cor3 = '#38576b'  # azul
cor4 = '#ECEFF1'  # cinza
cor5 = '#FFAB40'  # laranja

# criar tela da Calculadora
janela = tk.Tk()
# edita o titulo da janela
janela.title('Calculadora')
# definindo o tamanho da tela
janela.config(bg=cor1)

# ajustar linhas e colunas automaticamente a tela
janela.rowconfigure([0, 1], weight=1)
janela.columnconfigure([0, 1, 2, 3], weight=1)

# bloquear redimensionamento janela
# janela. resizable(width=False, height=False)


# funções
def pegar_numeros(botao):
    pega_numero = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(pega_numero) + str(botao))
    return


def limpa_campo():
    display.delete(0, tk.END)
    label_resultado['text'] = ''
    return


def calcular(*args):
    expressao = display.get()
    resultado = eval(expressao)
    label_resultado['text'] = resultado
    return


# label resultado
label_resultado = tk.Label(text='', height=2,
                           font='Ivy 20', anchor='e', justify='right', bg=cor3, fg=cor2)
label_resultado.grid(row=0, column=0, columnspan=4, sticky='nsew')
# entrada dados
display = tk.Entry(janela, font='Ivy 18')
display.grid(row=1, column=0, columnspan=4, sticky='nsew')

# criando botões
b1 = tk.Button(text='C', width=11, height=3, bg=cor4, fg='red', font=(
    'Ivy 13 bold'), command=limpa_campo)
b1.grid(row=2, column=0, columnspan=2, sticky='nsew')
b2 = tk.Button(text='%', command=lambda: pegar_numeros(
    '%'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b2.grid(row=2, column=2, sticky='nsew')
b3 = tk.Button(text='/', command=lambda: pegar_numeros('/'), width=5, height=3, bg=cor5,
               fg=cor2, font=('Ivy 13 bold'))
b3.grid(row=2, column=3, sticky='nsew')

b4 = tk.Button(text='7', command=lambda: pegar_numeros(
    '7'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b4.grid(row=3, column=0, sticky='nsew')
b5 = tk.Button(text='8', command=lambda: pegar_numeros(
    '8'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b5.grid(row=3, column=1, sticky='nsew')
b6 = tk.Button(text='9', command=lambda: pegar_numeros(
    '9'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b6.grid(row=3, column=2, sticky='nsew')
b7 = tk.Button(text='*', command=lambda: pegar_numeros('*'), width=5, height=3, bg=cor5,
               fg=cor2, font=('Ivy 13 bold'))
b7.grid(row=3, column=3, sticky='nsew')

b8 = tk.Button(text='4', command=lambda: pegar_numeros(
    '4'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b8.grid(row=4, column=0, sticky='nsew')
b9 = tk.Button(text='5', command=lambda: pegar_numeros(
    '5'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b9.grid(row=4, column=1, sticky='nsew')
b10 = tk.Button(text='6', command=lambda: pegar_numeros(
    '6'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b10.grid(row=4, column=2, sticky='nsew')
b11 = tk.Button(text='-', command=lambda: pegar_numeros('-'), width=5, height=3, bg=cor5,
                fg=cor2, font=('Ivy 13 bold'))
b11.grid(row=4, column=3, sticky='nsew')

b12 = tk.Button(text='1', command=lambda: pegar_numeros(
    '1'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b12.grid(row=5, column=0, sticky='nsew')
b13 = tk.Button(text='2', command=lambda: pegar_numeros(
    '2'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b13.grid(row=5, column=1, sticky='nsew')
b14 = tk.Button(text='3', command=lambda: pegar_numeros(
    '3'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b14.grid(row=5, column=2, sticky='nsew')
b15 = tk.Button(text='+', command=lambda: pegar_numeros('+'), width=5, height=3, bg=cor5,
                fg=cor2, font=('Ivy 13 bold'))
b15.grid(row=5, column=3, sticky='nsew')

b16 = tk.Button(text='0', command=lambda: pegar_numeros(
    '0'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b16.grid(row=6, column=0, columnspan=2, sticky='nsew')
b17 = tk.Button(text=',', command=lambda: pegar_numeros(
    '.'), width=5, height=3, bg=cor4, font=('Ivy 13 bold'))
b17.grid(row=6, column=2, sticky='nsew')
b18 = tk.Button(text='=', command=calcular, width=5, height=3, bg=cor5,
                fg=cor2, font=('Ivy 13 bold'))
b18.grid(row=6, column=3, sticky='nsew')


# mainloop() -> fica esperando uma ação na janela, senão o codigo abre e fecha a janela
janela.mainloop()
