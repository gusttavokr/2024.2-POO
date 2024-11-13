x = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"}

print(x["RN"])

x["AM"] = "Manaus"

print(x)

for item in x.items():
    print(item)