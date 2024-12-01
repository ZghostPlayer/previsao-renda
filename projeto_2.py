import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon=":$:",
)

st.write('# Análise Exploratória: Fatores que Influenciam a Renda')
st.write("""
Esta aplicação exibe gráficos para explorar como diferentes variáveis se relacionam com a renda.
""")

renda = pd.read_csv('./input/previsao_de_renda.csv')

renda['data_ref'] = pd.to_datetime(renda['data_ref'])

#plots
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=renda, x='renda', hue='posse_de_imovel', kde=True, bins=30, ax=ax)
ax.set_title('Distribuição da Renda por Posse de Imóvel')
ax.set_xlabel('Renda')
ax.set_ylabel('Frequência')
st.pyplot(fig)
st.write("""
**Legenda**:
- Este gráfico mostra a distribuição da renda, separada entre indivíduos com e sem imóvel.
- A maior parte da renda está concentrada em valores baixos (próximos de zero).
- Observa-se que pessoas **sem imóvel** (azul) têm maior frequência em rendas mais baixas.
- Para rendas mais altas (acima de 50.000), ambos os grupos apresentam frequência muito baixa, indicando poucos registros com valores extremos.
""")

fig, ax = plt.subplots(figsize=(10, 6))
renda['renda_log'] = np.log1p(renda['renda'])
sns.histplot(data=renda, x='renda_log', hue='posse_de_imovel', kde=True, bins=30, ax=ax)
ax.set_title('Distribuição da Renda por Posse de Imóvel')
ax.set_xlabel('Renda')
ax.set_ylabel('Frequência')
st.pyplot(fig)
st.write("""
**Conclusões**:
1. A **posse de imóvel** não parece ter um impacto direto significativo na renda, já que as distribuições entre os grupos são semelhantes.
2. A maior parte das rendas está concentrada entre valores reais de **2000 a 8000**, após a transformação logarítmica.
3. Valores extremos na renda (cauda longa) indicam a presença de outliers, que podem necessitar de atenção especial para evitar distorções nos modelos preditivos.
4. A transformação logarítmica foi crucial para melhorar a visualização, pois reduziu a assimetria dos dados.
""")

st.write('## Distribuição da Renda por Categoria')

# Boxplot para renda por educação
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=renda, x='educacao', y='renda', ax=ax)
ax.set_title('Renda por Educação')
ax.set_xlabel('Educação')
ax.set_ylabel('Renda')
st.pyplot(fig)
st.write("""
**Conclusões do Gráfico (Renda por Educação):**
1. A **renda aumenta com o nível educacional**, com destaque para **superior completo** e **pós-graduação** como os níveis associados às maiores rendas.
2. Indivíduos com **primário** ou **superior incompleto** apresentam rendas menores, concentradas na base da distribuição.
3. **Outliers** (rendas muito altas) estão presentes em todos os níveis, mas são mais frequentes em níveis educacionais superiores.
4. Este gráfico confirma que **educação é uma variável significativa** para a previsão da renda.
""")

# Boxplot para renda por estado civil
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=renda, x='estado_civil', y='renda', ax=ax)
ax.set_title('Renda por Estado Civil')
ax.set_xlabel('Estado Civil')
ax.set_ylabel('Renda')
st.pyplot(fig)
st.write("""
**Conclusões do Gráfico (Renda por Estado Civil):**
1. O estado civil **casado** apresenta maior concentração de rendas mais altas e maior presença de outliers.
2. Outros estados civis, como **solteiro**, **união estável** e **separado**, mostram rendas concentradas em valores menores e com menos variação.
3. Este gráfico sugere que o estado civil pode ter uma relação moderada com a renda, sendo um fator importante a ser considerado no modelo preditivo.
""")

st.write('## Gráficos bivariada')
# Pivot table para heatmap
heatmap_data = renda.pivot_table(values='renda', index='estado_civil', columns='tipo_renda', aggfunc='mean')

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title('Renda Média por Estado Civil e Tipo de Renda')
st.pyplot(fig)

st.write("""
**Conclusões do Gráfico (Renda Média por Estado Civil e Tipo de Renda):**
1. Servidores públicos separados lideram com a maior renda média (**10.538,56**), seguidos por servidores públicos casados (**7.272,92**).
2. Pensionistas e bolsistas têm as menores rendas médias, com destaque para pensionistas solteiros e bolsistas em união estável.
3. Estados civis **casado** e **solteiro** dominam as maiores variações de renda entre os diferentes tipos.
4. Este gráfico reforça que o tipo de renda tem um peso significativo na previsão de valores elevados, enquanto o estado civil é mais relevante em categorias como servidor público e empresário.
""")

# Stacked barplot: Percentual de Tipo de Renda por Faixa Etária
tipo_renda_percentual = renda.groupby(['idade', 'tipo_renda'])['renda'].count().unstack()
tipo_renda_percentual = tipo_renda_percentual.div(tipo_renda_percentual.sum(axis=1), axis=0)

# Scatterplot: Idade x Renda (Colorido por Educação)
fig = px.scatter(renda, x='idade', y='renda', color='educacao', 
                 title='Idade vs. Renda (Por Educação)', labels={'educacao': 'Educação'})
st.plotly_chart(fig)
st.write("""
**Conclusões do Gráfico (Idade vs. Renda por Educação):**
1. Indivíduos com **pós-graduação** e **superior completo** têm maior probabilidade de alcançar altos rendimentos, especialmente acima dos 40 anos.
2. A faixa etária de **30 a 50 anos** concentra a maior parte das rendas, sendo o pico de geração de riqueza.
3. Indivíduos com **primário** ou **secundário** apresentam rendas mais baixas e menor dispersão.
4. A presença de outliers é mais comum em faixas etárias avançadas e em níveis superiores de educação.
""")

fig, ax = plt.subplots(figsize=(10, 6))
tipo_renda_percentual.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Distribuição Percentual dos Tipos de Renda por Faixa Etária')
ax.set_ylabel('Percentual')
ax.set_xlabel('Faixa Etária')
st.pyplot(fig)
st.write("""
**Conclusões do Gráfico (Distribuição Percentual dos Tipos de Renda por Faixa Etária):**
1. **Assalariados** dominam a maioria das faixas etárias, começando a apresentar uma queda a partir dos 54 anos.
2. **Pensionistas** se concentram nas idades mais avançadas (acima de 54 anos), refletindo o comportamento esperado de aposentadoria.
3. **Servidores públicos** mantêm uma distribuição estável, mas com menor participação em extremos de idade.
4. **Bolsistas** são o menor tipo de renda presente no gráfico em comparação aos outros
""")




