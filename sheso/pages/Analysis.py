import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Analysis Dashboard',
    page_icon='📊'
)
st.sidebar.success('select page above')
st.markdown('<h1 style= "text-align:center; color: #FF4500 ;">Describtive analysis</h1>', unsafe_allow_html= True)


tap1, tap2 = st.tabs(['📈  stats','📊 Uni & Bivariate analysis'])
df=pd.read_csv('df1.csv')
df.drop('Unnamed: 0', axis=1, inplace= True)
num=df.describe()
cat= df.describe(include='O')

with tap1:
    col1, col2, col3 = st.columns([6,0.5,6])
    with col1:
        st.subheader('numerical descibtive stat')
        st.dataframe(num.T, 500, 400)
        
    with col3:
        st.subheader('categorical descibtive stat')
        st.dataframe(cat.T, 500, 400)
        
with tap2:
    col1, col2, col3 = st.columns([8,1, 8])
    
    
    with col1:
        st.subheader('Univariate Analysis')
        st.subheader('total price')
        fig=px.histogram(df,x= 'total_price', color_discrete_sequence= ['orange'], nbins= 10 , marginal = 'box')
        st.plotly_chart(fig,use_container_width=True)
        
        st.subheader('Gender')
        fig=px.histogram(df, x='gender',color_discrete_sequence= ['orange'])
        st.plotly_chart(fig,use_container_width=True)
        
        st.subheader('Product type per gender')
        fig=px.pie(df, names='gender',color_discrete_sequence=['orange'],facet_col='product_type')
        fig.update_layout(height=600,width=800)
        st.plotly_chart(fig,use_container_width=True)
        
    with col3: 
        st.subheader('Bivariate Analysis')
        st.subheader(' the product type  total price  per color')
        fig = px.scatter(df, x='total_price', y= 'product_type', color ='colour', marginal_x='violin', marginal_y= 'box') 
        st.plotly_chart(fig,use_container_width=True)
        
        st.subheader(' the product type  total price  per month')
        fig=px.bar(df, x='OD_month', y= 'total_price', color='product_type')
        st.plotly_chart(fig,use_container_width=True)
