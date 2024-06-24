import difflib

# Função para processar os dados de entrada
def processar_dados(dados_str):
    linhas = dados_str.strip().split('\n')
    colunas = ["Campo" + str(i+1) for i in range(len(linhas))]
    dados = {col: linha for col, linha in zip(colunas, linhas)}
    return dados

# Função para comparar dois dicionários
def comparar_dados(dados1, dados2):
    diferencias = {}
    for chave in dados1.keys():
        if dados1[chave] != dados2.get(chave, None):
            diferencias[chave] = (dados1[chave], dados2.get(chave, None))
    return diferencias

# Dados das consultas (copie e cole seus dados aqui)
consulta1_str = """\
363		
14/07/20 12:09:14.000000000	
B228		
"""

consulta2_str = """\
363		
14/07/20 12:09:14.000000000	
B229
"""

# Processar os dados de entrada
consulta1 = processar_dados(consulta1_str)
consulta2 = processar_dados(consulta2_str)

# Comparar os dicionários
diferencias = comparar_dados(consulta1, consulta2)

# Imprimir as diferenças
print("Diferenças encontradas:")
for campo, (valor1, valor2) in diferencias.items():
    print(f"{campo}: '{valor1}' != '{valor2}'")
