from utils import obter_inteiro, obter_inteiro_faixa, limpar_tela
import os

def main():
    
    maior_exaustao = -1
    nome_maior_exaustao = ''
    menor_realizacao = 7
    nome_menor_realizacao = ''
    soma_medias_estudo = 0
    
    print(''' -------------------------
   Avaliação de exaustão
 -------------------------''')
    n_avaliados = obter_inteiro('Insira aqui a quantidade de pessoas a seres avaliadas: ')
    limpar_tela()
    
    for i in range(1, n_avaliados+1):
        contador_fora_do_padrao = 0
        print(f'{i}° pessoa')
        nome = input('Qual seu nome? ')
        limpar_tela()
        print(f'{nome}, sua avaliação se baseará em 9 perguntas, certo? (Pressione Enter para continuar)')
        input()
        limpar_tela()
        print('1- Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao1 = obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('2- Sinto-me esgotado(a) ao final de um dia de estudos/trabalho.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao1 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('3- Acordar de manhã e ter que enfrentar mais um dia me causa cansaço.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao1 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        
        resultado_dimensao1 = resposta_dimensao1 / 3
        diagnostico1 = checar_diagnostico(resultado_dimensao1)
        if 2.1 < resultado_dimensao1:
            contador_fora_do_padrao += 1
        
        
        print('4- Sinto que me tornei mais indiferente com as pessoas ao meu redor.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao2 = obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('5- Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao2 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('6- Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas. ')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao2 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        
        resultado_dimensao2 = resposta_dimensao2 / 3
        diagnostico2 = checar_diagnostico(resultado_dimensao2)
        if 2.1 < resultado_dimensao2:
            contador_fora_do_padrao += 1
        
        
        print('7- Consigo lidar eficazmente com os problemas que surgem no meu dia a dia.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao3 = obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('8- Sinto que estou tendo uma influência positiva na vida das pessoas.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao3 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        print('9- Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas.')
        print('0 = Nunca 1 = Raramente 2 = Às vezes 3 = Regularmente\n4 = Frequentemente 5 = Quase sempre 6 = Sempre')
        resposta_dimensao3 += obter_inteiro_faixa('', 0, 6)
        limpar_tela()
        
        resultado_dimensao3 = resposta_dimensao3 / 3
        diagnostico3 = checar_diagnostico_inverso(resultado_dimensao3)
        if 3.9 > resultado_dimensao3:
            contador_fora_do_padrao += 1
            
        soma_medias_estudo = (resultado_dimensao1 + resultado_dimensao2) / 2
        if resultado_dimensao1 > maior_exaustao:
            maior_exaustao = resultado_dimensao1
            nome_maior_exaustao = nome
        if resultado_dimensao3 < menor_realizacao:
            menor_realizacao = resultado_dimensao2
            nome_menor_realizacao = nome
    
        print(f'''========== Laudo: {nome} ========== 
Exaustão Emocional : {resultado_dimensao1:.2f} → {diagnostico1} 
Despersonalização : {resultado_dimensao2:.2f} → {diagnostico2} 
Realização Pessoal : {resultado_dimensao3:.2f} → {diagnostico3}
''')
        if contador_fora_do_padrao > 0:
            print()
            print(f'Atenção ⚠️: {contador_fora_do_padrao} dimensão(ões) fora do padrão\nRecomenda-se acompanhamento profissional. ')
        input()
        limpar_tela()
        
    media_geral = soma_medias_estudo / n_avaliados
    
    print(f'''======= Resumo do estudo ======= 
Respondentes : {n_avaliados}
Maior Exaustão : {nome_maior_exaustao} ({maior_exaustao:.2f}) 
Menor Realização : {nome_menor_realizacao} ({menor_realizacao:.2f}) 
Média Geral Burnout : {media_geral:.2f} 
''')
    input()
    limpar_tela()
        
def checar_diagnostico(a):
    if 0 <= a <= 2:
        return 'Baixo ✅'
    elif 2.1 < a < 3.9:
        return 'Moderado ⚠️'
    else:
        return 'Alto 🚨🚨'
    
def checar_diagnostico_inverso(a):
    if 0 <= a <= 2:
        return 'Baixa 🚨🚨'
    elif 2.1 <= a <= 3.9:
        return 'Moderada ⚠️'
    else:
        return 'Alta ✅' 
    
                
    
main()
    
    


