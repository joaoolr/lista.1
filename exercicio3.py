#3 - Uma escola precisa de um programa que ao lançar 4 notas de um aluno deverá calcular sua média e imprimir o seguinte status: Aprovado média 70 ou superior, Recuperação média entre 50 e 69 E Reprovado inferior a 50.

nota1 = float (input("digite a primeira nota:"))
nota2 = float (input("digite a segunda nota:"))
nota3 = float (input("digite a terceira nota:"))
nota4 = float (input("digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
print("A média das notas é:", media)

if media > 70:
    print("Você está Aprovado")
elif (media < 69):
    print("Você esta de Recuperação")
elif (media < 50):
    print("Você infelizmente está Reprovado")

