# Operações com Conjuntos em Python

Este projeto tem como objetivo desenvolver um programa que realiza operações em conjuntos de dados, como **união**, **interseção**, **diferença** e **produto cartesiano**.
O programa é desenvolvido em Python e recebe como entrada um arquivo de texto (.txt) contendo os dados e as operações a serem executadas.

## Requisitos do Projeto

O programa deve ler um arquivo de texto de entrada com o seguinte formato:

    1. A primeira linha contém o número de operações a serem realizadas.

    2. As linhas seguintes descrevem as operações e os conjuntos envolvidos:

      U: União

      I: Interseção

      D: Diferença

      C: Produto cartesiano

    3. Cada operação é seguida por duas linhas contendo os elementos dos conjuntos, separados por vírgulas.

### Exemplo de Arquivo de Entrada

4

U

3, 5, 67, 7

1, 2, 3, 4

I

1, 2, 3, 4, 5

4, 5

D

1, A, C, 34

A, C, D, 23

C

3, 4, 5, 5, A, B, R

1, B, C, D, 1

### Exemplo de Saída

Para a operação de união (U) entre os conjuntos {3, 5, 67, 7} e {1, 2, 3, 4}, a saída será:

União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}

### Como Executar

O código está disponível na pasta do projeto, junto com os arquivos de teste.

O programa pode ser executado no terminal ou gerar a saída em um arquivo.

**Observação**: A saída deve estar formatada corretamente, conforme mostrado no exemplo acima, para evitar erros.
