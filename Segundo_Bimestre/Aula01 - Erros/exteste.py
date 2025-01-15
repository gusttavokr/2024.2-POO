def nome_mes(m):
    match(m):
        case 1:
            return "Janeiro"
        case 2:
            return "Sexo"
        case _:
            raise ValueError("Número de mês inválido")

print(nome_mes(1))
print(nome_mes(2))
print(nome_mes(15))