# -*- coding: utf-8 -*-

# 4. Considere o experimento com dois sistemas operacionais apresentado em aula. Para cada sistema, realize uma análise exploratória dos dados coletados.
#
# (a) Calcule a média, mediana, quartis, variância, desvio-padrão e coeficiente de variação.
# (b) Obtenha as medidas de assimetria e curtose.
# (c) Construa o gráfico Box-Plot.
#
# Tabela 1: Dados dos Sistemas Operacionais - Tempo (segundos)
#
# Microsoft: 14.1, 12.8, 14.8, 13.9, 12.1, 12.5, 13.9, 12.2, 12.0, 12.4, 13.0, 13.1, 12.9, 14.2
# Linux: 12.0, 13.0, 12.1, 11.0, 13.4, 14.0, 12.0, 12.3, 13.5, 12.9, 12.4, 11.6, 12.8, 12.2, 11.8, 13.0

# Os dados fornecidos representam o tempo de resposta dos sistemas operacionais, que são variáveis quantitativas contínuas. 
# Eles podem assumir qualquer valor dentro de um intervalo e representam medições numéricas.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados fornecidos
dados_microsoft = [14.1, 12.8, 14.8, 13.9, 12.1, 12.5, 13.9, 12.2, 12.0, 12.4, 13.0, 13.1, 12.9, 14.2]
dados_linux = [12.0, 13.0, 12.1, 11.0, 13.4, 14.0, 12.0, 12.3, 13.5, 12.9, 12.4, 11.6, 12.8, 12.2, 11.8, 13.0]

# Criando DataFrames a partir dos dados
df_microsoft = pd.DataFrame(dados_microsoft, columns=['Microsoft'])
df_linux = pd.DataFrame(dados_linux, columns=['Linux'])

# (a) Cálculo das medidas de tendência central e dispersão
for sistema, df in zip(['Microsoft', 'Linux'], [df_microsoft, df_linux]):
    media = df[sistema].mean()
    mediana = df[sistema].median()
    quartis = df[sistema].quantile([0.25, 0.5, 0.75])
    variancia = df[sistema].var()
    desvio_padrao = df[sistema].std()
    coef_variacao = (desvio_padrao / media) * 100

    print(f"\nSistema Operacional: {sistema}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Quartis:\n{quartis}")
    print(f"Variância: {variancia:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Coeficiente de Variação: {coef_variacao:.2f}%")

# Sistema Operacional: Microsoft
# Média: 13.14
# Mediana: 12.95
# Quartis:
# 0.25    12.425
# 0.50    12.950
# 0.75    13.900
# Name: Microsoft, dtype: float64
# Variância: 0.80
# Desvio Padrão: 0.89
# Coeficiente de Variação: 6.80%    

# Sistema Operacional: Linux
# Média: 12.50
# Mediana: 12.35
# Quartis:
# 0.25    12.00
# 0.50    12.35
# 0.75    13.00
# Name: Linux, dtype: float64
# Variância: 0.61
# Desvio Padrão: 0.78
# Coeficiente de Variação: 6.25%

# (b) Cálculo das medidas de assimetria e curtose
for sistema, df in zip(['Microsoft', 'Linux'], [df_microsoft, df_linux]):
    assimetria = stats.skew(df[sistema])
    curtose = stats.kurtosis(df[sistema])

    print(f"\nSistema Operacional: {sistema}")
    print(f"Assimetria: {assimetria:.2f}")
    print(f"Curtose: {curtose:.2f}")

# Sistema Operacional: Microsoft
# Assimetria: 0.39
# Curtose: -1.11

# Sistema Operacional: Linux
# Assimetria: 0.09
# Curtose: -0.52    

# (c) Construindo os gráficos Box-Plot
plt.figure(figsize=(10, 6))
plt.boxplot([df_microsoft['Microsoft'], df_linux['Linux']], labels=['Microsoft', 'Linux'], vert=False)
plt.title('Box-Plot dos Sistemas Operacionais', fontsize=16)
plt.xlabel('Tempo (segundos)', fontsize=14)
plt.xticks(fontsize=12)
plt.savefig('boxplot_sistemas_operacionais.png')
plt.show()


