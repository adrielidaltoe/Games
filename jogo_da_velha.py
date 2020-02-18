
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def tabuleiro():
    # imprime um tabuleiro 3x3
    k=0
    tabuleiro1 = [[1,2,3],[4,5,6],[7,8,9]]
    print('Escolha uma posição no tabuleiro')
    for i in range(0,3):
        for j in range(0,3):
            k+=1
            if tabuleiro1[i][j] in l1:
                print('O', end=' ')
            elif tabuleiro1[i][j] in l2:
                print('X', end=' ')
            else:
                print(k, end=' ')
        print('')
        
def check_win(lista):
    #verifica a lista campeã
    lv = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9],[3,5,7]]
    if len(lista) >= 3:
        for i in lv:
            lr1 = list(set(lista).intersection(i))
            if len(lr1) == len(i):
                return True
    return False

def replay():
    return input('Quer jogar denovo? "SIM" ou "NAO"').lower().startswith('s')
    clear_output()

def jogo():
    tabuleiro()
    for i in range(0,5):
        jogador1 = int(input('Jogador1 escolha um número (1 a 9): '))
        if jogador1 not in l1 and jogador1 not in l2 and jogador1 < 10 and jogador1 > 0:
            l1.append(jogador1)
            clear_output()
            tabuleiro()
        else:
            while jogador1 in l1 or jogador1 in l2 or jogador1 > 10 or jogador1 < 1:
                print('Posição inválida. Escolha outro número')
                jogador1 = int(input('Jogador1 escolha um número (1 a 9): '))
            l1.append(jogador1)
            clear_output()
            tabuleiro() 
    
        if check_win(l1):
            print('Jogador1 venceu!')
            break
        
        if len(l1) == 5:
            print('O jogo empatou!')
            break
            
        if i >= 4:
            break
        jogador2 = int(input('Jogador2 escolha um número (1 a 9): '))
        if jogador2 not in l1 and jogador2 not in l2 and jogador2 < 10 and jogador2 > 0:
            l2.append(jogador2)
            clear_output()
            tabuleiro()
        else:
            while jogador2 in l1 or jogador2 in l2 or jogador2 > 10 or jogador2 < 1:
                print('Posição inválida. Escolha outro número')
                jogador2 = int(input('Jogador2 escolha um número (1 a 9): '))
            l2.append(jogador2)
            clear_output()
            tabuleiro()
    
        if check_win(l2):
            print('Jogador2 venceu!')
            break

while True:
    l1 = [] #lista de jogadas do jogador1
    l2 = [] #lista de jogadas do jogador2
    
    jogo()
    if not replay():
        print('Obrigado por ter jogado.')
        break
    clear_output()
    

