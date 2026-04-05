print("Pesquisa de Atendimento. \n")

qtdRuim = 0
qtdBom = 0
qtdExelente = 0

for i in range(50):
    nome = str(input("Qual é o seu nome?"))
    idade = int(input("Qual é o sua idade?"))
    opiniao = str(input("Como voce avalia nosso atendimento? RUIM, BOM, EXCELENTE")).lower(); opiniao.strip()
    print("\n")
    match opiniao:
        case "ruim":
            qtdRuim += 1
        case "bom":
            qtdBom += 1
        case "excelente":
            qtdExelente += 1
        case _:
            print("Opinião inválida")
            continue
            
            
print(f"Quantidade de opiniões no total: {qtdExelente + qtdBom + qtdRuim}")
print(f"Excelente: {qtdExelente}")
print(f"Bom: {qtdBom}")
print(f"Ruim: {qtdRuim}")