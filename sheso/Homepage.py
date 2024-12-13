import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


st.set_page_config(
    layout="wide",
    page_title="Home Page for Insights")


st.sidebar.success('select page above')
st.markdown('<h1 style= "text-align:center; color: #FF4500 ;">Shopping Cart EDA</h1>', unsafe_allow_html= True)

df=pd.read_csv('df1.csv')
product_type=pd.read_csv('product_type.csv')
achieving_gender=pd.read_csv('achieving_gender.csv')
achieveing_season=pd.read_csv('achieveing_season.csv')
underperforming_month=pd.read_csv('underperforming_month.csv')
top_10_customers=pd.read_csv('top_10_customers.csv')
revenue=pd.read_csv('revenue.csv')
age_state=pd.read_csv('age_state.csv')
state=pd.read_csv('state.csv')
average_df=pd.read_csv('date_difference_with_average.csv')

df.drop('Unnamed: 0', axis=1, inplace= True)
df_sample= df.head(10)

color1= px.colors.qualitative.Vivid

# 1 product type with the highest sales
product_type=df.groupby(['product_type'])[['total_price']].sum().sort_values(by='total_price',ascending = False)
fig = px.pie(df, values='total_price', names='product_type', hole=.3,color_discrete_sequence=px.colors.qualitative.Vivid)


# 2-gender of our most buying customers
achieving_gender=df.groupby('gender').agg({'total_price': 'sum'}).reset_index().sort_values(by='total_price',ascending = False)
fig1 = px.pie(df, values='total_price', names='gender', hole=.3,color_discrete_sequence=px.colors.qualitative.Vivid)

# 3- season  with highest sales
achieveing_season = df.groupby('order_season').agg({'total_price': 'sum'}).reset_index().sort_values(by='total_price',ascending = False)
fig2 = px.bar(achieveing_season, x="order_season", y=achieveing_season.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)


# 4- days difference between our order date and delievery date
average_diff= df['date_difference'].mean()


# 5-underperforming month
underperforming_month = df.groupby('OD_monthName').agg({'total_price': 'sum'}).reset_index().sort_values(by='total_price',ascending = True)
fig4 = px.line(underperforming_month, x="OD_monthName", y=underperforming_month.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)

# 6- top 10 most buying customers 
top_10_customers = df.groupby('customer_name').agg({'total_price': 'sum'}).reset_index().sort_values(by='total_price',ascending = False).head(10)
fig5 = px.bar(top_10_customers, x="customer_name", y=top_10_customers.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)

# 7- revenue over the months 
revenue = df.groupby('OD_monthName').agg({'total_revenue': 'mean'}).reset_index().sort_values(by='total_revenue')
fig6 = px.line(revenue, x="OD_monthName", y=revenue.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)

# 8- average age per state
age_state = df.groupby(['state']).agg({'age': 'mean'}).reset_index().sort_values(by='age', ascending=False)
fig7 = px.bar(age_state, x="state", y=age_state.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)

# 9- highest state sales 
state = df.groupby(['state']).agg({'total_price': 'sum'}).reset_index().sort_values(by='total_price', ascending=False)
fig8 = px.bar(state, x="state", y=state.columns[1:],color_discrete_sequence=px.colors.qualitative.Vivid)

# 10- corr between price and quantity 
fig9 = px.scatter(df, x='price_per_unit', y='quantity_x')

st.header('Sample Data')
st.dataframe(df_sample, hide_index=True)

st.header("product type with the highest sales")
st.plotly_chart(fig)

st.header("gender of our most buying customers?")
st.plotly_chart(fig1)


st.header("season  with highest sales?")
st.plotly_chart(fig2)

st.header("difference between delievery date and order date")
st.markdown("""
    <div style="width: 300px; height: 200px; border: 1px solid #ddd; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
        <h3 style="text-align: center;">Average Delivery Time</h3>
        <p style="text-align: center; font-size: 48px; color: #999;">{:.2f} Days</p>
        <p style="text-align: center; color: ##999;"></p>
    </div>
""".format(average_diff), unsafe_allow_html=True)

st.header("underperforming month")
st.plotly_chart(fig4)


st.header("top 10 most buying customers")
st.plotly_chart(fig5)


st.header("revenue over the months")
st.plotly_chart(fig6)

st.header("average age per state")
st.plotly_chart(fig7)

st.header("highest state sales")
st.plotly_chart(fig8)

st.header("corr between price and quantity")
st.plotly_chart(fig9)