# Os dados apresentados referem-se ao tempo de resposta (em segundos) dos dois sistemas operacionais, Microsoft e Linux, em um experimento. 
# A análise descritiva realizada sobre esses dados nos ajuda a tirar algumas conclusões e fazer comparações entre os dois sistemas:

# Análise Descritiva dos Dados
#
#  Média:
# A média nos mostra o valor típico do tempo de resposta para cada sistema. Se um sistema possui uma média menor, isso indica que, em geral, 
# ele tem tempos de resposta mais rápidos.
# Comparando as médias, podemos ver qual dos sistemas tende a ter um desempenho melhor em termos de tempo de resposta.
# 
# Mediana:
# A mediana é o valor central da distribuição, dividindo os dados em duas partes iguais. Se houver outliers (valores extremos), a mediana é uma medida mais representativa
#  do valor central do que a média.
# Uma mediana menor indica que metade dos valores está abaixo desse ponto, o que pode significar que o sistema é consistentemente mais rápido na maior parte do tempo.
# 
# Quartis:
# Os quartis dividem os dados em quatro partes iguais. Eles mostram a variabilidade do sistema operacional.
# Um menor intervalo interquartil (Q1 a Q3) indica uma maior consistência no tempo de resposta.
# 
# Variância e Desvio-Padrão:
# A variância e o desvio-padrão nos mostram a dispersão dos tempos de resposta. Um valor menor significa que o sistema apresenta tempos de resposta mais próximos da média, 
# indicando maior consistência.
# Se um sistema apresenta um desvio-padrão maior, isso indica que os tempos de resposta são mais variáveis, o que pode ser um problema para a previsibilidade do desempenho.
# 
# Coeficiente de Variação:
# O coeficiente de variação, dado em porcentagem, nos mostra a relação entre o desvio-padrão e a média. Um valor menor indica menor variabilidade em relação ao valor médio, 
# sendo um bom indicativo de um desempenho mais previsível.
# 
# Assimetria:
# A assimetria indica a distribuição dos dados em relação à média.
# Uma assimetria positiva significa que há mais valores menores e alguns poucos valores maiores (indica que a maioria dos tempos de resposta são menores, mas há alguns picos).
# Uma assimetria negativa indica que há mais valores maiores e alguns poucos valores menores.
# Valores próximos de zero indicam uma distribuição simétrica.
# 
# Curtose:
# A curtose nos mostra se os dados possuem caudas mais pesadas ou leves em comparação a uma distribuição normal.
# Uma curtose positiva indica que há uma maior concentração de valores nas extremidades (valores extremos são mais frequentes).
# Uma curtose negativa indica que os valores estão mais dispersos, com menos outliers.
# 
# Interpretação dos Resultados
# Menor Média e Mediana: Se um dos sistemas tem valores menores de média e mediana, isso pode indicar um desempenho mais rápido e, possivelmente, mais eficiente.
# Menor Variância e Desvio-Padrão: Esses valores menores sugerem que o sistema operacional é mais consistente no seu tempo de resposta, oferecendo previsibilidade.
# Box-Plot: O box-plot nos ajuda a comparar visualmente a mediana e a dispersão dos tempos de resposta de ambos os sistemas. Se um sistema possui um 
# intervalo interquartil menor e uma mediana baixa, ele tende a ser mais eficiente e consistente.
# 
# O Que Isso Pode Significar?
# Desempenho: Se o Linux, por exemplo, tiver uma média de tempo menor, isso indicaria que ele geralmente responde mais rapidamente que o Microsoft. 
# Essa informação pode ser usada para avaliar qual dos sistemas é mais eficiente em termos de resposta.
# Consistência: A análise da variabilidade é importante para identificar qual dos sistemas é mais estável e previsível. 
# Um sistema que apresenta menos variação nos tempos de resposta pode ser mais adequado para tarefas que exigem consistência.
# Outliers: A presença de outliers, identificada na curtose ou no box-plot, pode indicar situações de falhas ou lentidão inesperadas que ocorreram durante os testes. 
# Esses valores devem ser analisados para entender suas causas.