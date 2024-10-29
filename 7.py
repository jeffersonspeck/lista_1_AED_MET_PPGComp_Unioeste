# -*- coding: utf-8 -*-
# Enunciado organizado:
# Considere o conjunto de dados registrando algumas propriedades de portadores de cartão de crédito taiwaneses, disponíveis em http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients.
# Este conjunto de dados foi coletado por I-Cheng Yeh e é hospedado pelo UC Irvine Machine Learning Repository.
# Há uma variável indicando se um portador está inadimplente ou não, e uma variedade de outras variáveis.
#
# (a) Use histogramas condicionais para investigar se as pessoas que estão inadimplentes têm mais dívidas (use a variável X1 para dívida) do que aquelas que não estão inadimplentes.
# (b) Use box-plot (diagramas de caixa) para investigar se gênero, educação ou estado civil têm algum efeito no valor da dívida (novamente, use X1 para dívida).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importando o arquivo fornecido
file_path = 'default_credits.xls'
df = pd.read_excel(file_path, skiprows=[0], engine='xlrd')  # Pulando a primeira linha para obter o cabeçalho correto

# Renomeando as colunas para facilitar a manipulação
df.columns = ['ID', 'Limite_Crédito', 'Gênero', 'Educação', 'Estado_Civil', 'Idade', 'Hist_Pag_Set', 'Hist_Pag_Ago',
              'Hist_Pag_Jul', 'Hist_Pag_Jun', 'Hist_Pag_Mai', 'Hist_Pag_Abr', 'Fatura_Set', 'Fatura_Ago', 'Fatura_Jul',
              'Fatura_Jun', 'Fatura_Mai', 'Fatura_Abr', 'Pagamento_Set', 'Pagamento_Ago', 'Pagamento_Jul', 'Pagamento_Jun',
              'Pagamento_Mai', 'Pagamento_Abr', 'Inadimplente']

# (a) Histogramas condicionais para investigar inadimplência e dívida
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Limite_Crédito', hue='Inadimplente', kde=True, palette='Set1', bins=30)
plt.title('Distribuição do Limite de Crédito Condicionada à Inadimplência')
plt.xlabel('Limite de Crédito (X1)')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('histograma_inadimplencia_divida.png')
plt.show()

