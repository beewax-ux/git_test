import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

df["continent"] = df["continent"].apply(lambda x: x.replace(".", ""))

st.title("The Overview of Cars Characteristics by Continent ")


#je crée le BOUTON pour choisir le continent
filtre = st.selectbox(label="Choose the continent", options=df["continent"].unique())
st.write("You've selected:", filtre)

#Je cree le DF avec la condition ( le continent change en fonction de filtre
df_copy = df[df["continent"].str.contains(filtre)]

#First Chart
st.title("Data Visualization")

axes, fig = plt.subplots(2, 2, figsize=(20, 15))

ax1 = plt.subplot(2, 2, 1)
ax1 = sns.barplot(data=df_copy, x="continent", y="hp")
ax1.set_title('The Horse Power',
              fontdict = {'fontsize': 18,
                              'fontweight': 'bold',
                              'color': 'midnightblue'})

ax1 = plt.subplot(2, 2, 2)
ax1 = sns.scatterplot(data=df_copy, x="hp", y="cylinders")
ax1.set_title('Relation between Horse Power and Number of Cylinders ',
              fontdict = {'fontsize': 18,
                              'fontweight': 'bold',
                              'color': 'midnightblue'})

ax1 = plt.subplot(2, 2, 3)
ax1 = sns.barplot(data=df_copy, x="year", y="cylinders")
ax1.set_title('Number of Cylinders by year',
              fontdict = {'fontsize': 18,
                              'fontweight': 'bold',
                              'color': 'midnightblue'})

ax1 = plt.subplot(2, 2, 4)
ax1 = sns.scatterplot(data=df_copy, x="weightlbs", y="mpg")
ax1.set_title('The Weight VS Miles per Gallon',
              fontdict = {'fontsize': 18,
                              'fontweight': 'bold',
                              'color': 'midnightblue'})
st.pyplot(ax1.figure)


#THE SECOND CHART:
st.title("The horspower VS time to 60")

plt.figure(figsize=(20, 15))

ad=st.scatter_chart(data=df_copy, x="hp", y="time-to-60")
st.pyplot(ad.figure)

