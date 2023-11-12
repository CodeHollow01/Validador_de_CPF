import re

#por esse input funcionar como uma resposta em string, mesmo se for um número será interpretado como string
cpf = input("Insira seu Cpf: ")

def validação(cpf): #cria uma variável que muda de acordo como você caham a variável, nesse caso cpf

     if not cpf.isdigit(): # Verifica se todos os números do CPF são dígitos e se não for, retorna False
            return False
         
     cpf = re.sub("[^0-9]","",cpf) # Verifica os números que não são de 0-9(utilizando o ^) para trocalos por ""(apagando-os)
     cpf_calculo = cpf[0] * 11


     if cpf == cpf_calculo:
          return False

     if len(cpf) != 11: # Verifica se o tamanho do CPF inserido é igual a 11
          return False
     
     soma1 = sum(int(cpf[i]) * (10-i) for i in range(9)) # Define o valor de soma1 como o somatório do número inteiro de CPF i, sendo i de 0-8
     digito1 = (soma1 * 10) % 11 % 10 # O % em python calcula o resto de uma divisão
     soma2 = sum(int(cpf[i]) * (11-i) for i in range(10))# Define o valor de soma1 como o somatório do número inteiro de CPF i, sendo i de 0-8
     digito2 = (soma2 * 10) % 11 % 10 # O % em python calcula o resto de uma divisão

     if digito1 == int(cpf[9]) and digito2 == int(cpf[10]): # Verifica se o primeiro e o segundo dígito do CPF coicide com o inserido
          return True
     else:
          return False


if validação(cpf): # Verifica se a def(cpf) é verdadeira
     print("Valido")
else:
     print("Inválido")

