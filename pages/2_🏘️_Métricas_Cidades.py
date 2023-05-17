import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config( page_title = 'Métricas Gerais', layout = 'wide')


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

st.sidebar.markdown('''---''')

quantidade_pesquisa = st.sidebar.slider("Quantidade de cidades:", min_value=5, max_value=18, value=10)


st.sidebar.markdown('### Powered by Diniz JP')

        
        
        
with st.container(): 
    
    
    st.markdown('## Métricas Cidades')
#-------------------------------------------------------------#
    

    st.markdown('### Top {} cidades com a maior quantidade de restaurantes avaliados acima de 4.0'.format(quantidade_pesquisa))
    
    st.markdown('''Esses são as cidades com o maior número de restaurantes **bem avalidados** ''')

    count_city_rating = df[df['aggregate_rating'] >= 4]['city'].value_counts().reset_index().head(quantidade_pesquisa)
    
    count_city_rating.columns = ['city', 'count']
    
    fig_count_city_rating = create_bar_chart(count_city_rating, 'city', 'count', 'Nome da Cidade', 'Quantidade de Restaurantes')
    

    st.plotly_chart(fig_count_city_rating)
    
#-------------------------------------------------------------#
    
    st.markdown('### Top {} cidades com a maior quantidade de restaurantes avaliados abaixo de 2.5 '.format(quantidade_pesquisa))

    st.markdown('''Esses são as cidades com o maior número de restaurantes **mal avalidados** ''')

    city_mean_2_5 =  df[df['aggregate_rating'] <= 2.5]['city'].value_counts().sort_values( ascending=False).reset_index().head(quantidade_pesquisa)
    
    city_mean_2_5.rename(columns={'index':'city', 'city':'count'}, inplace=True)

    fig_city_mean_2_5 = create_bar_chart(city_mean_2_5,  'city', 'count', 'Nome da Cidade', 'Quantidade de Restaurantes')
    
    st.plotly_chart(fig_city_mean_2_5)
    
#-------------------------------------------------------------#
    
    st.markdown('### Top {} cidades com a maior preço médio do prato para dois '.format(quantidade_pesquisa))

    st.markdown('''Esses são as cidades com o maior **preço médio** do prato para dois, estão presentes majoritariamente nos Países:
                 **Estados Unidos** e **Filipinas**  ''')
    
    city_mean_for2 =  df.groupby(['country_code','city'])['price_in_dollar'].mean().sort_values( ascending=False).reset_index().head(quantidade_pesquisa).round(2)
    
    fig_city_mean_for2 = create_bar_chart(city_mean_for2, 'city', 'price_in_dollar','Nome da Cidade', 'Preço em Dólar $')
    
    fig_city_mean_for2.update_traces(hovertemplate='<b>%{x}</b><br>Preço: $%{y}<br>País: %{customdata}',
                                    customdata=city_mean_for2['country_code'])
    st.plotly_chart(fig_city_mean_for2)
