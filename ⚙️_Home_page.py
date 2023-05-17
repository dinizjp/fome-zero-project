import pandas as pd
import streamlit as st

df = pd.read_csv('zomato_tratado.csv')

st.set_page_config(
        page_title= 'Main Page'
        layout = 'wide'
)


                    # SIDEBAR
#-------------------------------------------------------------#

st.sidebar.markdown('# Fome Zero DashBoard')
st.sidebar.markdown('''---''')
st.sidebar.markdown('### Powered by Diniz JP')


st.sidebar.markdown("### Dados Tratados")

processed_data = pd.read_csv("zomato_tratado.csv")

st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",)



                 
#-------------------------------------------------------------#

with st.container():
    
    st.markdown('## 📈 Métricas Gerais')
    
    col1, col2, col3, col4, col5 = st.columns( 5, gap='small' )
    
    with col1:
        resp1 = len(df['restaurant_id'].unique())
        col1.metric('Restaurantes Cadastrados', resp1)
        
    with col2:
        resp2 = len(df['country_code'].unique())
        col2.metric('Países Cadastrados', resp2)
        
    with col3: 
        resp3 = len(df['city'].unique())
        col3.metric('Cidades Cadastradas', resp3)
        
    with col4:
        resp4 = df['votes'].sum()
        col4.metric('Avaliações Feitas na plataforma', f"{resp4:,}".replace(",", "."))

    with col5: 
        resp5 = len(df['cuisines'].unique())
        col5.metric('Tipos de Culinária Cadastrados',resp5)
        

st.write('# Fome Zero Growth Dashboard')

st.markdown(
    """
       Fome Zero Dashboard foi construido para ajudar o time de négocio a **tomar melhores decisões baseados nos dados** mais relevantes encontrados na análise exploratória dos dados
       
       
        ### Como utilizar esses Dashboard?
        - #### Métricas Gerais :
            - **Número de Restaurantes cadastrados**  
            - **Número de Paises cadastrados** 
            - **Número de Cidades cadastrados**
            - **Total de Avaliações Feitas na plataforma**
            - **Número de tipos de Culinária cadastrados**
            
        - #### Métricas Restaurantes:
            - **Top 10 restaurantes mais caros**
            - **Top 10 restaurantes com mais avaliações**
            - **Top 10 cidades com a maior quantidade de restaurantes avaliados acima de 4.0**
            
            
        - #### Gráficos :
            - **Média de preço do prato para duas pessoas por País**
            - **Quantidade de Restaurantes Registrados por País**
            - **Quantidade de Cidades Registrados por País**
            - **Média do número de avaliações por País**
        
        
        
        
""" )





