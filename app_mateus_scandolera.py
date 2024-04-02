# importa as bibliotecas necessárias
import streamlit      as st
import pandas         as pd
import plotly.express as px

try:
    # Abre o arquivo em modo de leitura através do pandas, transformando o mesmo em um dataframe (para ver o resultado basta descomentar a "print(df)" e rodar)
    df = pd.read_csv("C:\\_Temp\\BI\\fgp_bi_sem1-main\\arquivos\\vendas_floricultura_atualizada.csv", sep=',', quotechar='"')

    # print(df)

    # Define os vendedores que vão estar disponíveis diretamente do csv
    aListaVendedores = df.Vendedor.unique()
    aListaVendedores = list(aListaVendedores)
    aListaVendedores.insert(0, 'Todos os vendedores')

    # Define o título do aplicativo
    st.title("Aplicativo de vendas por vendedor")

    # Cria o combobox na barra lateral pra selecionar os vendedores
    oOpcaoSelecionada = st.sidebar.selectbox(
        'Selecione um dos vendedores: ',
        aListaVendedores
    )

    # Filtra os resultados com base no que foi selecionado no combobox
    if oOpcaoSelecionada == 'Todos os vendedores':
        oDataFrameFiltrado = df
    else:
        oDataFrameFiltrado = df[df['Vendedor'].str.contains(oOpcaoSelecionada)]

    # Plotagem do gráfico
    if not oDataFrameFiltrado.empty:
        vendas_por_vendedor = oDataFrameFiltrado.groupby('Vendedor')['Total Venda (R$)'].sum().reset_index()
        fig = px.bar(vendas_por_vendedor, x='Vendedor', y='Total Venda (R$)', title='Total de Vendas por Vendedor')
        st.plotly_chart(fig)

    st.write(oDataFrameFiltrado)

except Exception as e:
    print(f'Ocorreu um erro ao tentar gerar o app: {e}')
    exit(-1)