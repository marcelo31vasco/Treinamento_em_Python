# Entrada e saída de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

# Processamento
novo_salario = salario * 1.1  # Aumento de 10%

# Saída formatada
print(f"\nOlá, {nome}! Aqui estão seus dados:")
print(f"Idade: {idade} anos")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Salário com aumento de 10%: R$ {novo_salario:.2f}")

