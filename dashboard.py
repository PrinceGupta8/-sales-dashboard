#9. **Mini Dashboard**  
   #Create a dashboard for a dataset (e.g., COVID-19 data or a sales dataset) that displays:  
   ##- Summary statistics (mean, median, count) for numeric columns.  
   ##- Interactive charts (e.g., bar, line, pie charts) based on user inputs.  
   ##- Filters for time range, region, or category.
st.title('Sales Dashboard')
data=pd.read_csv('sales_data_sample.csv',encoding='ISO-8859-1')
data.rename(columns={'PRODUCTLINE':'Product Category','MONTH_ID':'Month','YEAR_ID':'Year'},inplace=True)


#filters for time range ,region,category
year=st.sidebar.multiselect('Select Year',options=data['Year'].unique(),default=data['Year'].unique())
month=st.sidebar.slider('Select Month',min_value=1,max_value=12,value=(1,12))
country=st.sidebar.multiselect('Select Country',options=data['COUNTRY'].unique(),default=data['COUNTRY'].unique())
category=st.sidebar.multiselect('Select Product Category',options=data['Product Category'].unique(),default=data['Product Category'].unique())

selected_data=data[
    (data['Year'].isin(year))&
    (data['Month']>=data['Month'].min())&
    (data['Month']<=data['Month'].max())&
    (data['COUNTRY'].isin(country))&
    (data['Product Category'].isin(category))
]
#summary statics
st.header('Summary statics')
num_col=selected_data.select_dtypes(include='number').columns.tolist()
des=selected_data[num_col].describe().T[['mean','50%','count']]
des.rename(columns={'50%':'median'},inplace=True)
st.write(des)

#Interactive charts (e.g., bar, line, pie charts)
st.header('Interective Charts')
 
#Sales and category
st.bar_chart(selected_data,x='Product Category',y='SALES')
st.line_chart(selected_data,x='Month',y='SALES')
data=selected_data.groupby('Product Category')['SALES'].sum().reset_index()
fig=px.pie(data,names='Product Category',values='SALES',title='Pie Chart for sales by Category')
st.plotly_chart(fig)