# (b) Box-plot individuais para investigar o efeito do gênero, educação e estado civil no valor da dívida
# Box-plot por Gênero
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Gênero', y='Limite_Crédito', palette='Set2')
plt.title('Box-Plot do Limite de Crédito por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Limite de Crédito (X1)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('boxplot_genero_divida.png')
plt.show()

# Box-plot por Educação
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Educação', y='Limite_Crédito', palette='Set3')
plt.title('Box-Plot do Limite de Crédito por Educação')
plt.xlabel('Educação')
plt.ylabel('Limite de Crédito (X1)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('boxplot_educacao_divida.png')
plt.show()

# Box-plot por Estado Civil
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Estado_Civil', y='Limite_Crédito', palette='Set1')
plt.title('Box-Plot do Limite de Crédito por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Limite de Crédito (X1)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('boxplot_estado_civil_divida.png')
plt.show()

# Explicação dos tipos de variáveis
# 'Limite_Crédito': Variável quantitativa contínua, pois representa um valor numérico (limite de crédito) que pode assumir valores dentro de um intervalo contínuo.
# 'Gênero': Variável qualitativa nominal, pois representa categorias (masculino, feminino) sem ordem implícita.
# 'Educação': Variável qualitativa ordinal, pois representa níveis de educação que têm uma ordem (por exemplo, ensino médio, graduação, pós-graduação).
# 'Estado_Civil': Variável qualitativa nominal, pois representa categorias de estado civil (solteiro, casado, etc.) sem uma ordem específica.
# 'Inadimplente': Variável qualitativa binária, pois indica duas categorias (inadimplente ou não).

# Tabulação dos dados
print("\nTabulação dos Dados:")
tabulacao_genero = df['Gênero'].value_counts()
tabulacao_educacao = df['Educação'].value_counts()
tabulacao_estado_civil = df['Estado_Civil'].value_counts()
tabulacao_inadimplencia = df['Inadimplente'].value_counts()

print("\nTabulação por Gênero:")
print(tabulacao_genero)

print("\nTabulação por Educação:")
print(tabulacao_educacao)

print("\nTabulação por Estado Civil:")
print(tabulacao_estado_civil)

print("\nTabulação por Inadimplência:")
print(tabulacao_inadimplencia)

# Tabulação dos Dados:

# Tabulação por Gênero:
# 2    18112
# 1    11888
# Name: Gênero, dtype: int64

# Tabulação por Educação:
# 2    14030
# 1    10585
# 3     4917
# 5      280
# 4      123
# 6       51
# 0       14
# Name: Educação, dtype: int64

# Tabulação por Estado Civil:
# 2    15964
# 1    13659
# 3      323
# 0       54
# Name: Estado_Civil, dtype: int64

# Tabulação por Inadimplência:
# 0    23364
# 1     6636
# Name: Inadimplente, dtype: int64

# Contexto dos Dados
# O conjunto de dados analisa portadores de cartão de crédito taiwaneses e inclui informações sobre:
# Limite de crédito (variável X1), representando o valor disponível para cada titular.
# Gênero, Educação, Estado Civil e Inadimplência, que são características dos portadores.

# A pesquisa busca responder duas perguntas principais:
# As pessoas inadimplentes têm mais dívidas? (ou seja, se há diferença nos limites de crédito para inadimplentes e não inadimplentes).
# Gênero, Educação ou Estado Civil influenciam o valor do limite de crédito?

# Resultados da Análise Exploratória
# (a) Distribuição do Limite de Crédito por Inadimplência
# O histograma gerado mostra a distribuição do limite de crédito condicionada pela inadimplência. Podemos analisar algumas características importantes:
# Sobreposição de Distribuições: Através do uso de cores diferentes para inadimplentes e não inadimplentes, 
# conseguimos ver se há uma tendência dos inadimplentes terem limites de crédito mais altos ou não.

# Tendências de Dívida:
# Se notarmos que os inadimplentes tendem a ter limites de crédito mais altos, isso sugere que pessoas com dívidas maiores têm maior dificuldade 
# em cumprir com seus pagamentos.
# Se as distribuições são bastante semelhantes, então o limite de crédito, por si só, não parece ser um bom indicador de inadimplência.

# (b) Box-Plots Individuais para Gênero, Educação e Estado Civil
# Os box-plots individuais para Gênero, Educação e Estado Civil permitem investigar se alguma dessas características tem efeito sobre o valor do limite de crédito.
# Box-Plot por Gênero:
# Compara os limites de crédito entre homens e mulheres.
# Se observarmos uma diferença significativa na mediana (linha central da caixa) ou na amplitude interquartil (IQR), podemos concluir que o gênero tem 
# algum efeito no valor do limite de crédito.
# Se os box-plots dos dois gêneros são semelhantes, o gênero pode não ser um fator significativo para determinar o valor do limite.

# Box-Plot por Educação:
# Representa o limite de crédito de acordo com diferentes níveis de educação (como ensino médio, graduação, etc.).
# Se houver diferenças na distribuição dos limites, isso pode indicar que níveis mais altos de educação tendem a estar associados a limites maiores, 
# sugerindo que a educação afeta o acesso ao crédito.

# Box-Plot por Estado Civil:
# Compara os limites de crédito para diferentes estados civis (solteiro, casado, etc.).
# Diferenças visíveis na mediana ou IQR podem indicar que o estado civil também tem algum efeito no valor do limite, possivelmente relacionado à estabilidade 
# financeira percebida pelos bancos.

# Tabulação dos Dados
# Tabulação das Variáveis Categóricas (Gênero, Educação, Estado Civil, Inadimplente):
# A tabulação nos fornece a frequência de cada categoria.
# Isso permite entender a distribuição geral dos portadores de cartão dentro dessas categorias. Por exemplo, quantos são homens versus mulheres, qual a 
# proporção de diferentes níveis de educação, quantos estão inadimplentes, etc.

# Interpretação Geral
# Inadimplência e Dívida:
# Se os inadimplentes têm um limite de crédito mais alto (observado no histograma), isso sugere que o maior valor de dívida pode estar correlacionado com um 
# risco maior de não pagamento. Isso poderia indicar a necessidade de critérios mais rigorosos para determinar o limite de crédito para certos perfis de clientes.

# Influência de Gênero, Educação e Estado Civil no Limite de Crédito:
# Gênero: Se não houver diferenças significativas entre os box-plots para homens e mulheres, o gênero pode não ser um fator relevante para o valor do limite de crédito.
# Educação: Se houver um aumento consistente no limite de crédito com níveis mais altos de educação, isso indicaria que as instituições financeiras consideram a 
# educação como um fator que melhora a estabilidade financeira e, portanto, aumentam o limite.
# Estado Civil: Diferenças entre solteiros, casados e outros estados civis poderiam indicar que os bancos associam diferentes níveis de estabilidade financeira a 
# diferentes estados civis.

# Conclusões
# A partir dos gráficos e da tabulação dos dados, algumas conclusões podem ser tiradas:
# Padrões de Dívida e Risco: Os inadimplentes tendem a ter mais dívida? Se sim, as instituições financeiras poderiam ajustar suas políticas de concessão de crédito.
# Critérios de Concessão de Crédito: Gênero, educação e estado civil afetam o limite de crédito de forma significativa? Isso ajudaria as instituições a entender se estão 
# sendo justas ou se existe algum viés sistemático na concessão de crédito.