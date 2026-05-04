from utils import obter_inteiro, limpar_tela, obter_real
def main():
    soma_folha = 0
    maior_salario_liquido = 0
    nome_maior_salario = ''
    menor_salario_liquido = 99999999999999
    nome_menor_salario = ''
    print('''----------------------------------------
========== Folha de pagamento ==========
----------------------------------------''')
    n_funcinarios = obter_inteiro('Insira a quantidade de funcionarios a serem pagos: ')
    limpar_tela()
    
    for i in range(1, n_funcinarios+1):
        print(f'{i}° Funcionário.')
        nome = input('Qual seu nome? ')
        salario = obter_real(f' > {nome}, quanto é o seu salário bruto? ')
        horas_extra = obter_inteiro('   > Quantas horas extras você trabalhou? ')
        limpar_tela()
        
        salario_hora = salario / 220
        valor_horas_extra = horas_extra * salario_hora * 3.75
        desconto_inss = salario * 0.11
        
        if salario > 2000:
            vale_refeicao = 150.00
        else:
            vale_refeicao = 0
        
        salario_liquido = salario + valor_horas_extra - desconto_inss - vale_refeicao
        
        soma_folha += salario
        
        if salario_liquido > maior_salario_liquido:
            maior_salario_liquido = salario_liquido
            nome_maior_salario = nome
            
        if salario_liquido < menor_salario_liquido:
            menor_salario_liquido = salario_liquido
            nome_menor_salario = nome
        
        print(f'''--- Extrato: {nome} ---
Salário Bruto: R$ {salario:.2f}
Horas Extras: R$ {valor_horas_extra:.2f} ({horas_extra}h)
INSS: R$ {desconto_inss:.2f}
Vale Refeição: R$ {vale_refeicao:.2f}
Salário Líquido: R$ {salario_liquido:.2f}
---''')
        input()
        limpar_tela()
    
    print(f'''----- Resumo -----
Maior salário líquido: {nome_maior_salario} > R$ {maior_salario_liquido:.2f}
Menor salário líquido: {nome_menor_salario} > R$ {menor_salario_liquido:.2f}
Gasto total: R$ {soma_folha:.2f}
-----''')
    
    input()
    limpar_tela()
            
main()