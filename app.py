# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Get matplotlib graphs with dark background
plt.style.use('dark_background')

# Remove unnecessary warnings
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():

    html1 = """
        <div style="background-color:#e60067;border-radius:10px;border-style:solid;border-color:black;padding:10px;">
        <h2 style="color:white;text-align:center;">The Sparks Foundation</h2>
        <h3 style="color:white;text-align:center;">(Graduate Rotational Internship Program)</h3>
        </div>
        """
    st.markdown(html1,unsafe_allow_html=True)
    st.write('')
    st.sidebar.title('Exploratory Data Analysis - Retail')

    # Read data
    df = pd.read_csv('SampleSuperstore.csv')

    nav = st.sidebar.radio('',['Home',"Dataset","Technologies Used"])
    if nav == 'Home':
        choice = st.sidebar.radio('Choose any parameter',['Retail Data','Numerical Variables','Categorical Variables','Data insights','Conclusion'])
        if choice == 'Retail Data':
                    st.title('Task 3: Exploratory Data Analysis - Retail')
                    st.write('### Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’:')
                    st.write('As a business manager, try to ﬁnd out the weak areas where you can work to make more proﬁt.')
                    st.write('What all business problems you can derive by exploring the data?')
                    st.write('')
                    st.write('### Retail Data')
                    
                    # Display dataset
                    st.dataframe(df)
                    
                    # Shape of data
                    st.write('')
                    st.write('#### Shape of Dataset')
                    records, attributes = df.shape
                    st.write(f'There are {records} records and {attributes} attributes')

                    # Data dictionary
                    st.write('')
                    st.write('#### Data Dictionary')
                    st.write(f'''
                                `Ship Mode`: Mode of shipping used for shipment delivery
                                
                                `Segment`: Customer segment product was shipped to

                                `Country`: Country in which the shipment was delivered

                                `City`: City in which shipment was delivered

                                `State`: State in which the shipment was delivered

                                `Postal Code`: Postal code the shipment was delivered to

                                `Region`: Country region

                                `Category`: The category product belongs to

                                `Sub-Category`: Sub-category of the product

                                `Sales`: Sale made in USD

                                `Quantity`: Product quantity

                                `Discount`: Discount given on the product

                                `Profit`: Profit/loss made on the sale''')

                    # # Information about dataset
                    # st.write('')
                    # st.write('#### Dataset Information')
                    # st.write(df.describe(include='all'))

                    # # Chech for missing values
                    # st.write('')
                    # st.write('#### Missing Values')
                    # st.write(df.isna().sum())
                    # st.write('There are no missing values')
        
        if choice == 'Numerical Variables':
            st.title('Numerical Variables')

            # List of numerical variables
            numerical_features = [feature for feature in df.columns if df[feature].dtypes != 'O']

            st.write('Number of numerical variables: ', len(numerical_features))
            st.subheader(numerical_features)

            # Visualise the numerical variables
            st.dataframe(df[numerical_features])

            st.write('')
            # Correlation
            fig, ax = plt.subplots(figsize=(10,8))   
            sns.heatmap(df.corr(),cmap='rocket_r',annot=True, ax=ax)
            plt.title('Heatmap of correlation matrix', fontsize = 20)
            st.pyplot()

            st.write('')
            # Discrete Variables
            st.header('Discrete Variables')
            discrete_feature=[feature for feature in numerical_features if len(df[feature].unique())<25]
            st.write("Discrete Variables Count: ",len(discrete_feature))
            st.subheader(discrete_feature)
            st.dataframe(df[discrete_feature])

            # Set plotly for visualizing pandas dataframe
            pd.options.plotting.backend = "plotly"

            # Lets Find the realtionship between them and Sales
            for feature in discrete_feature:
                data=df.copy()
                fig = data.groupby(feature)['Sales'].median().plot(kind='bar')
                fig.update_layout(xaxis_title=feature, yaxis_title='Sales', title=f'Relation between {feature} and Sales', template='plotly_dark')
                st.plotly_chart(fig, user_container_width=True)

            st.write('')
            # Continuous Variable
            st.header('Continuous Variable')
            continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature]
            st.write("Continuous feature Count: ",len(continuous_feature))
            st.subheader(continuous_feature)
            st.dataframe(df[continuous_feature])

            # Histogram of Continuous Variables
            for feature in continuous_feature:
                data = df.copy()
                fig = px.histogram(data[feature], x=feature, title=f'{feature} Histogram', template='plotly_dark', nbins=50)
                st.plotly_chart(fig, user_container_width=True)         

        if choice == 'Categorical Variables':
            st.title('Categorical Variables')

            categorical_features=[feature for feature in df.columns if df[feature].dtypes=='O']
            st.write('Number of categorical variables: ', len(categorical_features))
            st.subheader(categorical_features)
            st.dataframe(df[categorical_features])

            st.write('')
            st.write('### No. of categories in each categorical feature: ')
            
            # Types of categories
            for feature in categorical_features:
                st.write('The feature is {} and number of categories are {}'.format(feature,len(df[feature].unique())))

            pd.options.plotting.backend = "plotly"

            st.write('### Relationship between each categorical variable and  Sales')
            # Find out the relationship between categorical variable and Sales
            for feature in categorical_features:
                data=df.copy()
                fig = data.groupby(feature)['Sales'].mean().plot.bar()
                fig.update_layout(xaxis_title=feature, yaxis_title='Sales', title=f'Relation between {feature} and Sales', template='plotly_dark')
                st.plotly_chart(fig, user_container_width=True) 

            st.write('### Relationship between each categorical variable and  Profit')
            # Find out the relationship between categorical variable and Profit
            for feature in categorical_features:
                data=df.copy()
                fig = data.groupby(feature)['Profit'].mean().plot.bar()
                fig.update_layout(xaxis_title=feature, yaxis_title='Overall Profit', title=f'Relation between {feature} and Profit', template='plotly_dark')
                st.plotly_chart(fig, user_container_width=True)

            st.write('### Relationship between each categorical variable and  Discount')
            # Find out the relationship between categorical variable and Discount
            for feature in categorical_features:
                data=df.copy()
                fig = data.groupby(feature)['Discount'].mean().plot.bar()
                fig.update_layout(xaxis_title=feature, yaxis_title='Discount', title=f'Relation between {feature} and Discount', template='plotly_dark')
                st.plotly_chart(fig, user_container_width=True)

        if choice == 'Data insights':
            st.title('Data insights')
            ch = st.sidebar.radio('Based on: ',['Ship Mode','Segment','Region','City','State','Category','Sub-Category'])
            if ch == 'Ship Mode':
                    st.header('Ship Mode')
                    image = Image.open('Pairplot_ShipMode.png')
                    st.image(image,use_column_width=True)

                    st.subheader('Ship Mode wise analysis of Sale, Discount, profit')
                    pd.options.plotting.backend = "matplotlib"
                    df_ShipMode= df.groupby(['Ship Mode'])[['Sales', 'Discount', 'Profit']].mean()
                    df_ShipMode.plot.pie(subplots=True, 
                                        autopct='%1.1f%%',
                                        figsize=(18, 20),
                                        startangle=90,     # start angle 90° (Africa)
                                        shadow=True,
                                        labels = df_ShipMode.index,
                                        colors=['r','b','g','m'])
                    plt.title('Ship Mode wise analysis of Sale, Discount, profit', fontsize = 20)
                    st.pyplot()

                    st.subheader('Profit w.r.t Ship Mode and Discount')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(10,6))
                    df.groupby(['Ship Mode', 'Discount']).Profit.mean().plot(kind = 'bar')
                    plt.title('Profit w.r.t Ship Mode and Discount', fontsize = 20)
                    plt.ylabel('Profit')
                    st.pyplot()

                    st.subheader('Sales w.r.t Ship Mode and Sub-Category')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(15,9))
                    color1 = ['r']*len(df['Sub-Category'].unique())
                    color2 = ['g']*len(df['Sub-Category'].unique())
                    color3 = ['b']*len(df['Sub-Category'].unique())
                    color4 = ['m']*len(df['Sub-Category'].unique())
                    color = color1 + color2 + color3 + color4
                    df.groupby(['Ship Mode', 'Sub-Category']).Sales.mean().plot(kind = 'bar', color=color)
                    plt.title('Sales w.r.t Ship Mode and Sub-Category', fontsize = 20)
                    plt.ylabel('Sales')
                    st.pyplot()

            if ch == 'Segment':
                    st.header('Segment')
                    image = Image.open('Pairplot_Segment.png')
                    st.image(image,use_column_width=True)

                    st.subheader('Segment wise analysis of Sale, Discount, profit')
                    pd.options.plotting.backend = "matplotlib"
                    df_segment= df.groupby(['Segment'])[['Sales', 'Discount', 'Profit']].mean()
                    df_segment.plot.pie(subplots=True, 
                                        autopct='%1.1f%%',
                                        figsize=(18, 20),
                                        startangle=90,     # start angle 90° (Africa)
                                        shadow=True,
                                        labels = df_segment.index,
                                        colors=['r','b','g'])
                    plt.title('Segment wise analysis of Sale, Discount, profit', fontsize = 20)
                    st.pyplot()

                    st.subheader('Profit w.r.t Segment and Discount')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(10,6))
                    color1 = ['g']*4
                    color2 = ['r']*8
                    color = color1 + color2
                    df.groupby(['Segment', 'Discount']).Profit.mean().plot(kind = 'bar',color=color)
                    plt.title('Profit w.r.t Segment and Discount', fontsize = 20)
                    plt.ylabel('Profit')
                    st.pyplot()

                    st.subheader('Sales w.r.t Segment and Sub-Category')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(15,9))
                    color1 = ['r']*len(df['Sub-Category'].unique())
                    color2 = ['g']*len(df['Sub-Category'].unique())
                    color3 = ['b']*len(df['Sub-Category'].unique())
                    color = color1 + color2+ color3
                    df.groupby(['Segment', 'Sub-Category']).Sales.mean().plot(kind = 'bar', color=color)
                    plt.title('Sales w.r.t Segment and Sub-Category', fontsize = 20)
                    plt.ylabel('Sales')
                    st.pyplot()

            if ch == 'Region':
                    st.header('Region')
                    image = Image.open('Pairplot_Region.png')
                    st.image(image,use_column_width=True)

                    st.subheader('Region wise analysis of Profit, Discount and sell')
                    pd.options.plotting.backend = "matplotlib"
                    df_region= df.groupby(['Region'])[['Sales', 'Discount', 'Profit']].mean()
                    df_region.plot.pie(subplots=True, 
                                        autopct='%1.1f%%',
                                        figsize=(18, 20),
                                        startangle=90,     # start angle 90° (Africa)
                                        shadow=True,
                                        labels = df_region.index,
                                        colors=['r','b','g','m'])
                    plt.title('Region wise analysis of Sale, Discount, profit', fontsize = 20)
                    st.pyplot()

                    st.subheader('Profit w.r.t Region and Discount')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(10,6))
                    df.groupby(['Region', 'Discount']).Profit.mean().plot(kind = 'bar')
                    plt.title('Profit w.r.t Region and Discount', fontsize = 20)
                    plt.ylabel('Profit')
                    st.pyplot()

                    st.subheader('Sales w.r.t Region and Sub-Category')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(15,9))
                    color1 = ['r']*len(df['Sub-Category'].unique())
                    color2 = ['g']*len(df['Sub-Category'].unique())
                    color3 = ['b']*len(df['Sub-Category'].unique())
                    color4 = ['m']*len(df['Sub-Category'].unique())
                    color = color1 + color2 + color3 + color4
                    df.groupby(['Region', 'Sub-Category']).Sales.mean().plot(kind = 'bar', color=color)
                    plt.title('Sales w.r.t Region and Sub-Category', fontsize = 20)
                    plt.ylabel('Sales')
                    st.pyplot()

            if ch == 'City':
                    st.header('City')

                    st.subheader('City Wise Deal Analysis (Top 50)')
                    pd.options.plotting.backend = "matplotlib"
                    df2 = df['City'].value_counts()
                    df2.head(50).plot(kind='bar',figsize=(15,5))
                    plt.ylabel('Frequency / Number of deals')
                    plt.xlabel('City')
                    plt.title('City Wise Dealings', fontsize = 20)
                    st.pyplot()

                    st.subheader('Citywise Profit Analysis')
                    pd.options.plotting.backend = "matplotlib"
                    # Top 30 Cities with low profits
                    df_city= df.groupby(['City'])[['Sales', 'Discount', 'Profit']].mean()
                    df_city = df_city.sort_values('Profit')
                    df_city['Profit'].head(30).plot(kind='bar',figsize=(15,5), color = 'r')
                    plt.title('Top 30 Cities with Loss', fontsize = 20)
                    plt.ylabel('Loss')
                    st.pyplot()

                    # Top 30 Cities with high profits
                    df_city['Profit'].tail(30).plot(kind='bar',figsize=(15,5), color = 'g')
                    plt.title('Top 30 Cities with Profit', fontsize = 20)
                    plt.ylabel('Profit')
                    st.pyplot()

            if ch == 'State':
                    st.header('State')

                    state_code = {
                        'Alabama': 'AL',
                        'Alaska': 'AK',
                        'American Samoa': 'AS',
                        'Arizona': 'AZ',
                        'Arkansas': 'AR',
                        'California': 'CA',
                        'Colorado': 'CO',
                        'Connecticut': 'CT',
                        'Delaware': 'DE',
                        'District of Columbia': 'DC',
                        'Florida': 'FL',
                        'Georgia': 'GA',
                        'Guam': 'GU',
                        'Hawaii': 'HI',
                        'Idaho': 'ID',
                        'Illinois': 'IL',
                        'Indiana': 'IN',
                        'Iowa': 'IA',
                        'Kansas': 'KS',
                        'Kentucky': 'KY',
                        'Louisiana': 'LA',
                        'Maine': 'ME',
                        'Maryland': 'MD',
                        'Massachusetts': 'MA',
                        'Michigan': 'MI',
                        'Minnesota': 'MN',
                        'Mississippi': 'MS',
                        'Missouri': 'MO',
                        'Montana': 'MT',
                        'Nebraska': 'NE',
                        'Nevada': 'NV',
                        'New Hampshire': 'NH',
                        'New Jersey': 'NJ',
                        'New Mexico': 'NM',
                        'New York': 'NY',
                        'North Carolina': 'NC',
                        'North Dakota': 'ND',
                        'Northern Mariana Islands':'MP',
                        'Ohio': 'OH',
                        'Oklahoma': 'OK',
                        'Oregon': 'OR',
                        'Pennsylvania': 'PA',
                        'Puerto Rico': 'PR',
                        'Rhode Island': 'RI',
                        'South Carolina': 'SC',
                        'South Dakota': 'SD',
                        'Tennessee': 'TN',
                        'Texas': 'TX',
                        'Utah': 'UT',
                        'Vermont': 'VT',
                        'Virgin Islands': 'VI',
                        'Virginia': 'VA',
                        'Washington': 'WA',
                        'West Virginia': 'WV',
                        'Wisconsin': 'WI',
                        'Wyoming': 'WY'
                    }
                    df['state_code'] =df.State.apply(lambda x: state_code[x])

                    state_data = df[['Sales', 'Profit', 'state_code']].groupby(['state_code']).sum()
                    fig = go.Figure(data=go.Choropleth(
                        locations=state_data.index, 
                        z = state_data.Sales, 
                        locationmode = 'USA-states', 
                        colorscale = 'Reds',
                        colorbar_title = 'Sales in USD',
                    ))
                    fig.update_layout(
                        title_text = 'Total State-Wise Sales',
                        geo_scope='usa',
                        height=800,
                        template='plotly_dark'
                    )
                    st.plotly_chart(fig, user_container_width=True)

                    fig = go.Figure(data=go.Choropleth(
                        locations=state_data.index, # Spatial coordinates
                        z = state_data.Profit, # Data to be color-coded
                        locationmode = 'USA-states', # set of locations match entries in `locations`
                        colorscale = [[0, 'rgb(255,0,0)'], [0.25, 'rgb(255,255,255)'], [0.45, 'rgb(124,208,247)'], [0.6, 'rgb(97,255,140)'], [1, 'rgb(8,181,0)']],
                        colorbar_title = 'Profits in USD',
                    ))

                    fig.update_layout(
                        title_text = 'Total State-Wise Profit/Loss',
                        geo_scope='usa', # limite map scope to USA
                        height=600,
                        template='plotly_dark'
                    )
                    st.plotly_chart(fig, user_container_width=True)

                    st.subheader('State Wise Dealings')
                    pd.options.plotting.backend = "matplotlib"
                    df1 = df['State'].value_counts()
                    df1.plot(kind='bar',figsize=(15,5))
                    plt.ylabel('Frequency / Number of deals')
                    plt.xlabel('States')
                    plt.title('State Wise Dealings', fontsize = 20)
                    st.pyplot()

                    state_data = df[['Sales', 'Profit', 'state_code']].groupby(['state_code']).sum()
                    # Plots the turnover generated by different product categories and sub-categories for the list of given states
                    def state_data_viewer(states):
                        product_data = df.groupby(['State'])
                        for state in states:
                            data = product_data.get_group(state).groupby(['Category'])
                            fig,ax =plt.subplots(1, 3, figsize= (30,4))
                            fig.suptitle(state, fontsize=20)
                            ax_index =0
                            for cat in ['Furniture', 'Office Supplies', 'Technology']:
                                cat_data = data.get_group(cat).groupby(['Sub-Category']).sum()
                                sns.barplot(x=cat_data.Profit, y= cat_data.index, ax =ax[ax_index])
                                ax[ax_index].set_ylabel(cat)
                                ax_index+=1
                            st.pyplot()
                    st.subheader('Turnover generated by different product categories and sub-categories for the list of given states')
                    states =['California', 'Mississippi', 'Texas','Washington','Arizona']
                    st.write(states)
                    state_data_viewer(states)

            if ch == 'Category':
                    st.header('Category')
                    image = Image.open('Pairplot_Category.png')
                    st.image(image,use_column_width=True)

                    st.subheader('Category wise analysis of Profit, Discount and sell')
                    pd.options.plotting.backend = "matplotlib"
                    df_cat= df.groupby(['Category'])[['Sales', 'Discount', 'Profit']].mean()
                    df_cat.plot.pie(subplots=True, 
                                        autopct='%1.1f%%',
                                        figsize=(18, 20),
                                        startangle=90,     # start angle 90° (Africa)
                                        shadow=True,
                                        labels = df_cat.index,
                                        colors=['r','b','g'])
                    plt.title('Category wise analysis of Sale, Discount, profit', fontsize = 20)
                    st.pyplot()

                    st.subheader('Profit w.r.t Category and Discount')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(10,6))
                    df.groupby(['Category', 'Discount']).Profit.mean().plot(kind = 'bar')
                    plt.title('Profit w.r.t Category and Discount', fontsize = 20)
                    plt.ylabel('Profit')
                    st.pyplot()

                    st.subheader('Sales w.r.t Category and Sub-Category')
                    pd.options.plotting.backend = "matplotlib"
                    plt.figure(figsize=(15,9))
                    color1 = ['r']*4
                    color2 = ['g']*9
                    color3 = ['b']*4
                    color = color1 + color2+ color3
                    df.groupby(['Category', 'Sub-Category']).Sales.mean().plot(kind = 'bar', color=color)
                    plt.title('Sales w.r.t Category and Sub-Category', fontsize = 20)
                    plt.ylabel('Sales')
                    st.pyplot()

            if ch == 'Sub-Category':
                    st.header('Sub-Category')

                    st.subheader('Sub-Category: Sales and Profit Analysis')
                    pd.options.plotting.backend = "matplotlib"
                    df_sub_category= df.groupby(['Sub-Category'])[['Sales', 'Discount', 'Profit']].mean()
                    df_sub_category.sort_values('Profit')[['Sales','Profit']].plot(kind='bar', figsize=(15,10))
                    plt.title('Sales and Profit w.r.t Sub-Category', fontsize = 20)
                    plt.ylabel('Values')
                    st.pyplot()

                    df['price_per_product'] = df.Sales / df.Quantity
                    df['profit_per_product'] = df.Profit / df.Quantity 

                    data = df.groupby(['Category'])

                    st.subheader('Prices of products across each product category')
                    for cat, df in data:
                        sizes = np.absolute(df.price_per_product)
                        fig = px.scatter(df, x = 'price_per_product', title = cat.upper(), 
                                        color = 'Sub-Category',
                                        size = sizes, hover_data=['Sub-Category'])
                        fig.update_layout(
                            height = 500,
                            xaxis = dict(title='Price Per Product'),
                            yaxis = dict(title=''),
                            template='plotly_dark'
                        )
                        st.plotly_chart(fig, user_container_width=True)
                    
                    st.subheader('Profit of products across each product category')
                    for cat, df in data:
                        sizes = np.absolute(df.profit_per_product)
                        fig = px.scatter(df, x = 'profit_per_product', title = cat.upper(), 
                                        color = 'Sub-Category',
                                        size = sizes, hover_data=['Sub-Category'])
                        fig.update_layout(
                            height = 500,
                            xaxis = dict(title='Profit Per Product'),
                            yaxis = dict(title=''),
                            template='plotly_dark'
                        )
                        st.plotly_chart(fig, user_container_width=True)

        if choice == 'Conclusion':
            st.title('Conclusion')
            html6 = """
            <div>
            <ul>
                <li>Sales and profit are positively correlated to a certain extent whereas discount and profit are negatively correlated.</li>
                <li>Average number of deals per state in United States is 204 and average number of deals per city in United States is 19.</li>
                <li>The company has the highest sales in the state of California selling around $450K of goods with profits of over $75K.</li>
                <li>New York is the state with the second highest sales, with more than $300k worth of goods sold with profits of over $75K similar to California.</li>
                <li>The state of Texas, with the third highest sales proved to be the most expensive state for the company with a very high loss of around $25K.</li>
            </ul>
            </div>
            """
            st.markdown(html6,unsafe_allow_html=True)

            st.write('')
            st.header('How to increase Profit?')
            html7 = """
            <div>
            <ul style="list-style-type:square;">
                <li>Discount should be kept lower than 30%.</li>
                <li>Discount of 50% on the same day should be avoided at all costs as it leads to major loss.</li>
                <li>Sales of copiers in technology in the home office segment category should be escalated.</li>
                <li>Moreover, increased sales from first class ship mode may provide substantial gain.</li>
                <li>Sales in Texas and Ohio should be declined.</li>
                <li>Additionally, sales of furniture and machines should not be encouraged.</li>
            </ul>
            </div>
            """
            st.markdown(html7,unsafe_allow_html=True)

    if nav == 'Technologies Used':
        st.title("Technologies Used")
        html5 = """
        <div>
        <ul>
            <li>Python</li>
            <li>Numpy</li>
            <li>Pandas</li>
            <li>Matplotlib</li>
            <li>Seaborn</li>
            <li>Plotly</li>
            <li>Visual Studio Code</li>
        </ul>
        </div>
        """
        st.markdown(html5,unsafe_allow_html=True)

    if nav == 'Dataset':
        st.header('The data can be downloaded from the given link:')
        html_string = "<div><a href='https://bit.ly/3i4rbWl' style='color:#454eff; text-decoration:none; font-size:20px'>Retail Dataset</a></div>"
        st.markdown(html_string, unsafe_allow_html=True)


    st.sidebar.header('Developed by')
    html_string = "<div><a href='https://ritwiksharma107.github.io/portfolio/' style='color:#e60067; text-decoration:none; font-size:30px'>Ritwik Sharma</a></div>"
    st.sidebar.markdown(html_string, unsafe_allow_html=True)
    st.sidebar.write('**Data Science and Business Analytics Intern**')

if __name__ == '__main__':
    main()
