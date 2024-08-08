#Faça um algoritmo que peça 3 números para o usuário e verifique qual o maior e menor número, mostrar também quando tiver números iguais.
num1 =  int (input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 =  int (input("Digite o terceiro: "))

maior = num1
if (num2 > num1 and num2 > num3 ):
    maior = num2
if (num3 > num1 and num3 >= num2):
    maior = num3

    menor = num1
if(num2 < num1 and num2 < num3):
    menor = num2
if(num3 < num1 and num3 <= num2 ):
    menor = num3

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")