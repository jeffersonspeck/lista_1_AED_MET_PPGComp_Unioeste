# -*- coding: utf-8 -*-

# Em um questionário aplicado aos estudantes que frequentavam a biblioteca do campus, foi perguntado como classificariam o serviço prestado. 
# As respostas foram: "ótimo", "bom", "bom", "péssimo", "bom", "bom", "ótimo", "ótimo", "bom", "ótimo", "bom", "ótimo", "bom", "bom", "ótimo", "bom", 
# "péssimo", "bom", "péssimo", "bom", "péssimo", "bom", "bom", "bom", "bom", "ótimo", "bom", "péssimo", "ótimo", "ótimo", "bom", "péssimo".
# (a) Classifique as respostas.

# (b) Construa uma tabela e um gráfico para representar e resumir essa informação. Comente.

#o tipo de variável neste caso é qualitativa ordinal.


import pandas as pd
import matplotlib.pyplot as plt

# (a) Classificando as respostas
respostas = [
    "ótimo", "bom", "bom", "péssimo", "bom", "bom", "ótimo", "ótimo", "bom", "ótimo",
    "bom", "ótimo", "bom", "bom", "ótimo", "bom", "péssimo", "bom", "péssimo", "bom",
    "péssimo", "bom", "bom", "bom", "bom", "ótimo", "bom", "péssimo", "ótimo", "ótimo",
    "bom", "péssimo"
]

# Criando um DataFrame
df = pd.DataFrame(respostas, columns=["Classificacao"])

# Tabela de Frequência:
# bom        17
# ótimo       9
# péssimo     6

# Contando as frequências de cada classificação
frequencia = df["Classificacao"].value_counts()

# (b) Construindo uma tabela e um gráfico para resumir a informação
print("Tabela de Frequência:")
print(frequencia)

# Salvando a tabela como figura
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('tight')
ax.axis('off')
tabela = ax.table(cellText=frequencia.reset_index().values, colLabels=["Classificação", "Frequência"], cellLoc='center', loc='center')
plt.savefig('1-tabela_classificacao.png')
plt.show()

# Plotando um gráfico de barras para as classificações
plt.figure(figsize=(8, 5))
frequencia.plot(kind='bar', color=['skyblue'])
plt.title('Classificação do Serviço Prestado')
plt.xlabel('Classificação')
plt.ylabel('Frequência')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Salvando o gráfico em um arquivo PNG
plt.savefig('1-classificacao_servico.png')
plt.show()