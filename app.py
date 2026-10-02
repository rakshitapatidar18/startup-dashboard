# """
# cd "C:\Users\raksh\OneDrive\CampusX"
# python -m streamlit run "startup-dashboard/app.py" --server.port 8501
# """


import os
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "startup_cleaned.csv")

df = pd.read_csv(CSV_PATH)
st.dataframe(df)
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

st.set_page_config(layout='wide',page_title='Startup Analysis')

def load_overall_analysis():
    st.title('Overall Analysis')
    # total invested amount
    total = round(df['amount'].sum())

    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    
    # avg ticket size 
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    #  total funded startups 
    num_startups = df['startup'].nunique()
    
    col1,col2,col3,col4 = st.columns(4)

    with col1 :
      st.metric('Total',str(total) + 'Cr')

    with col2:
      st.metric('Maximum Funding',str(max_funding) + 'Cr')

    with col3:
       st.metric('Average Funding',str(round(avg_funding)) + 'Cr')

    with col4:
       st.metric('Total Funded Startups',str(num_startups))


    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    
    if selected_option == 'Total':
       temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
       temp_df = df.groupby(['year','month']).size().reset_index(name='amount')
    
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'], marker='o')
    st.pyplot(fig3)
    


def load_investor_detail(investor):
    st.title(investor)

    # load the recenct 5 investment of the investoe
    last5_df = df[df['investors'].str.contains(investor)].head()[['date',
                'startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df) 

    col1,col2 =st.columns(2)
    with col1:
    # biggest investment
       big_series = df[df['investors'].str.contains(investor)
            ].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
       st.subheader('Biggest Investments')

       # bar graphh
       fig, ax = plt.subplots()
       ax.bar(big_series.index,big_series.values)
       st.pyplot(fig)

    with col2:
       vertical_series = df[df['investors'].str.contains(investor)
                        ].groupby('vertical')['amount'].sum()
       st.subheader('Sector Investments')

       fig1, ax1 = plt.subplots()
       ax1.pie(vertical_series,labels=vertical_series.index,autopct='%0.01f%%')
       st.pyplot(fig1)

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YOY Investments')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)
    

    
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one',['Overall Analysis','StartUp','Investor'])

if option == "Overall Analysis":
    # bt0 = st.sidebar.button('Show Overall Analysis')
    # if bt0:
    load_overall_analysis()
  
elif option == 'StartUp':
    startup = st.sidebar.selectbox(
        'Select startup',
        sorted(df['startup'].dropna().unique().tolist())
    )
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')

else:
    investor = st.sidebar.selectbox(
        'Select investor',
        sorted(set(df['investors'].str.split(',').sum()))
    )
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_detail(investor)

    # st.title('Investor Analysis')



