# -*- coding: utf-8 -*-
# Considere o conjunto de dados relacionado ao tempo de carga (em segundos) de um aplicativo:
# 4,7  4,9  5,1  5,4  5,7  6,0  6,3  6,8  7,3  8,4
# 4,8  4,9  5,1  5,4  5,7  6,0  6,3  6,8  7,3  8,9
# 4,8  5,0  5,2  5,5  5,7  6,2  6,4  6,9  8,2  9,1
# 4,9  5,0  5,3  5,6  5,7  6,2  6,5  7,0  8,2  9,9
# 4,9  5,0  5,4  5,6  5,9  6,2  6,7  7,1  8,3  14,1

# A variável utilizada no conjunto de dados fornecido é uma variável quantitativa contínua:

# Quantitativa: Porque representa valores numéricos (tempo de carga em segundos).
# Contínua: Porque pode assumir qualquer valor dentro de um intervalo contínuo, incluindo casas decimais (como 4,7; 5,0; 6,8).
# Essas características indicam que estamos lidando com medições que podem ter qualquer valor real dentro de um intervalo, 
# tornando a variável ideal para ser representada por métodos como histogramas e box-plots.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos
dados = [
    4.7, 4.9, 5.1, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.4,
    4.8, 4.9, 5.1, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.9,
    4.8, 5.0, 5.2, 5.5, 5.7, 6.2, 6.4, 6.9, 8.2, 9.1,
    4.9, 5.0, 5.3, 5.6, 5.7, 6.2, 6.5, 7.0, 8.2, 9.9,
    4.9, 5.0, 5.4, 5.6, 5.9, 6.2, 6.7, 7.1, 8.3, 14.1
]

# Criando um DataFrame a partir dos dados
df = pd.DataFrame(dados, columns=['Tempo de Carga'])

# (a) Construindo classes e tabela de frequências
num_classes = 6  # Escolhemos 6 classes para agrupar os dados
frequencias, bins = np.histogram(df['Tempo de Carga'], bins=num_classes)
classes = [f"{bins[i]:.1f} - {bins[i+1]:.1f}" for i in range(len(bins) - 1)]

# Tabela de frequências com cálculo das frequências
frequencia_absoluta = pd.DataFrame({
    'Classe': classes,
    'Freq Absoluta': frequencias
})
frequencia_absoluta['Freq Relativa'] = frequencia_absoluta['Freq Absoluta'] / len(df)
frequencia_absoluta['Freq Percentual (%)'] = frequencia_absoluta['Freq Relativa'] * 100
frequencia_absoluta['Freq Acumulada'] = frequencia_absoluta['Freq Absoluta'].cumsum()
frequencia_absoluta['Freq Acumulada Relativa'] = frequencia_absoluta['Freq Acumulada'] / len(df)
frequencia_absoluta['Freq Acumulada Percentual (%)'] = frequencia_absoluta['Freq Acumulada Relativa'] * 100

# Mostrando a tabela de frequências
print("Tabela de Frequências:")
print(frequencia_absoluta)

# Salvando a tabela de frequências como imagem
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
tabela = ax.table(
    cellText=frequencia_absoluta.values,
    colLabels=frequencia_absoluta.columns,
    cellLoc='center',
    loc='center'
)
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
plt.savefig('2-tabela_frequencias.png')
plt.show()

# (c) Histograma das classes
plt.figure(figsize=(12, 6))
plt.hist(df['Tempo de Carga'], bins=num_classes, color='skyblue', edgecolor='black')
plt.title('Histograma do Tempo de Carga', fontsize=16)
plt.xlabel('Tempo de Carga (segundos)', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('2-histograma_tempo_carga.png')
plt.show()

# (d) Função para construir o diagrama de ramo e folhas
dados_ordenados = sorted(dados)
ramos = {}

for valor in dados_ordenados:
    ramo = int(valor)
    folha = int(round((valor - ramo) * 10))
    if ramo not in ramos:
        ramos[ramo] = []
    ramos[ramo].append(folha)

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

tabela = []
for ramo, folhas in ramos.items():
    folhas_str = " ".join(map(str, folhas))
    tabela.append([f"{ramo} | {folhas_str}"])

ax.table(
    cellText=tabela,
    colLabels=["Diagrama de Ramo e Folhas"],
    cellLoc='left',
    loc='center',
    fontsize=12
)
plt.savefig('2-diagrama_ramo_folhas.png')
plt.show()

# Interpretação do Diagrama de Ramo-e-Folhas
# O diagrama de ramo-e-folhas é uma maneira de representar os dados de forma ordenada, que permite visualizar 

# rapidamente a distribuição dos valores. Nesse tipo de diagrama:
# Ramo: Representa a parte inteira do valor (por exemplo, 4).
# Folha: Representa a parte decimal, multiplicada por 10 (por exemplo, 7 para 4,7).


# Esse diagrama serve para:
# Facilitar a visualização dos dados e identificar a frequência dos valores.
# Mostrar a forma da distribuição, destacando a concentração dos dados.
# Evidenciar possíveis outliers.

# Interpretação dos Dados:
# No diagrama, podemos observar que a maioria dos tempos de carga está concentrada nos valores 4, 5 e 6.
# Há algumas folhas nos ramos 8 e 9, indicando alguns tempos de carga mais longos.
# Um outlier significativo está no ramo 14, que é o valor 14,1. Isso indica que houve um tempo de carga muito acima da média, fora do padrão dos outros valores.

# (e) Box-plot do tempo de carga
plt.figure(figsize=(12, 6))
plt.boxplot(df['Tempo de Carga'], vert=False)
plt.title('Box-Plot do Tempo de Carga', fontsize=16)
plt.xlabel('Tempo de Carga (segundos)', fontsize=14)
plt.xticks(fontsize=12)
plt.savefig('2-boxplot_tempo_carga.png')
plt.show()

# Interpretação do Box-Plot
# O box-plot (ou gráfico de caixa) é uma representação gráfica que mostra a distribuição dos dados de forma resumida. Ele fornece informações como:
# Caixa: Representa o intervalo interquartil (IQR), que vai do primeiro quartil (Q1) ao terceiro quartil (Q3), contendo os 50% centrais dos dados.
# Linha no meio da caixa: Representa a mediana, que é o valor central dos dados.
# "Bigodes" (Whiskers): Representam os limites dos dados, geralmente definidos como 1,5 vezes o IQR para cada lado. Valores fora desses limites são considerados outliers.
# Pontos fora dos "bigodes": Representam os outliers, que são valores que se desviam significativamente do resto da distribuição.

# Interpretação dos Dados:
# A mediana está em torno de 5,7, indicando que metade dos tempos de carga está abaixo desse valor e metade acima.
# A caixa mostra que a maioria dos dados está concentrada entre aproximadamente 5,0 e 6,9 segundos, o que corresponde ao IQR.
# Um outlier significativo aparece em 14,1 segundos, que está fora do padrão dos outros valores e indica um tempo de carga anormalmente alto em comparação com os demais.

# Para Que Cada Representação Serve
# Diagrama de Ramo-e-Folhas: Serve para visualizar rapidamente a distribuição e concentração dos dados, além de ajudar a identificar a ordem e a frequência dos valores. 
# É uma boa escolha para pequenas quantidades de dados.

# Box-Plot: É útil para resumir a distribuição dos dados, mostrar a mediana, os quartis, e identificar outliers. 
# Ele fornece uma visão geral da variabilidade dos dados e é particularmente útil para comparar distribuições entre diferentes grupos.
