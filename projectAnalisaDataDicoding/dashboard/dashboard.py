import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('combined_data.csv')
    return df
def main():
    st.title('Bike Rental Analysis Dashboard')

    st.write("""

    Proyek Analisis Data: Bike-sharing-dataset
    - **Nama:** Antonius Miquel Aureliano
    - **Email:**
    - **ID Dicoding:** antonius_miquel_bDY0

    """)
    df = load_data()
    st.subheader('Data Overview')
    st.write(df.head())

    st.subheader('Trend of Bike Rentals from 2011 to 2012')

    rentals_2011 = df[df['yr_day'] == 0].groupby('mnth_day')['cnt_day'].sum()
    rentals_2012 = df[df['yr_day'] == 1].groupby('mnth_day')['cnt_day'].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(rentals_2011, label='2011', marker='o')
    plt.plot(rentals_2012, label='2012', marker='^')
    plt.title('Bike Rentals from 2011 to 2012')
    plt.xlabel('Month')
    plt.ylabel('Total Rentals')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend()
    st.pyplot()

    heatmap_data_hour = df[['temp_hour', 'atemp_hour', 'cnt_hour']]
    st.subheader('Heatmap for temp_hour, atemp_hour, cnt_hour')
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data_hour.corr(), annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})
    st.pyplot()

    heatmap_data_day = df[['temp_day', 'atemp_day', 'cnt_day']]
    st.subheader('Heatmap for temp_day, atemp_day, cnt_day')
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data_day.corr(), annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})
    st.pyplot()

    st.subheader('Average Rentals by Day of the Week and by Working Day')

    selected_year = st.selectbox('Select Year', ['2011', '2012', 'Combined'])

    if selected_year == '2011':
        df_year = df[df['yr_day'] == 0]  # Filter for year 2011
    elif selected_year == '2012':
        df_year = df[df['yr_day'] == 1]  # Filter for year 2012
    else:
        df_year = df

    rentals_by_day = df_year.groupby(['weekday_day', 'workingday_day'])['cnt_day'].mean().reset_index()

    weekday_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    rentals_by_day['weekday_day'] = rentals_by_day['weekday_day'].map(lambda x: weekday_names[x])

    plt.figure(figsize=(10, 6))
    sns.barplot(data=rentals_by_day, x='weekday_day', y='cnt_day', hue='workingday_day')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Daily Rentals')
    plt.xticks(range(7), weekday_names)
    plt.legend(title='Working Day')
    plt.grid(True)
    st.pyplot()

    st.subheader('Hourly Bike Rentals')

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_year, x='hr', y='cnt_hour', estimator='sum', marker='o')
    plt.title('Hourly Bike Rentals')
    plt.xlabel('Time of Day')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(range(24))
    plt.grid(True)
    st.pyplot()

    st.subheader('Hourly Bike Rentals - Working Day vs Holiday/Weekend')

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_year, x='hr', y='cnt_hour', hue='workingday_hour', estimator='sum', marker='o')
    plt.title('Hourly Bike Rentals - Working Day vs Holiday/Weekend')
    plt.xlabel('Time of Day')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(range(24))
    plt.grid(True)
    plt.legend(title='Day type', labels=['Working Day', 'Holiday/Weekend'])
    st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    main()



