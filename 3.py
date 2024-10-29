# -*- coding: utf-8 -*-
# Considere as notas de uma turma de alunos:
# 6.5, 7.2, 8.0, 5.5, 9.2, 7.8, 6.0, 7.5, 8.5, 6.8, 7.2, 8.9, 9.0, 5.0, 7.0
# (a) Construa um histograma para visualizar como as notas estão distribuídas.
# (b) Obtenha medidas de tendência central (média, moda, mediana, quartis).
# (c) Obtenha medidas de dispersão (variância, desvio padrão e coeficiente de variação).
# (d) Calcule o coeficiente de assimetria e curtose.
# (e) Construa um Box-Plot e interprete os resultados.

# No conjunto de dados fornecido, as notas dos alunos representam uma variável quantitativa contínua:

# Quantitativa: Porque os valores são numéricos, representando medidas (notas dos alunos).
# Contínua: Porque as notas podem assumir qualquer valor dentro de um intervalo, incluindo números com casas decimais (como 7.2, 6.8, etc.).
# Essas notas refletem uma medição contínua, indicando o desempenho dos alunos em uma escala que pode ter subdivisões finas. 
# A variável é contínua porque não se limita a valores inteiros e possui precisão decimal.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados fornecidos
notas = [
    6.5, 7.2, 8.0, 5.5, 9.2, 7.8, 6.0, 7.5, 8.5, 6.8, 7.2, 8.9, 9.0, 5.0, 7.0
]

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(notas, columns=['Notas'])

# Medidas de Tendência Central:
# Média: 7.34
# Moda: 7.20
# Mediana: 7.20
# Quartis:
# 0.25    6.65
# 0.50    7.20
# 0.75    8.25
# Name: Notas, dtype: float64

# Medidas de Dispersão:
# Variância: 1.61
# Desvio Padrão: 1.27
# Coeficiente de Variação: 17.26%

# Coeficiente de Assimetria e Curtose:
# Assimetria: -0.20
# Curtose: -0.84

# (a) Construindo um histograma para visualizar como as notas estão distribuídas
plt.figure(figsize=(10, 6))
plt.hist(df['Notas'], bins=6, color='skyblue', edgecolor='black')
plt.title('Histograma das Notas da Turma', fontsize=16)
plt.xlabel('Notas', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('3-histograma_notas.png')
plt.show()

# (b) Obtendo medidas de tendência central
media = df['Notas'].mean()
moda = df['Notas'].mode()[0]  # Obtendo a primeira moda
mediana = df['Notas'].median()
quartis = df['Notas'].quantile([0.25, 0.5, 0.75])

print("Medidas de Tendência Central:")
print(f"Média: {media:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Quartis:\n{quartis}")

# (b) Medidas de Tendência Central
# Média: 7.34 - Representa a média aritmética das notas, indicando a pontuação média dos alunos.
# Moda: 7.20 - A moda é a nota que mais se repete na amostra.
# Mediana: 7.20 - A mediana é o valor central, que divide a distribuição ao meio.
# Quartis:
# Q1 (25%): 6.65
# Q2 (Mediana, 50%): 7.20
# Q3 (75%): 8.25

# (c) Obtendo medidas de dispersão
variancia = df['Notas'].var()
desvio_padrao = df['Notas'].std()
coef_variacao = (desvio_padrao / media) * 100

print("\nMedidas de Dispersão:")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Coeficiente de Variação: {coef_variacao:.2f}%")

# Medidas de Dispersão:
# Variância: 1.61
# Desvio Padrão: 1.27
# Coeficiente de Variação: 17.26%

# (d) Calculando o coeficiente de assimetria e curtose
assimetria = stats.skew(df['Notas'])
curtose = stats.kurtosis(df['Notas'])

print("\nCoeficiente de Assimetria e Curtose:")
print(f"Assimetria: {assimetria:.2f}")
print(f"Curtose: {curtose:.2f}")

# Coeficiente de Assimetria e Curtose:
# Assimetria: -0.20
# Curtose: -0.84

# (d) Coeficiente de Assimetria e Curtose
# Assimetria: -0.20 - Como o valor é ligeiramente negativo, indica uma leve assimetria à esquerda, ou seja, há uma pequena tendência de as notas serem maiores.
# Curtose: -0.84 - Indica que a distribuição das notas é platicúrtica, ou seja, tem menos concentração de valores nas extremidades em comparação com uma distribuição normal.

# (e) Construindo um Box-Plot e interpretando os resultados
plt.figure(figsize=(10, 6))
plt.boxplot(df['Notas'], vert=False)
plt.title('Box-Plot das Notas da Turma', fontsize=16)
plt.xlabel('Notas', fontsize=14)
plt.xticks(fontsize=12)
plt.savefig('3-boxplot_notas.png')
plt.show()

# (e) Box-Plot
# O box-plot foi construído e mostra a dispersão das notas, incluindo:

# Mediana (7.20): Indica o valor central.
# Intervalo Interquartil (IQR): Entre Q1 (6.65) e Q3 (8.25), onde 50% dos valores estão concentrados.
# Outliers: Não foram identificados valores fora dos limites dos "bigodes" do box-plot.