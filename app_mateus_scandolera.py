# importa as bibliotecas necessárias
import streamlit as st
import pandas    as pd

# Abre o arquivo em modo de leitura através do pandas, transformando o mesmo em um dataframe (para ver o resultado basta descomentar a "print(df)" e rodar)
df = pd.read_csv("C:\\Dev\\_Temp\\BI\\fgp-bi-sem1\\arquivos\\vendas_floricultura_atualizada.csv", sep=',', quotechar='"')

# print(df)

# Define os vendedores que vão estar disponíveis
aVendedoresDisponiveis = [
    "Todos os vendedores",
    "Vendedor 1"         ,
    "Vendedor 2"         ,
    "Vendedor 3"
]

# Define o título do aplicativo
st.title("Aplicativo de vendas por vendedor")

# Cria o combobox na barra lateral pra selecionar os vendedores
oOpcaoSelecionada = st.sidebar.selectbox(
    'Selecione um dos vendedores: ',
    aVendedoresDisponiveis
)

# Filtra os resultados com base no que foi selecionado no combobox
if oOpcaoSelecionada == 'Todos os vendedores':
    oDataFrameFiltrado = df
else:
    oDataFrameFiltrado = df[df['Vendedor'].str.contains(oOpcaoSelecionada)]

st.table(oDataFrameFiltrado)
