# fome-zero-project
# 1. Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes.
Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

## O Desafio
O CEO também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

# Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

# Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?


# Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

# Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

# Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária sushi, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária sushi, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?


O objetivo deste projeto é que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

# 2. Premissa assumidas para a análise
1. A análise foi realizada nas maiores quantidade de restaurantes registrados no País, Cidades e nas médias de cada avaliação
2. As 03 principais visões do Dashboard construído são Países, Cidades e Restaurantes 

# 3. Estratégia da solução
O Painel estratégico foi desenvolvido utilizando as métricas que refletem as 03 principais visões do modelo de negócio da empresa:

   - #### Métricas Gerais :
      - **Número de Restaurantes cadastrados**  
      - **Número de Paises cadastrados** 
      - **Número de Cidades cadastrados**
      - **Total de Avaliações Feitas na plataforma**
      - **Número de tipos de Culinária cadastrados**
            
   - #### Métricas Restaurantes:
      - **Top 10 restaurantes mais caros**
      - **Top 10 restaurantes com maior número de avaliações**
      - **3 Perguntas de hipótese com resposta**
           
   - #### Métricas Cidades :
      - **Top 10 cidades com a maior quantidade de restaurantes avaliados acima de 4.0**
      - **Top 10 cidades com a maior quantidade de restaurantes avaliados abaixo de 2.5**
      - **Top 10 cidades com a maior preço médio do prato para dois**
      - **Quantidade de Cidades Registrados por País**
      - **Média do número de avaliações por País**
        
   - #### Métricas Países :
      - **Média de preço do prato para duas pessoas por país em dólar**
      - **Quantidade de Restaurantes Registrados por País**
      - **Quantidade de Cidades Registrados por País**
      - **Média do número de avaliações por País**
      - **Quantidade de Culinárias distintas por País**
      - **Quantidade de Restaurantes considerado tipo Gourmet** 
            
# 4. O produto final do projeto 
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado a internet. 

O painel pode ser acessado através do link: https://dinizjp-fome-zero-project.streamlit.app/


# 5. Conclusão
O objetivo desse projeto foi reforçar as habilidades de análise explorátoria com as bibliotecas Pandas e Plotly, e também utilizar a ferramenta de desenvolvimento web Streamlit para criar um Dashboard interativo, usando gráficos que exibam as principais métricas da melhor forma possível para o CEO.

