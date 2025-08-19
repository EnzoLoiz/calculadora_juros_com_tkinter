import tkinter as tk
from tkinter import ttk

def funcao_desconto(valor, porcentagem):
    desconto =  valor * porcentagem/100
    valor_final=  valor - desconto 
    return desconto, valor_final

def funcao_juros_simples(capital_inicial, juros, tempo):
    juros_simples = capital_inicial * (juros/100) * tempo
    return juros_simples

def funcao_juros_composto(capital_inicial, taxa_de_juros, tempo):
    montante= capital_inicial * (1 + taxa_de_juros/100)**tempo
    juros = montante - capital_inicial

    return montante, juros





def fazer_calculo():
    quantia= float(entrada_quantia.get())
    taxa= float(entrada_taxa.get())
    tempo_escolhido=entrada_quantia_tempo.get()

    tipo_conta=tipo_de_contas.get()
    choice_tempo= tipo_de_tempo.get()

    if choice_tempo == '1':
        tempo = tempo_escolhido / 365
    elif choice_tempo == '2':
        tempo = tempo_escolhido / 12
    elif choice_tempo == '3':
        tempo = tempo_escolhido 


    if tipo_conta == "Desconto":
        desconto, valor_f= funcao_desconto(quantia, taxa)
        label_resultado_final.config(text=f"O valor do desconto é: {desconto} e o valor final retirando o desconto é: {valor_f}")
    elif tipo_conta == "Juros Simples":
        j_s= funcao_juros_simples(quantia, taxa, tempo)
        label_resultado_final.config(text=f"O acrescimo calculado sobre o valor inicial pelo juros simples é de: {j_s:.2f}")
    elif tipo_conta == "Juros Composto":
        montante, j_c= funcao_juros_composto(quantia, taxa, tempo)
        label_resultado_final.config(text=f"O montante foi de {montante:.2f} e o juros composto é de: {j_c:.2f}") 


janela=tk.Tk()
janela.title("Calculadora de juros com tkinter")
janela.geometry("800x500")

frame_topo = tk.Frame(janela)
frame_topo.pack(side="top", pady=20)

frame_tipo_conta=tk.Frame(frame_topo)
frame_tipo_conta.pack(side='left', padx=50)

label_escolha_conta_usuario = tk.Label(frame_tipo_conta, text="--> Escolha o tipo de conta que irá calcular <--")
label_escolha_conta_usuario.pack(pady= 5,side= 'top', anchor= 'w')

tipo_de_contas= ttk.Combobox(frame_tipo_conta,
    values = ["Desconto", "Juros Simples", "Juros Composto"]                                
)
tipo_de_contas.pack(padx=5,pady=5, side="top", anchor= "w")
tipo_de_contas.current(0)

frame_tempo=tk.Frame(frame_topo)
frame_tempo.pack(side='left', padx=50)

label_escolha_tempo_usuario = tk.Label(frame_tempo, text="--> Escolha o tipo de tempo  <--")
label_escolha_tempo_usuario.pack(pady= 5,side= 'top', anchor= 'center')

tipo_de_tempo= ttk.Combobox(frame_tempo,
    values = ["Dia", "Mês", "Ano"]                                
)
tipo_de_tempo.pack(padx=5,pady=5, side="top", anchor= "center")
tipo_de_tempo.current(0)

frame_centro=tk.Frame(janela)
frame_centro.pack(pady=40)

frame_centro_taxa=tk.Frame(frame_centro)
frame_centro_taxa.pack(pady=10)


frame_centro_quantia_tempo=tk.Frame(frame_centro)
frame_centro_quantia_tempo.pack(pady=10)

label_digita_quantia_tempo = tk.Label(frame_centro_quantia_tempo, text="--> Digite o tempo(caso seja desconto, não precisa colcocar)  <--")
label_digita_quantia_tempo.pack(pady= 5,side= 'top', anchor= 'center')

entrada_quantia_tempo=tk.Entry(frame_centro_quantia_tempo)
entrada_quantia_tempo.pack(side='left', padx=150)


label_digita_taxa_usuario = tk.Label(frame_centro_taxa, text="--> Digite a taxa  <--")
label_digita_taxa_usuario.pack(pady= 5,side= 'top', anchor= 'center')

entrada_taxa=tk.Entry(frame_centro_taxa)
entrada_taxa.pack(side='left', padx=150)

frame_centro_quantia=tk.Frame(frame_centro)
frame_centro_quantia.pack(pady=10)

label_digita_quantia_usuario = tk.Label(frame_centro_quantia, text="--> Digite a quantia  <--")
label_digita_quantia_usuario.pack(pady= 5,side= 'top', anchor= 'center')

entrada_quantia=tk.Entry(frame_centro_quantia)
entrada_quantia.pack(side='left', padx=150)

botao_de_calcular=tk.Button(janela, width= 20, text="CALCULAR", command=fazer_calculo)
botao_de_calcular.pack(pady=5)

label_resultado_final=tk.Label(janela, text='')
label_resultado_final.pack(pady=5)

janela.mainloop()