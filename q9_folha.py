from utils import obter_inteiro, limpar_tela, obter_real
def main():
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
        
        print(f'''--- Extrato: {nome} ---
Salário Bruto: R$ {salario:.2f}
Horas Extras: R$ {valor_horas_extra:.2f} ({horas_extra}h)
INSS: R$ {desconto_inss:.2f}
Vale Refeição: R$ {vale_refeicao:.2f}
Salário Líquido: R$ {salario_liquido:.2f}
---''')
        input()
        limpar_tela()
            
main()