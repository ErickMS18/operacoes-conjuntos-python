# Erick Maestri de Souza
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







