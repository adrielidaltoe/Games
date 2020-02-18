
# coding: utf-8

# In[ ]:


import random
from IPython.display import clear_output

class JogoAdivinhacao:
    
    '''Jogo para adivinhar um número'''
    
    def randomizaNumero(self):
        self.number = random.randint(1,1000)
        
    def chuteNumero(self): #salva o chute
        self.chute = int(input('Chute um número: '))
    
    def verificaChute(self): #verifica se o número fornecido é igual a random
        if (self.chute == self.number):
            print("Você acertou")
            return True
        elif (self.chute > self.number):
            print("Você chutou um número maior")
            return False
        else:
            print('Você chutou um número menor')
            return False
        
    def replay(self): #pergunta se quer jogar novamente, se sim inicia novamente o jogo
        return input('Quer jogar denovo? "SIM" ou "NAO"').lower().startswith('s')
    
    def jogar(self): #inicia o jogo
        self.randomizaNumero()
        while True:
            self.chuteNumero()
            if self.verificaChute():
                if not self.replay():
                    print('Até a próxima!')
                    break
                else:
                    self.randomizaNumero()
                    clear_output()

