# Inicializa o contador de vitórias
vitorias = 0

# Lê o resultado dos 6 jogos disputados
for i in range(6):
    # .upper() garante que 'v' minúsculo vire 'V' maiúsculo
    # .strip() remove espaços em branco acidentais
    resultado = input().upper().strip()
    
    if resultado == 'V':
        vitorias += 1

# Determina o grupo na OBI baseado no número de vitórias acumuladas
if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >= 1:
    print(3)
else:
    print(-1)
