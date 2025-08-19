lista_perguntas = [
    "[1] Calcular desconto",
    "[2] Calcular juros simples",
    "[3] Calcular juros compostos",
    "[0] Sair"
]

tipo_de_tempo = [
    "[1] dias",
    "[2] meses",
    "[3] Anos",
]

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

while True:
    for i in lista_perguntas:
        print(i)
    
    choice = input("Qual opção você deseja?: ")

    if choice == '1':
        print('Diga o valor e o desconto/porcentagem')
        valor = float(input('digite o valor: '))
        porcentagem = float(input("digite a porcentagem: "))
        d, valor_f=funcao_desconto(valor, porcentagem)
        print(f'o valor do desconto é: {d}')
        print(f'o valor final retirando o desconto é: {valor_f}')
    elif choice == '2':

        capital_inicial = float(input("Digite o seu valor inicial: "))
        juros = float(input("Digite a taxa de juros : "))

        for t in tipo_de_tempo:
            print(t)

        choice_tempo = input("Qual opção de tipo de tempo voce escolhe?: ")
        tempo_escolhido = int(input("Qual a quantidade de tempo?: "))

        if choice_tempo == '1':
            tempo = tempo_escolhido / 365
        elif choice_tempo == '2':
            tempo = tempo_escolhido / 12
        elif choice_tempo == '3':
            tempo = tempo_escolhido 

        j_s = funcao_juros_simples(capital_inicial, juros, tempo)
        print(f"O acrescimo calculado sobre o valor inicial pelo juros simples é de: {j_s:.2f}")
        
    elif choice == '3':

        capital_inicial = float(input("Digite o seu valor inicial: "))
        taxa_de_juros = float(input("digite a taxa de juros: "))
        choice_tempo = input("Qual opção de tipo de tempo voce escolhe?: ")
        tempo_escolhido = int(input("Qual a quantidade de tempo?: "))

        if choice_tempo == '1':
            tempo = tempo_escolhido / 365
        elif choice_tempo == '2':
            tempo = tempo_escolhido / 12
        elif choice_tempo == '3':
            tempo = tempo_escolhido 

        montante, j_c = funcao_juros_composto(capital_inicial, taxa_de_juros, tempo)
        print(f"O montante foi de {montante:.2f} e o juros composto é de: {j_c:.2f}")


    elif choice == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção invadila, escolha novamente')