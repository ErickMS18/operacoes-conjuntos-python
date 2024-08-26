# Erick Maestri de Souza
#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#4
#U
#3, 5, 67, 7
#1, 2, 3, 4
#I
#1, 2, 3, 4, 5
#4, 5
#D
#1, A, C, 34
#A, C, D, 23
#C
#3, 4, 5, 5, A, B, R
#1, B, C, D, 1
#Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
#{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
#A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
#a informação e a formatação mostrada a seguir:
#União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
#Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
#de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
#No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.

#Criei uma pasta com meu código e os arquivos para serem lidos; pode-se tanto alterar um código já existente ou só incluir o novo arquivo na pasta.
#Detalhes de como abrir os arquivos no fim do código; no último comentário

import re
from itertools import product

def abrir_arquivo(path): #Como serão realizado testes, uma função é necessária para otimização.
    with open(path, "r") as file:
        conteudo = file.read().splitlines()
    return conteudo

def processar_operacoes(conteudo_arquivo): #Calcula quantas operações serão feitas no arquivo.
    numero_repeticoes = int(conteudo_arquivo[0])
    linha_atual = 1

    for _ in range(numero_repeticoes):
        if linha_atual + 2 >= len(conteudo_arquivo):
            break

        operacao = conteudo_arquivo[linha_atual]
        linha_atual += 1

        numeros_A = re.findall(r"\d+|\w", conteudo_arquivo[linha_atual]) #Graças ao import re, posso usar d+ para interpretar corretamente números consecutivos com mais de uma casa decimal e o w para interpretar alfanuméricos.
        numeros_B = re.findall(r"\d+|\w", conteudo_arquivo[linha_atual + 1])

        A = []
        B = []

        for num in numeros_A:
            A.append(int(num) if num.isdigit() else num) #Caso seja um número, ele converte para inteiro, se não, o caracter se mantém como string e é adicionado na lista A.


        for num in numeros_B:
            B.append(int(num) if num.isdigit() else num)

        conjuntoA = set(A) #Transformar listas em conjuntos me permite executar comandos naturais do Python para União, Intersecção e Diferença.
        conjuntoB = set(B)

        if operacao == "U":
            resultado = conjuntoA | conjuntoB
            print(f"União: conjunto A {conjuntoA}, conjunto B {conjuntoB}. Resultado: {resultado}")
        elif operacao == "I":
            resultado = conjuntoA & conjuntoB
            print(f"Intersecção: conjunto A {conjuntoA}, conjunto B {conjuntoB}. Resultado: {resultado}")
        elif operacao == "D":
            resultado = conjuntoA - conjuntoB
            print(f"Diferença: conjunto A {conjuntoA}, conjunto B {conjuntoB}. Resultado: {resultado}")
        elif operacao == "C":
            resultado = list(product(A, B))
            print(f"Produto Cartesiano: conjunto A {conjuntoA}, conjunto B {conjuntoB}. Resultado: {resultado}")
        else:
            print("Operação inválida")

        linha_atual += 2

executar_arquivo = input("Nome do arquivo a ser executado: ") #Digite exatamente o nome do arquivo com sua extensão; Ex: Teste 3.txt
conteudo_arquivo = abrir_arquivo((executar_arquivo))

processar_operacoes(conteudo_arquivo)







