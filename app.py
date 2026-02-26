import streamlit as st
import pandas as pd


st.set_page_config(layout="wide", page_title="scraper de livros", page_icon='📚')
st.title("📚 Scraper de livros")
st.write("Clique no botão para coletar dados do site books to scrape.")

st.divider()

st.header("Coleta de dados")

col1, col2, col3 = st.columns(3)

df = pd.read_csv('projeto_automação_livros.csv')
with col1:
    st.metric('total de livros', len(df))
with col2:
    media_valor = df['preço'].mean()
    st.metric('media de preços', f'£{media_valor:.2f}')
with col3:
    media_estrelas = df['avaliação'].mean()
    st.metric('media de avaliação', f'{media_estrelas:.2f}')

st.subheader('📊 preço medio por avaliação')
grafico = df.groupby('avaliação')['preço'].mean().reset_index()
st.bar_chart(grafico, x='avaliação', y='preço', width=800, height=400)

st.dataframe(df, use_container_width=True)
