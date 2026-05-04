import os
def obter_inteiro(a:str):   
    while True:
        try:
            return int(input(a))
        except:
            print('Favor inserir um número')
            
def obter_real(a:str):   
    while True:
        try:
            return float(input(a))
        except:
            print('Favor inserir um número')
                
def obter_inteiro_faixa(a,i, l):
    numero = obter_inteiro(a)
    while True:
        if i <= numero  <= l:
            return numero
        else:
            print(f'Favor inserir um número entre {i} e {l}')
            numero = obter_inteiro(a)
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
