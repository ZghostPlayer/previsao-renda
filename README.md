# **Previsão de Renda**

Este projeto tem como objetivo explorar fatores que influenciam a renda dos indivíduos e construir modelos preditivos utilizando técnicas de Ciência de Dados. Além disso, inclui uma aplicação interativa desenvolvida em **Streamlit** para análise visual dos dados.

---

## 🎯 **Objetivo do Projeto**
O projeto foi desenvolvido para:
- Explorar as variáveis que influenciam a renda.
- Construir modelos preditivos utilizando algoritmos como **Regressão Linear** e **Random Forest**.
- Criar uma aplicação interativa para análise de dados e visualização de resultados.

---

## 🛠️ **Ferramentas Utilizadas**
### **Linguagem de Programação:**
- Python

### **Bibliotecas:**
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `scikit-learn`
- `streamlit`
- `plotly`

### **IDE:**
- Jupyter Notebook
- Visual Studio Code

---

## 📊 **Análise dos Dados**

O processo seguiu as etapas do **CRISP-DM**:

1. **Entendimento do Negócio**:
   - Identificação de variáveis relevantes e definição do problema.

2. **Entendimento dos Dados**:
   - Exploração e análise das variáveis.
   - Análise univariada e relações bivariadas.

3. **Preparação dos Dados**:
   - Tratamento de dados faltantes.
   - Transformação de variáveis categóricas em numéricas.
   - Criação de novas variáveis, como log-transformações.

4. **Modelagem**:
   - Teste de algoritmos: **Regressão Linear** e **Random Forest**.
   - O **Random Forest** foi selecionado como o melhor modelo com os seguintes resultados:
     - **R²:** 0.37
     - **RMSE:** 4203.31
     - **MAE:** 2597.37

5. **Avaliação**:
   - Comparação entre os modelos.
   - Análise das variáveis mais importantes.

---

## 📈 **Visualizações**
A aplicação **Streamlit** apresenta:

1. **Distribuição da Renda**:
   - Por características como posse de imóvel, estado civil e educação.

2. **Relações Bivariadas**:
   - Gráficos de dispersão e boxplots para entender como variáveis como idade e tipo de renda influenciam a renda.

3. **Análises Interativas**:
   - Gráficos interativos criados com **Plotly**, como a evolução da renda ao longo do tempo.

---

## 🌐 **Video da aplicação**

https://github.com/user-attachments/assets/6fcab94f-32bb-4cab-80bb-1167fc28cc23

---

## 📂 **Estrutura do Projeto**
```plaintext
previsao-renda/
├── input/                # Dados utilizados no projeto
├── output/               # Imagens e resultados gerados
├── projeto_2.ipynb       # Jupyter Notebooks com análises iniciais
├── projeto_2.py          # Código principal da aplicação Streamlit
└── README.md             # Arquivo de descrição do projeto
```

## 🔍 **Exemplos de Gráficos**
1. **Distribuição da Renda**
2. **Idade vs. Renda (Por Educação)**
3. **Renda Média por Estado Civil e Tipo de Renda**

## 💡 **Conclusões**
- **Educação** tem grande impacto na renda, especialmente para níveis superiores como **pós-graduação**.
- **Estado Civil** influencia moderadamente, com **casados** apresentando maior renda média.
- **Modelos de Machine Learning**:
  - O **Random Forest** se mostrou mais eficiente para prever a renda, superando a **Regressão Linear**.

---
