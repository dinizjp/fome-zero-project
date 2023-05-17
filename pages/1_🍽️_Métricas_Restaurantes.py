import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config( page_title = 'Métricas Gerais', layout = 'wide',theme="light")


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

quantidade_pesquisa = st.sidebar.slider("Quantidade de restaurantes:", min_value=5, max_value=18, value=10)


st.sidebar.markdown('### Powered by Diniz JP')



        
#-------------------------------------------------------------#
        
        
with st.container(): 
    
    
    st.markdown('## Métricas Restaurantes')
#-------------------------------------------------------------#
   
    st.markdown('### Top {} restaurantes mais caros'.format(quantidade_pesquisa))
    
    st.markdown('''Esses são os restaurantes mais caros encontrados no banco de dados, estão presentes majoritariamente nos Países:
                 **Estados Unidos** e **Singapura**   ''')
    
    top_10_more_expensive = df.nlargest(quantidade_pesquisa,'price_in_dollar').reset_index(drop=True)
    
    fig_10_more_expensive = create_bar_chart(top_10_more_expensive, 'restaurant_name', 'price_in_dollar', 'Nome do Restaurante', 'Preço em Dólar $')
    
    fig_10_more_expensive.update_traces(hovertemplate='<b>%{x}</b><br>Preço: $%{y}<br>País: %{customdata}',
                                    customdata=top_10_more_expensive['country_code'])
    
    st.plotly_chart(fig_10_more_expensive)

#-------------------------------------------------------------#
    
    
    st.markdown('### Top {} restaurantes com maior número de avaliações'.format(quantidade_pesquisa))
    
    st.markdown('''Esses são os restaurantes com maior número de avaliações encontrados no banco de dados, estão presentes majoritariamente na **India** ''')
        
    top_10_more_vote = df.nlargest(quantidade_pesquisa, 'votes').reset_index(drop=True)
    
    fig_10_more_vote = create_bar_chart(top_10_more_vote, 'restaurant_name', 'votes', 'Nome restaurante', 'Quantidade de Avaliações')
    
    fig_10_more_vote.update_traces(hovertemplate='<b>%{x}</b><br>Preço: $%{y}<br>País: %{customdata}',
                                    customdata=top_10_more_vote['country_code'])
    
    st.plotly_chart(fig_10_more_vote)

    

#-------------------------------------------------------------#

    st.markdown('####  Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)??')

    st.markdown('''**Sim**, os pratos japonses nos USA tem um valor médio maior do que o prato para duas nas churrascarias americanas ''')

    rest_japanese = df.loc[(df['country_code'] == 'United States of America') & (df['cuisines'] == 'Japanese'), 'price_in_dollar'].mean().round(2)

    rest_bbq = df.loc[(df['country_code'] == 'United States of America') & (df['cuisines'] == 'BBQ'), 'price_in_dollar'].mean().round(2)

    df_result = pd.DataFrame( {'cuisines': ['Japonesa', 'BBQ'],
            'mean_price_in_dollar': [rest_japanese, rest_bbq]})

    fig_df_result = create_bar_chart(df_result, 'cuisines', 'mean_price_in_dollar', 'Tipo de Culinária', 'Valor Médio em Dólar$')
   
    fig_df_result.update_xaxes(tickfont=dict(size=16))

    fig_df_result.update_traces( marker_color=['#EC6868', '#68AAEC'], textfont=dict(size=15) )
    
    st.plotly_chart(fig_df_result)


#-------------------------------------------------------------#
    
    st.markdown('#### Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?')

    st.markdown('''**Não**, os restaurantes que aceitam reserva tem um valor médio menor do prato para duas pessoas ''')    
    
    
    group_mean_reserv = df.groupby('has_table_booking')['price_in_dollar'].mean().reset_index().sort_values('price_in_dollar', ascending=False).round(2)

    group_mean_reserv.replace({0: 'Aceita Reserva', 1: 'Não Aceita Reserva'}, inplace=True)
    
    fig_group_mean_reserv = create_bar_chart(group_mean_reserv, 'has_table_booking', 'price_in_dollar', '', 'Valor médio em Dólar$')
   
    fig_group_mean_reserv.update_xaxes(tickfont=dict(size=16))

    fig_group_mean_reserv.update_traces( marker_color=['#EC6868', '#68AAEC'], textfont=dict(size=15) )
    
    st.plotly_chart(fig_group_mean_reserv)
    
    

#-------------------------------------------------------------#

    st.markdown('####  Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?')
    
    st.markdown('''**Sim**, os restaurantes que aceitam pedido online têm, em média, mais avaliações registradas. ''')
    
    group_mean_delivery = df.groupby('has_online_delivery')['votes'].mean().reset_index().round()
    
    group_mean_delivery = group_mean_delivery.sort_values('votes', ascending= False)

    fig_group_mean_delivery = create_bar_chart(group_mean_delivery, 'has_online_delivery', 'votes', '', 'Quantidade de Avaliações')

    fig_group_mean_delivery.update_xaxes(tickvals=[1, 0], ticktext=['Com pedidos online', 'Sem pedidos online'], tickfont=dict(size=16))

    fig_group_mean_delivery.update_traces(marker_color=['#68AAEC', '#EC6868'], textfont=dict(size=15))

    st.plotly_chart(fig_group_mean_delivery)
