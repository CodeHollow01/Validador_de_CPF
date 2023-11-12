import re
# o % em python calcula o resto de uma divisão
#por esse input funcionar como uma resposta em string, mesmo se for um número será interpretado como string
cpf = input("Insira seu Cpf: ")
#cria uma variável que muda de acordo como você caham a variável, nesse caso cpf
def validação(cpf):

     if not cpf.isdigit():
            return False
         
     cpf = re.sub("[^0-9]","",cpf)
     cpf_calculo = cpf[0] * 11


     if cpf == cpf_calculo:
          return False

     if len(cpf) != 11:
          return False
     
     soma1 = sum(int(cpf[i]) * (10-i) for i in range(9))
     digito1 = (soma1 * 10) % 11 % 10
     soma2 = sum(int(cpf[i]) * (11-i) for i in range(10))
     digito2 = (soma2 * 10) % 11 % 10

     if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
          return True
     else:
          return False


if validação(cpf):
     print("Valido")
else:
     print("Inválido")

