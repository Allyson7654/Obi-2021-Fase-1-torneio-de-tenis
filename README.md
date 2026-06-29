OBI 2021 - Torneio de Tênis

Este repositório apresenta uma solução desenvolvida em Python para o problema "Torneio de Tênis", proposto na Fase 1 - Nível Júnior da Olimpíada Brasileira de Informática (OBI) de 2021.

Sobre o problema

No Torneio de Tênis organizado pela Confederação Brasileira de Tênis, cada participante disputa 6 partidas. Ao final dos jogos, o jogador é classificado de acordo com a quantidade de vitórias obtidas:

Grupo 1: 5 ou 6 vitórias.
Grupo 2: 3 ou 4 vitórias.
Grupo 3: 1 ou 2 vitórias.
Eliminado (-1): nenhuma vitória.

O objetivo do programa é receber o resultado das seis partidas e informar automaticamente em qual grupo o participante será classificado.

Entrada

A entrada é composta por 6 linhas, cada uma representando o resultado de uma partida:

`v` para vitória.
`P` para derrota.

Saída

O programa deve exibir apenas um número inteiro indicando a classificação do jogador:

`1` para Grupo 1;
`2` para Grupo 2;
`3` para Grupo 3;
`-1` caso o participante seja eliminado.


Como a solução foi desenvolvida

A solução foi pensada para ser simples, organizada e fácil de entender.

Primeiramente, é utilizado um laço de repetição `for`, que executa exatamente seis vezes, uma para cada partida. Em cada repetição, o programa lê o resultado informado pelo usuário. Para evitar problemas com letras minúsculas ou espaços extras, são utilizados os métodos `.upper()` e `.strip()`. Sempre que o resultado é `V`, o contador de vitórias é incrementado.

Após a leitura de todas as partidas, uma estrutura de decisão (`if`, `elif` e `else`) verifica a quantidade de vitórias e determina o grupo correspondente, exibindo o resultado na tela.


Tecnologias utilizadas

Linguagem: Python 3
Conceitos aplicados:

Estruturas de repetição (`for`);
Entrada e saída de dados (`input` e `print`);
Manipulação de strings (`.upper()` e `.strip()`);
Estruturas condicionais (`if`, `elif` e `else`).
