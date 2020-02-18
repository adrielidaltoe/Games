
# coding: utf-8

# In[11]:


class Calculadora:
    
    '''A função calcular roda a calculadora automaticamente'''
    
    def _escolheOperador(self):
        print('Escolha uma operação: \n\n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n')
        
        while True: #checa se foi fornecido valores como espaço, enter e trata isso
            try:
                operacao = int(input('Escolha 1, 2, 3 ou 4:'))
            except:
                print('Parece que você não escolheu um número entre 1 e 4')
                continue
            else:
                break
        
        while True: #checa se o valor fornecido foi > 4 ou < 1
            if operacao > 4 or operacao < 1:
                print('Parece que você não escolheu um número entre 1 e 4')
                operacao = int(input('Escolha 1, 2, 3 ou 4:'))
            else:
                break
        return operacao
    
    def _escolhaNum(self): #pede que o usuário informe um número
        while True:
            try:
                valor = int(input('Digite um número:'))
            except:
                print('Parece que você não escolheu um número. Tente novamente')
                continue
            else:
                break
        return valor
    
    def _retornaCalculo(self, operador, num1, num2): #verificar o operador escolhido e retorna a operação com os números escolhi.
        if operador == 1:
            print('O resultado é %s + %s = ' %(num1,num2), num1 + num2)
        elif operador == 2:
            print('O resultado é %s - %s = ' %(num1,num2), num1 - num2)
        elif operador == 3:
            print('O resultado é %s * %s = ' %(num1,num2), num1 * num2)
        else:
            try:
                print('O resultado é %s / %s = ' %(num1,num2), num1 / num2)
            except: 
                print('Não existe divisão por 0, escolha outro segundo número')
    
    def _replay(self): #pergunta se quer fazer outra operação e inicializa novamente
        return input('Deseja fazer um novo cálculo? "SIM" ou "NAO"').lower().startswith('s')
    
    def calcular(self): #função calcular, reune todas as outras
        
        while True:
            operador = self._escolheOperador()
            print()
            num1 = self._escolhaNum()
            num2 = self._escolhaNum()
            print()
            self._retornaCalculo(operador, num1, num2) 
            print()
            if not self._replay():
                break

