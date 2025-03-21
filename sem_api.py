# 1. Pega o report (por texto mesmo, ou coverto pra json não mão)
# 2. Separa os dados do report
# 3. Salva no banco
# 4. E vê os reports


# lê os dados do report
# como faz um scanf em python?
linhas = []

print("Insira seu report abaixo: (dê dois enter pra terminar de enviar)")

while linha := input():
        linhas.append(linha)

print(linhas)
# salvar no banco ou no arquivo por enqnt?