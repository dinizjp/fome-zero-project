import pandas as pd 
import streamlit as st
import plotly.express as px

st.set_page_config( page_title = 'Restaurantes', layout = 'wide')


                        #Funções 
#-------------------------------------------------------------#
import plotly.express as px

def create_bar_chart(data, x, y, xlabel, ylabel, textposition='outside'):
    fig = px.bar(data.sort_values(y, ascending=False),
                 x=x,
                 y=y,
                 width=1000,
                 height=500,
                 labels={y: ylabel, x: xlabel},
                 text=y)
    
    fig.update_traces(textfont=dict(size=12),
                      textposition=textposition)
    
    colors = ['#00519e','#0d59a2','#1a62a7','#276bac','#3474b1','#417db6','#4e85bb','#5b8ec0','#6897c5',
 '#75a0c9','#82a9ce','#8fb2d3','#9cbad8','#a9c3dd','#b6cce2','#c3d5e7','#d0deec','#dde7f1']

    
    fig.update_traces(marker_color=colors)
    
    fig.update_layout(xaxis_title_font=dict(size=16),
                      xaxis_tickfont=dict(size=10))
    
    return fig

#------------ Importar o arquivo------------------------------# 

df = pd.read_csv('zomato_tratado.csv')


                    # SIDEBAR
#-------------------------------------------------------------#


st.sidebar.markdown('#  Fome Zero DashBoard')


st.sidebar.markdown("## Filtros")

countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as métricas",
        df["country_code"].unique().tolist(),
        default=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])

linhas_selecionadas = df['country_code'].isin(countries)

df = df.loc[linhas_selecionadas,:]
    


st.sidebar.markdown('''---''')
st.sidebar.markdown('### Powered by Diniz JP')


#-------------------------------------------------------------#
st.markdown('## 📊 Métricas Países')


   
with st.container():
    
    st.markdown('''---''')
    st.markdown('### Média de preço do prato para duas pessoas por país em dólar')
    st.markdown('O país com a maior média de preço do prato para duas pessoas é **Singapura**, e com menor é **Turquia** ')
    mean_price = df.groupby('country_code')['price_in_dollar'].mean().reset_index().round(2)
    fig_mean_price = create_bar_chart(mean_price, 'country_code', 'price_in_dollar', 'Países', 'Preço em dólar $')
    st.plotly_chart(fig_mean_price)
    

with st.container(): 

    st.markdown('''---''')
    st.markdown('### Quantidade de Restaurantes Registrados por País')
    st.markdown('O país que possui mais restaurantes registrados é a **India**, e com menos é a **Indonesia**  ')
    rest_country = df.groupby('country_code')['restaurant_name'].count().reset_index()
    fig_rest_country = create_bar_chart(rest_country, 'country_code', 'restaurant_name', 'Países', 'Quantidade de restaurantes')
    st.plotly_chart(fig_rest_country)

        
        
with st.container():
        
    st.markdown('''---''')
    st.markdown('### Quantidade de Cidades Registrados por País')
    st.markdown('O país com mais cidades registradas é a **India**, e com menos é o **Qatar**, **Singapura** e **Sri Lanka**  ')
    city_country = df.groupby('country_code')['city'].nunique().reset_index()
    fig_city_country = create_bar_chart(city_country, 'country_code', 'city', 'Países', 'Quantidade de cidades')
    st.plotly_chart(fig_city_country)


with st.container():
     
    st.markdown('''---''')
    st.markdown('### Média do número de avaliações por País')
    st.markdown('O país que possui, em média, a maior quantidade de avaliações registradas é a **Indonesia**, e com menos é o **Brasil** ')
    mean_votes_country = df.groupby('country_code')['votes'].mean().reset_index().round()
    fig_mean_votes_country = create_bar_chart(mean_votes_country, 'country_code', 'votes', 'Países', 'Quantidade média de avaliações')
    st.plotly_chart(fig_mean_votes_country)
    
with st.container():
     
    st.markdown('''---''')
    st.markdown('### Quantidade de Culinárias distintas por País')
    st.markdown('O país com o maior quantidade de culinárias distintas é a **India**, e com menor é as **Filipinas** ')
    country_cuisines = df.groupby('country_code')['cuisines'].nunique().reset_index().sort_values('cuisines', ascending=False).round()
    fig_country_cuisines = create_bar_chart(country_cuisines, 'country_code', 'cuisines', 'Países', 'Quantidade de culinárias')
    st.plotly_chart(fig_country_cuisines)
    
    
with st.container():
     
    st.markdown('''---''')
    st.markdown('### Quantidade de Restaurantes considerado tipo Gourmet')
    st.markdown('O país com o maior quantidade de restaurantes tipo Gourmet (o tipo mais caro) é o **Estados Unidos**, e com menor é a **Indonesia** ')
    country_price_gourmet = df[df['price_range'] >= 4]['country_code'].value_counts().sort_values( ascending=False).reset_index()
    country_price_gourmet.rename(columns={'index':'country_code', 'country_code':'count'},inplace=True)    
    fig_country_price_gourmet = create_bar_chart(country_price_gourmet, 'country_code', 'count', 'Países', 'Quantidade de restaurantes')
    st.plotly_chart(fig_country_price_gourmet)
